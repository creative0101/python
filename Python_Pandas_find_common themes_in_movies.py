import pandas as pd

file_name = "https://raw.githubusercontent.com/practiceprobs/datasets/main/netflix-titles/netflix-titles.csv"
df = pd.read_csv(file_name)
df.head()

# TASK 1: Find the 10 most common words in the descriptions.

df['description'].str.split(expand=True).stack().value_counts().head(10)

# too many irrelevant words

# get the nltk library

import nltk
nltk.download('stopwords')

# exclude stopwords and words with less than two letters

from nltk.corpus import stopwords

stop = stopwords.words('english')

description2 = df['description'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop) and len(word)>2]))

description2.str.split(expand=True).stack().value_counts().head(10)

# TASK 2: Create a wordcloud for the 30 most common words.

# import wordcloud

from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt

# define the wordcloud

text = ' '.join(word for word in description2)
wordcloud = WordCloud(background_color='white').generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

"""RESULTS: Seemingly, most words revolve around social relationships, i.e. "friend", "family", and so on."""
