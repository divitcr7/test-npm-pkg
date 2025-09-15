#!/usr/bin/env python3
"""
Random Python code demonstrating various programming concepts
"""

import random
import math
from datetime import datetime
from typing import List, Dict, Optional

class RandomDataGenerator:
    """A class that generates random data and performs various operations."""
    
    def __init__(self, seed: Optional[int] = None):
        if seed:
            random.seed(seed)
        self.data: List[int] = []
        self.stats: Dict[str, float] = {}
    
    def generate_numbers(self, count: int = 10, min_val: int = 1, max_val: int = 100) -> List[int]:
        """Generate a list of random numbers."""
        self.data = [random.randint(min_val, max_val) for _ in range(count)]
        return self.data
    
    def calculate_statistics(self) -> Dict[str, float]:
        """Calculate basic statistics for the generated data."""
        if not self.data:
            return {}
        
        self.stats = {
            'mean': sum(self.data) / len(self.data),
            'min': min(self.data),
            'max': max(self.data),
            'std_dev': math.sqrt(sum((x - sum(self.data) / len(self.data)) ** 2 for x in self.data) / len(self.data))
        }
        return self.stats
    
    def fibonacci_sequence(self, n: int) -> List[int]:
        """Generate Fibonacci sequence up to n terms."""
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
    
    def is_prime(self, num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    def find_primes_in_data(self) -> List[int]:
        """Find all prime numbers in the generated data."""
        return [num for num in self.data if self.is_prime(num)]

def random_word_generator(length: int = 8) -> str:
    """Generate a random word of specified length."""
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    word = ''
    
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(consonants)
        else:
            word += random.choice(vowels)
    
    return word.capitalize()

def matrix_operations():
    """Demonstrate some matrix operations."""
    # Create random 3x3 matrix
    matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
    
    print("Random 3x3 Matrix:")
    for row in matrix:
        print(row)
    
    # Calculate determinant (for 3x3 matrix)
    def determinant_3x3(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
                m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
                m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    
    det = determinant_3x3(matrix)
    print(f"Determinant: {det}")
    
    # Transpose matrix
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("Transpose:")
    for row in transpose:
        print(row)

def recursive_factorial(n: int) -> int:
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)

def binary_search(arr: List[int], target: int) -> int:
    """Perform binary search on a sorted array."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def main():
    """Main function to demonstrate the random code."""
    print("=== Random Python Code Demo ===")
    print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Initialize random data generator
    generator = RandomDataGenerator(seed=42)
    
    # Generate and display random numbers
    numbers = generator.generate_numbers(15, 1, 50)
    print(f"Generated numbers: {numbers}")
    
    # Calculate statistics
    stats = generator.calculate_statistics()
    print(f"Statistics: {stats}")
    
    # Find primes
    primes = generator.find_primes_in_data()
    print(f"Prime numbers in data: {primes}")
    
    # Generate Fibonacci sequence
    fib = generator.fibonacci_sequence(10)
    print(f"Fibonacci sequence (10 terms): {fib}")
    
    # Generate random words
    words = [random_word_generator(random.randint(5, 10)) for _ in range(5)]
    print(f"Random words: {words}")
    
    # Demonstrate factorial
    fact_num = random.randint(5, 10)
    factorial = recursive_factorial(fact_num)
    print(f"Factorial of {fact_num}: {factorial}")
    
    # Demonstrate binary search
    sorted_data = sorted(numbers)
    target = random.choice(sorted_data)
    index = binary_search(sorted_data, target)
    print(f"Binary search for {target} in {sorted_data}: found at index {index}")
    
    print("\n=== Matrix Operations ===")
    matrix_operations()
    
    # Some fun with list comprehensions and lambda functions
    print("\n=== Fun with Python Features ===")
    squares = [x**2 for x in range(1, 11)]
    print(f"Squares 1-10: {squares}")
    
    even_squares = list(filter(lambda x: x % 2 == 0, squares))
    print(f"Even squares: {even_squares}")
    
    # Dictionary comprehension
    word_lengths = {word: len(word) for word in words}
    print(f"Word lengths: {word_lengths}")

if __name__ == "__main__":
    main()
