# Get the value of n from the user
n = int(input("Enter the value of n:"))

# Initialize the starting value
value = 1

# Use a for loop to generate the sequence
for i in range(n):
    print(value, end=" ")
    value *= 2