import re

# Sample text
text = """
Hello, my email is example@example.com.
You can also contact me at support@test.org.
My website is https://www.example.com.
I have a cat named Mini and a dog named Gabbar.
"""

# Function to demonstrate regex functions
def regex_functions_demo(text):
    # 1. re.search(): Search for the first match of the pattern
    email_search = re.search(r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b', text)
    if email_search:
        print("First email found:", email_search.group())
    else:
        print("No email found.")

    # 2. re.match(): Check if the string starts with the pattern
    match_result = re.match(r'Hello', text)
    if match_result:
        print("Text starts with 'Hello'.")
    else:
        print("Text does not start with 'Hello'.")

    # 3. re.findall(): Find all occurrences of the pattern
    urls = re.findall(r'https?://[^\s]+', text)
    print("URLs found:", urls)

    # 4. re.sub(): Substitute occurrences of the pattern with a replacement
    replaced_text = re.sub(r'\b(cat|dog)\b', 'animal', text)
    print("Text after substitution:")
    print(replaced_text)

    # 5. re.split(): Split the string by occurrences of the pattern
    split_text = re.split(r'\s+', text)
    print("Words in the text:")
    print(split_text)

# Run the demo function
regex_functions_demo(text)
