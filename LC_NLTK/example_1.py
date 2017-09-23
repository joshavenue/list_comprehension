import nltk
from nltk.book import *

x = [w for w in text3 if len(w) == 5]

print(len(x))

## For all the words in text3, shows only text that has 5 characters
## Then print the numbers of words that has only 5 characters.
