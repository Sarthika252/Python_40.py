import re

# Sample text
text = """
Hello, my email is example@example.com.
You can also contact me at support@test.org.
Don't forget to visit my website at https://www.example.com.
"""

# Define patterns using metacharacters
email_pattern = r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b'  # Matches email addresses
url_pattern = r'https?://[^\s]+'                # Matches URLs
word_pattern = r'\b\w{5}\b'                     # Matches words with exactly 5 characters

# Find all matches for each pattern
emails = re.findall(email_pattern, text)
urls = re.findall(url_pattern, text)
five_letter_words = re.findall(word_pattern, text)

# Print the results
print("Email Addresses Found:")
print(emails)

print("\nURLs Found:")
print(urls)

print("\nFive Letter Words Found:")
print(five_letter_words)
