# Creating a dictionary with some initial values
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

# Accessing a value using a key
print("Bob's grade:", student_grades["Bob"])

# Adding a new key-value pair to the dictionary
student_grades["Eve"] = 88
print("Updated dictionary after adding Eve:", student_grades)

# Updating the value of an existing key
student_grades["Alice"] = 95
print("Updated dictionary after modifying Alice's grade:", student_grades)

# Removing a key-value pair from the dictionary
removed_grade = student_grades.pop("Charlie")
print(f"Removed Charlie's grade ({removed_grade}). Updated dictionary:", student_grades)

# Checking if a key exists in the dictionary
if "David" in student_grades:
    print("David is in the dictionary.")

# Getting the number of key-value pairs in the dictionary
print("Number of students:", len(student_grades))

# Iterating over the dictionary
print("All students and their grades:")
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

# Getting all the keys
print("List of all students:", list(student_grades.keys()))

# Getting all the values
print("List of all grades:", list(student_grades.values()))

# Clearing the dictionary
student_grades.clear()
print("Dictionary after clearing all elements:", student_grades)