# Define a sample string
sample_string = "Hello, Python Programmers! Welcome to the world of Python."
print("The string is :",sample_string)
# 1. String Length
length = len(sample_string)
print("Length of the string:", length)

# 2. String Slicing
substring = sample_string[7:13]
print("Sliced substring:", substring)

# 3. String Uppercase
uppercase_string = sample_string.upper()
print("Uppercase string:", uppercase_string)

# 4. String Lowercase
lowercase_string = sample_string.lower()
print("Lowercase string:", lowercase_string)

# 5. String Capitalization
capitalized_string = sample_string.capitalize()
print("Capitalized string:", capitalized_string)

# 6. String Title Case
title_string = sample_string.title()
print("Title case string:", title_string)

# 7. String Replace
replaced_string = sample_string.replace("Python", "Java")
print("String after replacement:", replaced_string)

# 8. String Split
split_string = sample_string.split(" ")
print("Split string into list:", split_string)

# 9. String Join
joined_string = "-".join(split_string)
print("Joined string with hyphen:", joined_string)

# 10. String Find
index = sample_string.find("Python")
print("Index of 'Python':", index)

# 11. String Count
count = sample_string.count("Python")
print("Count of 'Python':", count)

# 12. String Startswith
starts_with_hello = sample_string.startswith("Hello")
print("String starts with 'Hello':", starts_with_hello)

# 13. String Endswith
ends_with_python = sample_string.endswith("Python.")
print("String ends with 'Python.':", ends_with_python)

# 14. String Strip (removes leading/trailing whitespace)
strip_string = "   Hello, World!   ".strip()
print("String after strip:", strip_string)

# 15. String Format
formatted_string = "Hello, {}! Welcome to the {}.".format("Alice", "world of Python")
print("Formatted string:", formatted_string)

# 16. String Concatenation
concatenated_string = "Hello" + ", " + "World!"
print("Concatenated string:", concatenated_string)

# 17. String Isdigit
digit_check = "12345".isdigit()
print("String is digit:", digit_check)

# 18. String Isalpha
alpha_check = "Python".isalpha()
print("String is alphabetic:", alpha_check)

# 19. String Isalnum
alnum_check = "Python123".isalnum()
print("String is alphanumeric:", alnum_check)

# 20. String Islower
islower_check = "python".islower()
print("String is lowercase:", islower_check)

# 21. String Isupper
isupper_check = "PYTHON".isupper()
print("String is uppercase:", isupper_check)

# 22. String Swapcase
swapcase_string = sample_string.swapcase()
print("Swapcase string:", swapcase_string)

# 23. String Zfill (Pads string with zeros)
zfilled_string = "42".zfill(5)
print("Zero filled string:", zfilled_string)

# 24. String Center (Centers string within specified width)
centered_string = "Python".center(20, '-')
print("Centered string:", centered_string)

# 25. String Rjust (Right justifies string within specified width)
rjust_string = "Python".rjust(20, '-')
print("Right justified string:", rjust_string)

# 26. String Ljust (Left justifies string within specified width)
ljust_string = "Python".ljust(20, '-')
print("Left justified string:", ljust_string)