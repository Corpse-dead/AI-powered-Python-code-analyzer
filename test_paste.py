"""
Test the paste code API endpoint
"""
import requests
import json

# Sample code to paste and analyze
sample_code = '''
def fibonacci(n):
    """Calculate Fibonacci number using recursion"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Calculate 10th Fibonacci number
result = fibonacci(10)
print(f"The 10th Fibonacci number is: {result}")
'''

print("🔄 Testing PASTE CODE functionality...")
print("=" * 70)

try:
    # Send POST request to analyze-text endpoint
    response = requests.post(
        'http://localhost:8000/api/analyze-text',
        json={'code': sample_code},
        headers={'Content-Type': 'application/json'}
    )
    
    if response.status_code == 200:
        result = response.json()
        
        print("\n✅ PASTE CODE ANALYSIS SUCCESSFUL!")
        print("=" * 70)
        print(f"\n🎯 Quality Score: {result['overall_score']}/100")
        print(f"📝 Grade: {result['ml_prediction']['rating']}")
        print(f"🤖 Prediction: {result['ml_prediction']['prediction']}")
        print(f"💪 Confidence: {result['ml_prediction']['confidence']}%")
        
        print(f"\n📊 CODE METRICS:")
        print(f"   • Lines of Code: {result['metrics']['lines_of_code']}")
        print(f"   • Functions: {result['metrics']['num_functions']}")
        print(f"   • Avg Complexity: {result['metrics']['avg_complexity']}")
        print(f"   • Maintainability Index: {result['metrics']['maintainability_index']}")
        print(f"   • Comments: {result['metrics']['comments']}")
        print(f"   • Comment Ratio: {result['metrics']['comment_ratio']*100:.1f}%")
        
        print(f"\n💡 SUGGESTIONS:")
        for i, suggestion in enumerate(result['suggestions'], 1):
            print(f"   {i}. {suggestion}")
        
        if result['metrics']['code_smells']:
            print(f"\n🔍 CODE SMELLS DETECTED:")
            for smell in result['metrics']['code_smells']:
                print(f"   ⚠️  {smell}")
        else:
            print(f"\n✅ No code smells detected!")
        
        print("\n" + "=" * 70)
        print("✨ This is exactly what you'll see in the web interface!")
        print("=" * 70)
        
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
        
except requests.exceptions.ConnectionError:
    print("❌ Error: Could not connect to server")
    print("Make sure the server is running at http://localhost:8000")
except Exception as e:
    print(f"❌ Error: {e}")
