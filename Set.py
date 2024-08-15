# A Python program to demonstrate the use of sets and set functions

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Display the sets
print("Set1:", set1)
print("Set2:", set2)

# Adding an item to the set
set1.add(9)
print("Set1 after adding 9:", set1)

# Removing an item from the set (raises KeyError if the item is not present)
set1.remove(2)
print("Set1 after removing 2:", set1)

# Discard - Removes an item if it is present, does nothing if it is not present
set1.discard(10)  # 10 is not in set1, so nothing happens
print("Set1 after discarding 10:", set1)

# Pop - Removes and returns an arbitrary element from the set (use carefully)
popped_item = set1.pop()
print("Popped item:", popped_item)
print("Set1 after pop:", set1)

# Clear - Removes all items from the set
set1.clear()
print("Set1 after clear:", set1)

# Set Operations

# Re-creating sets for operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union - Returns a set containing all elements from both sets
union_set = set1.union(set2)
print("Union of Set1 and Set2:", union_set)

# Intersection - Returns a set containing elements common to both sets
intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2:", intersection_set)

# Difference - Returns a set containing elements present in set1 but not in set2
difference_set = set1.difference(set2)
print("Difference of Set1 and Set2 (Set1 - Set2):", difference_set)

# Symmetric Difference - Returns a set containing elements in either set1 or set2 but not in both
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of Set1 and Set2:", symmetric_difference_set)

# Subset - Checks if set1 is a subset of set2
is_subset = set1.issubset(set2)
print("Is Set1 a subset of Set2?", is_subset)

# Superset - Checks if set1 is a superset of set2
is_superset = set1.issuperset(set2)
print("Is Set1 a superset of Set2?", is_superset)

# Disjoint - Checks if set1 and set2 have no elements in common
is_disjoint = set1.isdisjoint(set2)
print("Are Set1 and Set2 disjoint?", is_disjoint)

# Copy - Returns a shallow copy of the set
copied_set = set1.copy()
print("Copied Set1:", copied_set)
