# Smart Code Review Assistant Project

An AI-powered Python code analyzer that uses machine learning to evaluate code quality, detect code smells, and provide actionable improvement suggestions.

## Project Stack
- **Backend**: FastAPI with Uvicorn
- **ML/AI**: scikit-learn (RandomForest), NumPy
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Code Analysis**: Radon, Python AST, custom analyzers

## Project Structure
- `app.py` - FastAPI application entry point
- `src/code_analyzer.py` - Static code analysis module
- `src/ml_models.py` - ML-based quality prediction
- `static/` - Web interface (HTML/CSS/JS)
- `test_app.py` - Test suite

## Development Guidelines
- Use Python 3.8+ best practices
- Follow PEP 8 style guidelines
- Include type hints in function signatures
- Write docstrings for all functions and classes
- Keep ML model predictions efficient and scalable
- Use virtual environment (.venv) for dependencies
- Test changes with `python test_app.py`

## Running the Application
1. Activate venv: `.venv\Scripts\activate`
2. Run server: `python app.py`
3. Open browser: http://localhost:8000

## Key Features
- ML-based code quality scoring (0-100)
- Static analysis (complexity, maintainability, Halstead metrics)
- Code smell detection
- Smart improvement suggestions
- Modern web interface with file upload and code paste
