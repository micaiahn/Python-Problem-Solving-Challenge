# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:11:27 2025

@author: Micaiah
"""

# Beginner Level

# 1. Check if a number is even or odd
def check_even_odd(number):
    # Check if the number is divisible by 2
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 2. Calculate factorial of a number
def factorial(n):
    # Initialize the result to 1 (factorial of 0 is 1)
    result = 1
    for i in range(1, n + 1):
        # Multiply result by the current number
        result *= i
    return result

# 3. Reverse a string without using built-in functions
def reverse_string(s):
    # Initialize an empty string to store the reversed string
    reversed_str = ""
    for char in s:
        # Prepend each character to the reversed string
        reversed_str = char + reversed_str
    return reversed_str

# 4. Check if a string is a palindrome
def is_palindrome(s):
    # Convert the string to lowercase for case-insensitive comparison
    s = s.lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# 5. Print Fibonacci sequence up to a given number of terms
def fibonacci_sequence(n):
    # Initialize the first two terms of the Fibonacci sequence
    fib = [0, 1]
    while len(fib) < n:
        # Append the sum of the last two terms to the sequence
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Intermediate Level

# 6. Find the largest and smallest elements in a list
def find_largest_smallest(lst):
    # Initialize smallest and largest with the first element
    smallest, largest = lst[0], lst[0]
    for num in lst:
        # Update smallest and largest if a smaller or larger value is found
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

# 7. Sort a list of numbers in ascending order without built-in functions
def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            # Swap elements if they are in the wrong order
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

# 8. Count occurrences of each word in a string
def word_count(s):
    # Split the string into words
    words = s.split()
    counts = {}
    for word in words:
        # Increment the count for each word
        counts[word] = counts.get(word, 0) + 1
    return counts

# 9. Find the GCD and LCM of two numbers
def gcd_lcm(a, b):
    # Helper function to calculate GCD using the Euclidean algorithm
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    gcd_val = gcd(a, b)
    # Calculate LCM using the relationship between GCD and LCM
    lcm_val = abs(a * b) // gcd_val
    return gcd_val, lcm_val

# 10. Remove duplicate elements from a list while maintaining order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        # Add item to the result if it's not already in the set
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# 11. Check if a number is prime
def is_prime(num):
    # A prime number must be greater than 1
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        # Check if num is divisible by any number up to its square root
        if num % i == 0:
            return False
    return True

# 12. Sum of all prime numbers within a given range
def sum_primes_in_range(start, end):
    # Sum all prime numbers in the specified range
    return sum(num for num in range(start, end + 1) if is_prime(num))

# 13. Generate a random password of a given length
def generate_password(length):
    import random
    import string

    # Combine letters and digits for password generation
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# 14. Find the second largest element in a list
def second_largest(lst):
    # Remove duplicates and sort the list
    unique = list(set(lst))
    unique.sort()
    # Return the second last element in the sorted list
    return unique[-2]

# 15. Convert a decimal number to binary, octal, and hexadecimal
def convert_number(num):
    # Convert the number to binary, octal, and hexadecimal formats
    return bin(num)[2:], oct(num)[2:], hex(num)[2:]

# Advanced Level

# 16. Solve a quadratic equation
def solve_quadratic(a, b, c):
    import cmath

    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    # Calculate the two roots using the quadratic formula
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    return root1, root2

# 17. Transpose a matrix
def transpose_matrix(matrix):
    # Use zip to transpose the rows and columns
    return [list(row) for row in zip(*matrix)]

# 18. Basic calculator
def calculator(a, b, operation):
    # Perform the requested operation
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    else:
        return "Invalid operation"

# 19. Merge two dictionaries and sum values of common keys
def merge_dicts(dict1, dict2):
    # Copy the first dictionary
    merged = dict1.copy()
    for key, value in dict2.items():
        # Sum values for keys that exist in both dictionaries
        merged[key] = merged.get(key, 0) + value
    return merged

# 20. Simulate a stack using lists
def stack_operations():
    stack = []

    # Function to push an element onto the stack
    def push(element):
        stack.append(element)

    # Function to pop an element from the stack
    def pop():
        return stack.pop() if stack else "Stack is empty"

    # Function to peek at the top element of the stack
    def peek():
        return stack[-1] if stack else "Stack is empty"

    return push, pop, peek
