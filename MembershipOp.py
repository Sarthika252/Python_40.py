def membership_operations(element, sequence):
    # Membership: in
    in_operation = element in sequence
    print(f"{element} in {sequence} -> {in_operation}")

    # Membership: not in
    not_in_operation = element not in sequence
    print(f"{element} not in {sequence} -> {not_in_operation}")
sequence = [1, 2, 3, 4, 5]
element_present = 3
element_absent = 7

membership_operations(element_present, sequence)
membership_operations(element_absent, sequence)