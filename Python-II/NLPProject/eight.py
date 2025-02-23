from textblob import TextBlob
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import imageio
from wordcloud import WordCloud

mask_image = imageio.imread('mask_heart.png')
wordcloud = WordCloud(colormap='prism', mask=mask_image,background_color='white')

url2 = 'https://www.gutenberg.org/cache/epub/997/pg997-images.html' #dante es
html_text2 = (requests.get(url).text)
soup = BeautifulSoup(html_text, 'html.parser')

blob = TextBlob(soup)
spBlob = (blob.translate(to='en'))


url = 'https://www.gutenberg.org/cache/epub/996/pg996-images.html'
html_text = (requests.get(url).text)
soup1 = BeautifulSoup(html_text, 'html.parser')

enBlob = TextBlob(soup1)

axes = df.plot.bar(x='word', y='count', legend=False)
plt.gcf().tight_layout()

wordcloud = wordcloud.generate(enBlob)