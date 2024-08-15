import math

# Function to calculate the factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(2, num + 1):
            fact *= i
        return fact

# Get the value of x (in radians) and n (number of terms) from the user
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms (n): "))

# Initialize the sum for cosine series
cos_x = 0

# Calculate the cosine series
for i in range(n):
    term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    cos_x += term

# Print the result
print(f"The value of cos({x}) using {n} terms is: {cos_x}")