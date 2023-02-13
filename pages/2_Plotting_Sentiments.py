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

st.set_page_config(page_title="Plotting Sentiments", page_icon="📈")

st.markdown("# Plot Sentiments of Headlines from U.S. News")
st.sidebar.header("Plotting")
st.write(
    """This plots the sentiment distribution of the top news headlines from the U.S. News website that we just scraped.  Enjoy!"""
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


#Plot Bar chart pf the label

fig, ax = plt.subplots()

counts = df.label.value_counts(normalize=True) * 100

sns.barplot(x=counts.index, y=counts, ax=ax)

ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel("Percentage")

st.markdown('<h3>Distribution of Sentiments of the Headlines</h3>', unsafe_allow_html=True)
csv = convert_df(df)
st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
st.pyplot(fig)

status_text.text("100% Complete" )
progress_bar.progress(100)
progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")