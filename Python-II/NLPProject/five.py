from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from bs4 import BeautifulSoup
import requests
import random

url = 'https://www.gutenberg.org/cache/epub/2000/pg2000-images.html' #don q
html_text = (requests.get(url).text)
soup = BeautifulSoup(html_text, 'html.parser')

url2 = 'https://www.gutenberg.org/cache/epub/997/pg997-images.html' #dante
html_text2 = (requests.get(url).text)
soup2 = BeautifulSoup(html_text, 'html.parser')

blob = soup
blob2= soup2

print(blob.translate(to='en'))
print(blob2.translate(to='en'))
