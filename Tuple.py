# A Python program to demonstrate the use of tuples and tuple functions

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print("Original tuple:", my_tuple)
print("Element at index 2:", my_tuple[2])

# Tuple slicing
print("Slice from index 1 to 3:", my_tuple[1:4])

# Count - Counting the number of occurrences of a value
count_of_2 = my_tuple.count(2)
print("Count of 2:", count_of_2)

# Index - Finding the index of the first occurrence of a value
index_of_4 = my_tuple.index(4)
print("Index of 4:", index_of_4)

# Length - Getting the number of items in the tuple
length_of_tuple = len(my_tuple)
print("Length of tuple:", length_of_tuple)

# Concatenation - Joining two tuples
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print("After concatenation:", concatenated_tuple)

# Repetition - Repeating the tuple multiple times
repeated_tuple = my_tuple * 2
print("After repetition:", repeated_tuple)

# Unpacking - Assigning elements of a tuple to variables
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)

# Converting a tuple to a list and modifying it
tuple_to_list = list(my_tuple)
tuple_to_list.append(6)  # Modify the list
print("Modified list:", tuple_to_list)

# Converting the list back to a tuple
modified_tuple = tuple(tuple_to_list)
print("Modified tuple:", modified_tuple)
