# Get the user's age
age = int(input("Enter your age: "))

# Determine the life stage based on age
if age < 0:
    print("Invalid age!")
elif age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
