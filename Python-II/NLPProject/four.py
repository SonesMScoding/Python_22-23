from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from bs4 import BeautifulSoup
import requests
import random

url = 'https://www.gutenberg.org/cache/epub/26/pg26-images.html'
html_text = (requests.get(url).text)
soup = BeautifulSoup(html_text, 'html.parser')


paragraphs = soup.find_all('p')
blob = TextBlob(paragraphs, analyzer=NaiveBayesAnalyzer())


print(blob.sentiment)
