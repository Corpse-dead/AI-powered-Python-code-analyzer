"""
ML Models Module
Uses machine learning to predict code quality
"""

import re
import numpy as np
from typing import Dict, Any
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path


class CodeQualityPredictor:
    """ML-based code quality prediction"""
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=100, ngram_range=(1, 2))
        self.model = RandomForestClassifier(n_estimators=50, random_state=42)
        self._train_initial_model()
    
    def _train_initial_model(self):
        """Train a basic model with synthetic examples"""
        # Training samples (good vs bad code patterns)
        training_samples = [
            # Good code examples
            ("def calculate_sum(numbers): return sum(numbers)", "good"),
            ("class DataProcessor:\n    def __init__(self):\n        self.data = []", "good"),
            ("def validate_email(email: str) -> bool:\n    return '@' in email", "good"),
            ("import logging\nlogger = logging.getLogger(__name__)", "good"),
            ("def process_data(data: list) -> dict:\n    result = {}\n    return result", "good"),
            
            # Bad code examples
            ("def f(x): return x+x+x+x+x+x", "bad"),
            ("a=1;b=2;c=3;d=4;e=5;f=6", "bad"),
            ("def foo():\n    if True:\n        if True:\n            if True:\n                pass", "bad"),
            ("x = 12345678; y = 98765432", "bad"),
            ("def function(a,b,c,d,e,f,g,h,i): pass", "bad"),
        ]
        
        # Add more synthetic examples
        good_patterns = [
            "def well_named_function():\n    '''Docstring'''\n    pass",
            "class MyClass:\n    '''Class docstring'''\n    pass",
            "# This is a helpful comment\nresult = process_input(data)",
            "try:\n    risky_operation()\nexcept Exception as e:\n    handle_error(e)",
            "with open('file.txt') as f:\n    content = f.read()",
        ]
        
        bad_patterns = [
            "def a(): pass\ndef b(): pass\ndef c(): pass",
            "x=1;y=2;z=3;a=4;b=5;c=6;d=7",
            "global var1, var2, var3, var4",
            "eval(user_input)",
            "except: pass",
        ]
        
        all_samples = (
            training_samples + 
            [(p, "good") for p in good_patterns] +
            [(p, "bad") for p in bad_patterns]
        )
        
        codes, labels = zip(*all_samples)
        
        # Extract features
        X = self.vectorizer.fit_transform(codes)
        y = [1 if label == "good" else 0 for label in labels]
        
        # Train model
        self.model.fit(X, y)
    
    def predict_quality(self, code: str, metrics: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Predict code quality using ML model with optional static metrics
        
        Args:
            code: Python source code
            metrics: Optional static analysis metrics for better scoring
            
        Returns:
            Dictionary with prediction results
        """
        try:
            # Extract features
            features = self._extract_features(code)
            
            # Vectorize code
            X = self.vectorizer.transform([code])
            
            # Predict
            prediction = self.model.predict(X)[0]
            probabilities = self.model.predict_proba(X)[0]
            
            # Calculate quality score (0-100)
            if metrics and 'maintainability_index' in metrics:
                # Use static metrics for better scoring
                quality_score = self._calculate_composite_score(features, probabilities, metrics)
            else:
                quality_score = self._calculate_quality_score(features, probabilities)
            
            return {
                "quality_score": round(quality_score, 2),
                "prediction": "good" if quality_score >= 70 else "needs_improvement",
                "confidence": round(max(probabilities) * 100, 2),
                "features": features,
                "rating": self._get_rating(quality_score)
            }
        
        except Exception as e:
            return {
                "quality_score": 50,
                "prediction": "unknown",
                "confidence": 0,
                "error": str(e),
                "rating": "C"
            }
    
    def _extract_features(self, code: str) -> Dict[str, Any]:
        """Extract features from code"""
        lines = code.split('\n')
        
        return {
            "line_length_avg": sum(len(line) for line in lines) / len(lines) if lines else 0,
            "has_docstrings": '"""' in code or "'''" in code,
            "has_type_hints": '->' in code or ': ' in code,
            "num_comments": len(re.findall(r'#.*', code)),
            "num_functions": len(re.findall(r'def\s+\w+', code)),
            "num_classes": len(re.findall(r'class\s+\w+', code)),
            "has_main_guard": '__main__' in code,
            "uses_comprehension": '[' in code and 'for' in code,
            "proper_naming": bool(re.search(r'def\s+[a-z_][a-z0-9_]*', code)),
        }
    
    def _calculate_quality_score(self, features: Dict[str, Any], probabilities: np.ndarray) -> float:
        """Calculate overall quality score with balanced weighting"""
        # Base score from ML prediction (40% weight)
        ml_score = probabilities[1] * 100
        base_score = ml_score * 0.4
        
        # Feature-based score (60% weight)
        feature_score = 50  # Start at middle
        
        # Positive features (each worth up to 10 points)
        if features["has_docstrings"]:
            feature_score += 8
        if features["has_type_hints"]:
            feature_score += 8
        if features["num_comments"] > 0:
            feature_score += 4  # Reduced weight for comments
        if features["has_main_guard"]:
            feature_score += 3
        if features["proper_naming"]:
            feature_score += 7
        if features["uses_comprehension"]:
            feature_score += 3
        
        # Penalties
        if features["line_length_avg"] > 100:
            feature_score -= 5
        if features["num_functions"] == 0 and features["num_classes"] == 0:
            feature_score -= 10  # Empty or trivial code
        
        # Combine scores
        final_score = min(100, max(0, base_score + feature_score * 0.6))
        return final_score
    
    def _calculate_composite_score(self, features: Dict[str, Any], 
                                   probabilities: np.ndarray, 
                                   metrics: Dict[str, Any]) -> float:
        """Calculate score using both ML and static analysis metrics"""
        # ML component (30% weight)
        ml_score = probabilities[1] * 100 * 0.3
        
        # Maintainability Index (30% weight) - normalized to 0-100
        mi_score = metrics.get('maintainability_index', 50) * 0.3
        
        # Complexity (20% weight) - lower is better
        complexity = metrics.get('avg_complexity', 5)
        complexity_score = max(0, 100 - (complexity * 5)) * 0.2
        
        # Feature-based (20% weight)
        feature_score = 0
        if features["has_docstrings"]:
            feature_score += 5
        if features["has_type_hints"]:
            feature_score += 5
        if features["proper_naming"]:
            feature_score += 4
        if features["num_comments"] > 0:
            feature_score += 2
        if metrics.get('comment_ratio', 0) > 0.1:
            feature_score += 4
        
        feature_score = min(100, feature_score * 5) * 0.2
        
        # Calculate final score
        final_score = ml_score + mi_score + complexity_score + feature_score
        return min(100, max(0, final_score))
    
    def _get_rating(self, score: float) -> str:
        """Convert score to letter grade"""
        if score >= 85:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 55:
            return "C"
        elif score >= 40:
            return "D"
        else:
            return "F"
