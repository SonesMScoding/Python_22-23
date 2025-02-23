from pathlib import Path
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob

url = 'https://www.gutenberg.org/cache/epub/132/pg132-images.html'
html_text = (requests.get(url).text)
soup = BeautifulSoup(html_text, 'html.parser')

url = 'https://www.gutenberg.org/cache/epub/996/pg996-images.html'
html_text = (requests.get(url).text)
soup1 = BeautifulSoup(html_text, 'html.parser')

url = 'https://www.gutenberg.org/cache/epub/41537/pg41537-images.htm'
html_text = (requests.get(url).text)
soup2 = BeautifulSoup(html_text, 'html.parser')

url = 'https://www.gutenberg.org/cache/epub/26/pg26-images.html'
html_text = (requests.get(url).text)
soup3 = BeautifulSoup(html_text, 'html.parser')

donBlob = TextBlob(soup)
danteBlob= TextBlob(soup1)
frankenBlob = TextBlob(soup2)
paraBlob= TextBlob(soup3)

print(donBlob.word_counts['knight'])
print(danteBlob.word_counts['hell'])
print(frankenBlob.word_counts['the'])
print(paraBlob.word_counts['war'])
