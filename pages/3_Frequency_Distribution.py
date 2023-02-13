import streamlit as st
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import datetime 
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns
import time

nltk.download('vader_lexicon')
nltk.download('stopwords')

st.set_page_config(page_title="Frequency Distribution", page_icon="📈")

st.markdown("# Plotting Frequency Distribution of the words in Headlines from U.S. News")
st.sidebar.header("Plotting")
st.write(
    """This plots the frequency distribution of the words in top news headlines from the U.S. News website that we just scraped. You can choose how many words you want see on the charts. Enjoy!"""
)
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

#Web scraping
url_usnews = "https://www.usnews.com/"
html_tag_us = 'Box-w0dun1-0 ArmRestTopStories__Part-s0vo7p-1 erkdnc biVKSR'
html_tag_us1 = 'Box-w0dun1-0 ArmRestTopStories__Container-s0vo7p-0 dWWnRo jkIDND'
html_tag_us2 = 'BoxFeed__Container-jz7vbv-0 kCAxPf'
my_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

page_usnews = requests.get(url_usnews, headers = my_header)
soup_usnews = BeautifulSoup(page_usnews.text, 'html.parser')
content_usnews = soup_usnews.findAll('div', attrs = {'class': html_tag_us2})

top_stories = []

for i in range(len(content_usnews[0].findAll('a'))):
    if(content_usnews[0].findAll('a')[i].text not in ['World', 'Politics','Business', 
                                                       'Health', 'Science', 'Offbeat',  'U.S. News® ', 
                                                       'Entertainment', 'Sports' ]):
        top_stories.append(content_usnews[0].findAll('a')[i].text)
headlines = pd.DataFrame(top_stories)
headlines.rename(columns={0: "Headlines"}, inplace = True)

# # Sentiment Analysis

sia = SentimentIntensityAnalyzer()
results = []
for line in top_stories:
    
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)
    
df = pd.DataFrame.from_records(results)

df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.1, 'label'] = -1

df['scraped_date'] = date.today()

df = df.reindex(columns=['scraped_date','headline','neg', 'neu', 'pos', 'compound', 'label'])

df.rename(columns = {'neg':'negative', 'neu':'neutral', 'pos':'positive'}, inplace = True)
df.to_csv('usnews.csv', index=False)

#download csv functin
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')




# Frequency distribution

#Creating the tokenizer
tokenizer = nltk.tokenize.RegexpTokenizer(r'\s', gaps=True)

def process_text(top_stories):
    tokens = []
    for line in top_stories:
        toks = tokenizer.tokenize(line)
        toks = [t.lower() for t in toks if t.lower() not in stopwords]
        tokens.extend(toks)
    
    return tokens

stopwords = nltk.corpus.stopwords.words('english')

word_list = process_text(top_stories)

freq_dist = nltk.FreqDist(word_list)

freq_fig, ax = plt.subplots(figsize=(16,10))


st.markdown('<h3>Frequency Distribution of Words in Headlines</h3>', unsafe_allow_html=True)

word_count = st.slider('How many words do you wanna see on the chart?', 0, len(word_list), 1)
st.write("This is a distribution for ", word_count, " words")
freq_dist.plot(word_count)
st.pyplot(freq_fig)

status_text.text("100% Complete" )
progress_bar.progress(100)
progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
