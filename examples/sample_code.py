"""
Example Python code for testing the Code Review Assistant
This file demonstrates various code quality levels
"""


def good_example(numbers: list) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numeric values
        
    Returns:
        Average value as float
    """
    if not numbers:
        return 0.0
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    return average


class DataProcessor:
    """A well-documented class for data processing"""
    
    def __init__(self, data: list):
        """Initialize with data"""
        self.data = data
        self.processed = False
    
    def process(self) -> dict:
        """Process the data and return results"""
        result = {
            'count': len(self.data),
            'sum': sum(self.data) if self.data else 0
        }
        self.processed = True
        return result


# Bad example (for testing detection)
def bad():
    x=1;y=2;z=3
    if x:
        if y:
            if z:
                return 12345


if __name__ == "__main__":
    # Test the good example
    numbers = [1, 2, 3, 4, 5]
    avg = good_example(numbers)
    print(f"Average: {avg}")
    
    # Test the processor
    processor = DataProcessor(numbers)
    result = processor.process()
    print(f"Results: {result}")
