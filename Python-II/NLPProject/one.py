from textblob import TextBlob
from bs4 import BeautifulSoup
import requests
import random

url = 'https://www.gutenberg.org/cache/epub/132/pg132-images.html'
html_text = (requests.get(url).text)
soup = BeautifulSoup(html_text, 'html.parser')

paragraphs = soup.find_all('p')

blob = TextBlob(paragraphs)
print(blob.sentences)

#two.py
print(blob.tags)


#three.py
print(blob.noun_phrases)


#print(paragraph)
#print(random.choice(paragraphs))
