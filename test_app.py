"""
Quick test script for the Smart Code Review Assistant
Run this to verify the application is working correctly
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.code_analyzer import CodeAnalyzer
from src.ml_models import CodeQualityPredictor


def test_code_analyzer():
    """Test the CodeAnalyzer"""
    print("Testing Code Analyzer...")
    
    sample_code = '''
def calculate_average(numbers):
    """Calculate average of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

class Calculator:
    def add(self, a, b):
        return a + b
'''
    
    analyzer = CodeAnalyzer()
    results = analyzer.analyze(sample_code)
    
    print(f"✓ Lines of Code: {results.get('lines_of_code', 0)}")
    print(f"✓ Functions: {results.get('num_functions', 0)}")
    print(f"✓ Classes: {results.get('num_classes', 0)}")
    print(f"✓ Maintainability Index: {results.get('maintainability_index', 0)}")
    
    return True


def test_ml_model():
    """Test the ML predictor"""
    print("\nTesting ML Model...")
    
    sample_code = '''
def well_documented_function(param1: str, param2: int) -> bool:
    """
    A well-documented function with type hints.
    
    Args:
        param1: First parameter
        param2: Second parameter
        
    Returns:
        Boolean result
    """
    result = param1 and param2
    return bool(result)
'''
    
    predictor = CodeQualityPredictor()
    results = predictor.predict_quality(sample_code)
    
    print(f"✓ Quality Score: {results.get('quality_score', 0)}/100")
    print(f"✓ Grade: {results.get('rating', 'N/A')}")
    print(f"✓ Prediction: {results.get('prediction', 'N/A')}")
    print(f"✓ Confidence: {results.get('confidence', 0)}%")
    
    return True


def main():
    """Run all tests"""
    print("=" * 50)
    print("Smart Code Review Assistant - Test Suite")
    print("=" * 50)
    
    try:
        test_code_analyzer()
        test_ml_model()
        
        print("\n" + "=" * 50)
        print("✅ All tests passed!")
        print("=" * 50)
        print("\nTo start the application, run:")
        print("  python app.py")
        print("\nThen open: http://localhost:8000")
        
        return 0
    
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
