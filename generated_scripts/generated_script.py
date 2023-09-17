
import math

def calculate_square_root(number1, number2):
    square_root1 = math.sqrt(number1)
    square_root2 = math.sqrt(number2)
    return square_root1, square_root2

# Example usage
num1 = 16
num2 = 25
result1, result2 = calculate_square_root(num1, num2)
print("Square root of", num1, "is", result1)
print("Square root of", num2, "is", result2)
