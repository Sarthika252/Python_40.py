# A Python program to demonstrate the use of lists and list functions

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Append - Adding an item to the end of the list
my_list.append(6)
print("After append:", my_list)

# Insert - Adding an item at a specific position
my_list.insert(2, 10)  # Insert 10 at index 2
print("After insert:", my_list)

# Remove - Removing the first occurrence of a value
my_list.remove(4)
print("After remove:", my_list)

# Pop - Removing an item at a specific position (default is the last item)
popped_item = my_list.pop(3)  # Remove the item at index 3
print("Popped item:", popped_item)
print("After pop:", my_list)

# Extend - Adding multiple items to the end of the list
my_list.extend([7, 8, 9])
print("After extend:", my_list)

# Sort - Sorting the list in ascending order
my_list.sort()
print("After sort:", my_list)

# Reverse - Reversing the order of the list
my_list.reverse()
print("After reverse:", my_list)

# Count - Counting the number of occurrences of a value
count_of_sevens = my_list.count(7)
print("Count of 7:", count_of_sevens)

# Index - Finding the index of the first occurrence of a value
index_of_eight = my_list.index(8)
print("Index of 8:", index_of_eight)

# Length - Getting the number of items in the list
length_of_list = len(my_list)
print("Length of list:", length_of_list)

# Copy - Creating a copy of the list
copied_list = my_list.copy()
print("Copied list:", copied_list)

# Clear - Removing all items from the list
my_list.clear()
print("After clear:", my_list)
