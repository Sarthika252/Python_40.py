def display_data_types():
    # Numeric types
    int_type = 42
    float_type = 3.14
    complex_type = 3 + 4j

    # Sequence types
    string_type = "Hello, World!"
    list_type = [1, 2, 3, 4, 5]
    tuple_type = (1, 2, 3)

    # Set types
    set_type = {1, 2, 3}
    frozenset_type = frozenset({1, 2, 3})

    # Mapping type
    dict_type = {'one': 1, 'two': 2}

    # Boolean type
    bool_type = True

    # Binary types
    bytes_type = b'hello'
    bytearray_type = bytearray(b'hello')
    memoryview_type = memoryview(bytes(5))

    # None type
    none_type = None

    # Displaying all the data types
    print(f"Integer: {int_type} (Type: {type(int_type)})")
    print(f"Float: {float_type} (Type: {type(float_type)})")
    print(f"Complex: {complex_type} (Type: {type(complex_type)})\n")

    print(f"String: {string_type} (Type: {type(string_type)})")
    print(f"List: {list_type} (Type: {type(list_type)})")
    print(f"Tuple: {tuple_type} (Type: {type(tuple_type)})\n")

    print(f"Set: {set_type} (Type: {type(set_type)})")
    print(f"Frozenset: {frozenset_type} (Type: {type(frozenset_type)})\n")

    print(f"Dictionary: {dict_type} (Type: {type(dict_type)})\n")

    print(f"Boolean: {bool_type} (Type: {type(bool_type)})\n")

    print(f"Bytes: {bytes_type} (Type: {type(bytes_type)})")
    print(f"Bytearray: {bytearray_type} (Type: {type(bytearray_type)})")
    print(f"Memoryview: {memoryview_type} (Type: {type(memoryview_type)})\n")

    print(f"None: {none_type} (Type: {type(none_type)})")

# Calling the function to display all data types
display_data_types()

