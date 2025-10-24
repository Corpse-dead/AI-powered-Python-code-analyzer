"""
Demo script to show how the Smart Code Review Assistant works
"""

# Sample code to analyze - Good example
good_code = '''
def calculate_statistics(numbers: list) -> dict:
    """
    Calculate statistical measures for a list of numbers.
    
    Args:
        numbers: List of numeric values
        
    Returns:
        Dictionary containing mean, median, and sum
    """
    if not numbers:
        return {"mean": 0, "median": 0, "sum": 0}
    
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    # Calculate mean
    mean = sum(sorted_nums) / n
    
    # Calculate median
    if n % 2 == 0:
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    
    return {
        "mean": mean,
        "median": median,
        "sum": sum(sorted_nums)
    }
'''

# Sample code to analyze - Bad example
bad_code = '''
def f(x):
    a=1;b=2;c=3;d=4;e=5
    if x:
        if a:
            if b:
                if c:
                    if d:
                        return 12345678
    return a+b+c+d+e
'''

print("=" * 70)
print("🤖 SMART CODE REVIEW ASSISTANT - DEMO")
print("=" * 70)

# Analyze the good code
print("\n📊 ANALYZING GOOD CODE EXAMPLE...")
print("-" * 70)

from src.code_analyzer import CodeAnalyzer
from src.ml_models import CodeQualityPredictor

analyzer = CodeAnalyzer()
predictor = CodeQualityPredictor()

# Good code analysis
good_metrics = analyzer.analyze(good_code)
good_ml = predictor.predict_quality(good_code)
good_suggestions = analyzer.get_suggestions(good_metrics)

print(f"\n✅ GOOD CODE RESULTS:")
print(f"   Quality Score: {good_ml['quality_score']}/100 (Grade: {good_ml['rating']})")
print(f"   Prediction: {good_ml['prediction']}")
print(f"   Confidence: {good_ml['confidence']}%")
print(f"\n   📈 Metrics:")
print(f"      • Lines of Code: {good_metrics['lines_of_code']}")
print(f"      • Functions: {good_metrics['num_functions']}")
print(f"      • Avg Complexity: {good_metrics['avg_complexity']}")
print(f"      • Maintainability Index: {good_metrics['maintainability_index']}")
print(f"      • Comment Ratio: {good_metrics['comment_ratio']*100:.1f}%")
print(f"\n   💡 Top Suggestions:")
for suggestion in good_suggestions[:3]:
    print(f"      • {suggestion}")

# Bad code analysis
print("\n" + "=" * 70)
print("📊 ANALYZING BAD CODE EXAMPLE...")
print("-" * 70)

bad_metrics = analyzer.analyze(bad_code)
bad_ml = predictor.predict_quality(bad_code)
bad_suggestions = analyzer.get_suggestions(bad_metrics)

print(f"\n⚠️  BAD CODE RESULTS:")
print(f"   Quality Score: {bad_ml['quality_score']}/100 (Grade: {bad_ml['rating']})")
print(f"   Prediction: {bad_ml['prediction']}")
print(f"   Confidence: {bad_ml['confidence']}%")
print(f"\n   📈 Metrics:")
print(f"      • Lines of Code: {bad_metrics['lines_of_code']}")
print(f"      • Functions: {bad_metrics['num_functions']}")
print(f"      • Avg Complexity: {bad_metrics['avg_complexity']}")
print(f"      • Maintainability Index: {bad_metrics['maintainability_index']}")
print(f"\n   🔍 Code Smells Detected:")
for smell in bad_metrics['code_smells']:
    print(f"      • {smell}")
print(f"\n   💡 Top Suggestions:")
for suggestion in bad_suggestions[:3]:
    print(f"      • {suggestion}")

print("\n" + "=" * 70)
print("✨ HOW TO USE THE WEB INTERFACE:")
print("=" * 70)
print("\n1. Open http://localhost:8000 in your browser")
print("2. Choose one of two options:")
print("   • Upload a .py file using 'Upload File' section")
print("   • Paste Python code into the text area")
print("3. Click 'Analyze File' or 'Analyze Code'")
print("4. View beautiful results with scores, metrics, and suggestions!")
print("\n" + "=" * 70)
