import sys

args = sys.argv

print(args[0])
print(args[1])
print(args[2])

print("Congratulations! Python file excuted!")
print("Python file is going to examin Twitterððð")
print("ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼ã¼")




# !pip install tweepy==3.10.0

import tweepy as tw
import numpy as np
import pandas as pd
import datetime
import time
import janome
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from wordcloud import wordcloud
from janome.tokenizer import Tokenizer

API_Key = 'Xj2rGQY2rXIZNFyHvrLtMG9k3'
API_Sec= 'n6BLCvjdbVXy0yGyf9znyaiZYgEnpYbmbUtBK0hD5Qc85KkiMT'
Token= '795609199-URYcv9h24qwUWNYfKsA1m0Y66Do4PIivGdxHsDgu'
Token_Sec= 'yCwLzAQmHuTiNwLsQ7jrYggmAUtthxmOXImx69034LkBJ'


# Twitterãªãã¸ã§ã¯ãã®çæ
auth = tw.OAuthHandler(API_Key, API_Sec)
auth.set_access_token(Token, Token_Sec)
api = tw.API(auth)

count = 1000
search_word = 'ãã³ -filter:retweets' 

n =0 
data = []

for result in tweepy.Cursor(api.search, q=search_word).items(count):
  n += 1
  print('------{}-------'.format(n))
  print(result.text)
  data.append(result)


text=[]
for i in range(count):
  text.append(data[i].text)

text_merge = ''.join(text)

t = Tokenizer()
tokens = t.tokenize(text_merge)

wakati = []

for token in tokens:
  wakati.append(token.surface)


#ã¹ãã¼ã¹åºåãã®ä¸æã«ã¾ã¨ãã
wakati_merge = ' '.join(wakati)


import matplotlib.pyplot as plt
def draw_wordcloud(wordcloud, size):
    plt.figure(figsize = size)
    plt.imshow(wordcloud) 
    plt.axis("off")


#WordCloudã§è¡¨ç¤ºãã

# æ¥æ¬èªãã©ã³ãè¨­å®
fpath = '/content/gdrive/MyDrive/font/umeboshi_.ttf'

# éè¡¨ç¤ºã¯ã¼ã
stop_words = [u'ãã³', u'https', u'co', u'ã§ã', u'ãã', u'ãªã', u'ãã', u'ã¡ãã', u'ã®', u'ã¯', u'ã', u'ã', u'ã®', u'ã«', u'ã¾ã', u'ã§', u'ã¦', u't', u'ã', u'ã', u'ã¨', u'ã', u'ãª', u'ã', u'ã£ã¦', u'ã¾ã', u'ãã', u'ã ', u'ã', u'ã', u'ã']

# å³ã«ãã
wordcloud = WordCloud(font_path=fpath,
                      background_color="white",
                      stopwords=set(stop_words),
                      #collocations=False,
                      width=800,
                      height=600).generate(wakati_merge)
        
wordcloud.to_file("usr/mori-ma/sample.jpg")



# # APIã®å©ãæ¹
# import requests

# url = "http://zip.cgis.biz/xml/zip.php"
# payload = {"zn": "1310045"}

# r = requests.get(url, params=payload)

# r.text



# response = openai.Image.create(
#   prompt="a white siamese cat",
#   n=1,
#   size="1024x1024"
# )
# image_url = response['data'][0]['url']

