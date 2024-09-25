from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#import nltk
#nltk.download('stopwords')

stop_words=set(stopwords.words("english")) 
text="This is a sample sentence,showing off the stop words filtration."
words=word_tokenize(text)
filtered_words=[word for word in words if word.lower() not in stop_words]
print(filtered_words)