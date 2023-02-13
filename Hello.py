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

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to my Sentiment Analyser App 👋")

st.sidebar.success("Select a cool thing you want to see!")

st.markdown(
    """
     This app scrapes the top news headlines from the U.S. News website and performs sentiment analysis on them (you can access here --> https://www.usnews.com/)
    
    **Following are the python libraries used:**
       - Data Manipulation: pandas, numpy
       - Visualisation: matplotlib, seaborn
       - NLP: nltk
       
    **👈 Select a cool thing you want to see from the sidebar** to see what this app can do!
    ### You may wonder what the objective of this app is, read on to get to know more :P 
    - There is a very simple scrapper that is running in the background that pulls the headlines from the website (you can even download a csv file)
    - Then we can see a distribution of what the major sentiments behind the scraped headlines are (positive, negative and neutral). This is to check the hypothesis of whether news websites primarily report negative news or not! 
    - Finally, you can see the frequency distribution of the words in the headlines are.
    
    ** This is still a work-in-progress project and will keep improving as I learn **
    
"""
)