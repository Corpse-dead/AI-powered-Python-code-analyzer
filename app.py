"""
Smart Code Review Assistant - FastAPI Backend
Analyzes Python code using ML models and provides quality metrics
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pathlib import Path
from typing import Dict, Any
import os

from src.code_analyzer import CodeAnalyzer
from src.ml_models import CodeQualityPredictor

app = FastAPI(title="Smart Code Review Assistant", version="1.0.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_path = Path(__file__).parent / "static"
static_path.mkdir(exist_ok=True)
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")

# Initialize analyzers
code_analyzer = CodeAnalyzer()
ml_predictor = CodeQualityPredictor()


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main HTML page"""
    html_file = Path(__file__).parent / "static" / "index.html"
    if html_file.exists():
        return html_file.read_text(encoding='utf-8')
    return "<h1>Smart Code Review Assistant</h1><p>Upload code to analyze!</p>"


@app.post("/api/analyze")
async def analyze_code(file: UploadFile = File(...)) -> Dict[str, Any]:
    """
    Analyze uploaded Python code file
    
    Args:
        file: Uploaded Python file
        
    Returns:
        Analysis results including metrics, suggestions, and ML predictions
    """
    if not file.filename.endswith('.py'):
        raise HTTPException(status_code=400, detail="Only Python files (.py) are supported")
    
    try:
        # Read file content
        content = await file.read()
        code = content.decode('utf-8')
        
        # Perform analysis
        static_analysis = code_analyzer.analyze(code)
        ml_prediction = ml_predictor.predict_quality(code, static_analysis)
        suggestions = code_analyzer.get_suggestions(static_analysis)
        
        return {
            "filename": file.filename,
            "metrics": static_analysis,
            "ml_prediction": ml_prediction,
            "suggestions": suggestions,
            "overall_score": ml_prediction.get("quality_score", 0)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing code: {str(e)}")


@app.post("/api/analyze-text")
async def analyze_code_text(code: dict) -> Dict[str, Any]:
    """
    Analyze Python code from text input
    
    Args:
        code: Dictionary with 'code' key containing Python code string
        
    Returns:
        Analysis results
    """
    try:
        code_text = code.get("code", "")
        if not code_text:
            raise HTTPException(status_code=400, detail="No code provided")
        
        # Perform analysis
        static_analysis = code_analyzer.analyze(code_text)
        ml_prediction = ml_predictor.predict_quality(code_text, static_analysis)
        suggestions = code_analyzer.get_suggestions(static_analysis)
        
        return {
            "metrics": static_analysis,
            "ml_prediction": ml_prediction,
            "suggestions": suggestions,
            "overall_score": ml_prediction.get("quality_score", 0)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing code: {str(e)}")


@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": "1.0.0"}


if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
