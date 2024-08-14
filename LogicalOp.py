def logical_operations(a, b):
    # Logical AND
    and_operation = a and b
    print(f"{a} and {b} -> {and_operation}")
    
    # Logical OR
    or_operation = a or b
    print(f"{a} or {b} -> {or_operation}")
    
    # Logical NOT
    not_a = not a
    print(f"not {a} -> {not_a}")
    
    not_b = not b
    print(f"not {b} -> {not_b}")

# Example usage
a = True
b = False
logical_operations(a, b)
