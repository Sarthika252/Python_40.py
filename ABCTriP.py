# Function to print the pattern
def print_pattern(n):
    for i in range(1, n + 1):
        # Generate the list of characters for the current row
        row = [chr(ord('A') + j) for j in range(i)]
        # Print the row, with characters separated by a space
        print(' '.join(row))


n = int(input("Enter the value of n: "))

# Print the pattern
print_pattern(n)