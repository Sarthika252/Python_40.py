#Word tokenization and sentence tokenization
#import nltk
#nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize ,sent_tokenize
text="Hello,World! How are you?"
words=word_tokenize(text)
print(words)
sentences=sent_tokenize(text)
print(sentences) 