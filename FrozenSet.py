# Create frozensets
frozen_set1 = frozenset([1, 2, 3, 4, 5])
frozen_set2 = frozenset([4, 5, 6, 7, 8])

print("Frozen Set 1:", frozen_set1)
print("Frozen Set 2:", frozen_set2)

# Union of two frozensets
union_set = frozen_set1.union(frozen_set2)
print("\nUnion of Frozen Set 1 and Frozen Set 2:", union_set)

# Intersection of two frozensets
intersection_set = frozen_set1.intersection(frozen_set2)
print("Intersection of Frozen Set 1 and Frozen Set 2:", intersection_set)

# Difference between two frozensets
difference_set = frozen_set1.difference(frozen_set2)
print("Difference between Frozen Set 1 and Frozen Set 2:", difference_set)

# Symmetric difference between two frozensets
symmetric_difference_set = frozen_set1.symmetric_difference(frozen_set2)
print("Symmetric Difference between Frozen Set 1 and Frozen Set 2:", symmetric_difference_set)

# Check if one frozenset is a subset of another
is_subset = frozen_set1.issubset(frozen_set2)
print("\nIs Frozen Set 1 a subset of Frozen Set 2?:", is_subset)

# Check if one frozenset is a superset of another
is_superset = frozen_set1.issuperset(frozen_set2)
print("Is Frozen Set 1 a superset of Frozen Set 2?:", is_superset)

# Check if two frozensets are disjoint
are_disjoint = frozen_set1.isdisjoint(frozen_set2)
print("Are Frozen Set 1 and Frozen Set 2 disjoint?:", are_disjoint)

# Check if an element is in the frozenset
element = 3
is_in_set = element in frozen_set1
print(f"\nIs {element} in Frozen Set 1?:", is_in_set)

