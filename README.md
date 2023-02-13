# Welcome to my Sentiment Analyser App 👋

(You can access it here --> https://priyanka7219-sentiment-analyzer-hello-9splmb.streamlit.app/)

This app scrapes the top news headlines from the U.S. News website and performs sentiment analysis on them (you can access here --> https://www.usnews.com/)

## Following are the python libraries used:

1. Data Manipulation: pandas, numpy
2. Visualisation: matplotlib, seaborn
3. Natural Language Processing: nltk
4. Scraping: BeautifulSoup4, requests

## What can this app do?

1. There is a very simple scrapper that is running in the background that pulls the headlines from the website (you can even download a csv file)
2. Then we can see a distribution of what the major sentiments behind the scraped headlines are (positive, negative and neutral). This is to check the hypothesis of whether news websites primarily report negative news or not!
3. Finally, you can see the frequency distribution of the words in the headlines are.


## Learnings ##

***This was the first time that I tried creating an app which is why it took a while to debug issues.***

**Listing them down here along with what I did to resolve them**


1. The majority of my time that I wasted was in navigating the python virtual environment which is quite important to run streamlit apps. The requirements.txt might just be the most important file you ever add more than even your actual project:P

**Resolution:** Instead of manually going and adding all the libraries in a text file what you can do is install the "pipreqs" package. But make sure you actually add it in the venv that you initialised. If you have to overwrite this file then use pipreqs --force.

2. Theres another file called Pipfile that is important. I have to go back to check how it was initally created but if the requirements.txt and Pipfile are not in tandem you are at risk of losing your mind.

**Resolution:** There might be a better way but to save time just manually change it by opening in Notepad. It should have the same packages as requirements.txt. Once your Pipfile is alright, all's well in the world again. You can then run pipenv install --skip-lock or pipenv lock. This will create yet another file called Pipfile.lock

3. Do not run your app outside of the venv

**Resolution:** Make sure you use the pipenv shell command before you start fiddling with your app

4. Make sure you install the packages from requirements.txt in the venv

**Resolution:** Use the command pipenv install -r requirements.txt


## Github Basics

Even though I have used Github in the past it was super frustrating to work with it now since I had forgotten my basics

1. Getting your SSH key and storing it on Github --> https://www.youtube.com/watch?v=xwlQimbwJJE

2. Commands that should be at the top of your mind while using Git bash to push your code (P.S. In the gap of a year or two that I had not used Github they ended up changing the term from master to main :P)

```
   git add .
   git commit -m "commit message"
   git push origin main
   git pull
   git status
```


3. It is always useful to just go to the local folder and open git bash from there instead of trying to go to the path location from the command line
  

## Improvements (post feedback from peers)

** This is still a work-in-progress project and will keep improving as I learn **
