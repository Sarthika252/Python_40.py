def identity_operations(x, y):
    # Identity: is
    is_operation = x is y
    print(f"{x} is {y} -> {is_operation}")

    # Identity: is not
    is_not_operation = x is not y
    print(f"{x} is not {y} -> {is_not_operation}")


x = [1, 2, 3]
y = [1, 2, 3]
z = x

identity_operations(x, y)
identity_operations(x, z)