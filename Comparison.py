def comparison_operations(a, b):
    # Equal to
    equal = a == b
    print(f"{a} == {b} -> {equal}")
    
    # Not equal to
    not_equal = a != b
    print(f"{a} != {b} -> {not_equal}")
    
    # Greater than
    greater_than = a > b
    print(f"{a} > {b} -> {greater_than}")
    
    # Less than
    less_than = a < b
    print(f"{a} < {b} -> {less_than}")
    
    # Greater than or equal to
    greater_than_equal = a >= b
    print(f"{a} >= {b} -> {greater_than_equal}")
    
    # Less than or equal to
    less_than_equal = a <= b
    print(f"{a} <= {b} -> {less_than_equal}")
a = 10
b = 5
comparison_operations(a, b)