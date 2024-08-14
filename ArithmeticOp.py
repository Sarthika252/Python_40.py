def arithmetic_operations(a, b):
    # Addition
    addition = a + b
    print(f"{a} + {b} = {addition}")
    
    # Subtraction
    subtraction = a - b
    print(f"{a} - {b} = {subtraction}")
    
    # Multiplication
    multiplication = a * b
    print(f"{a} * {b} = {multiplication}")
    
    # Division
    if b != 0:
        division = a / b
        print(f"{a} / {b} = {division}")
    else:
        print("Division by zero is not allowed.")
    
    # Modulus
    if b != 0:
        modulus = a % b
        print(f"{a} % {b} = {modulus}")
    else:
        print("Modulus by zero is not allowed.")
    
    # Exponentiation
    exponentiation = a ** b
    print(f"{a} ** {b} = {exponentiation}")
    
    # Floor Division
    if b != 0:
        floor_division = a // b
        print(f"{a} // {b} = {floor_division}")
    else:
        print("Floor division by zero is not allowed.")

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
arithmetic_operations(a, b)