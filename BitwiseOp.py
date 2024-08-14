def bitwise_operations(a, b):
    # Bitwise AND
    and_operation = a & b
    print(f"{a} & {b} -> {and_operation}")

    # Bitwise OR
    or_operation = a | b
    print(f"{a} | {b} -> {or_operation}")

    # Bitwise XOR
    xor_operation = a ^ b
    print(f"{a} ^ {b} -> {xor_operation}")

    # Bitwise NOT
    not_a = ~a
    print(f"~{a} -> {not_a}")
    
    not_b = ~b
    print(f"~{b} -> {not_b}")

    # Bitwise Left Shift
    left_shift = a << 1
    print(f"{a} << 1 -> {left_shift}")

    # Bitwise Right Shift
    right_shift = a >> 1
    print(f"{a} >> 1 -> {right_shift}")
a = 10  # Binary: 1010
b = 4   # Binary: 0100
bitwise_operations(a, b)