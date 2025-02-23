from bs4 import BeautifulSoup
import pandas as pd
import requests
from nltk.corpus import stopwords
from operator import itemgetter
from textblob import TextBlob


url = 'https://www.gutenberg.org/cache/epub/1232/pg1232-images.html'
html_text = (requests.get(url).text)
soup = BeautifulSoup(html_text, 'html.parser')

url = 'https://www.gutenberg.org/cache/epub/41537/pg41537-images.htm'
html_text = (requests.get(url).text)
soup2 = BeautifulSoup(html_text, 'html.parser')

princeBlob= TextBlob(soup)
frankenBlob = TextBlob(soup2)

stop_words = stopwords.words('english')

items = princeBlob.word_counts.items()
items = [item for item in items if item[0] not in stop_words]
sorted_items = sorted(items, key=itemgetter(1), reverse=True)
top20 = sorted_items[1:21]

df = pd.DataFrame(top20, columns=['word', 'count'])

print(df)