# Function to calculate factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(2, num + 1):
            fact *= i
        return fact

n = int(input("Enter the value of n: "))

# Initialize the sum
sum_sequence = 0


for i in range(n + 1):
    sum_sequence += 1 / factorial(i)


print("The sum of the series is:", sum_sequence)