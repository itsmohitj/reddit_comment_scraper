
import praw
import matplotlib.pyplot as plt

reddit = praw.Reddit(client_id='client_id', client_secret='Client_Secret', user_agent='comment_scraper', username='Reddit_Username', password='Reddit_Password')

subreddit_name = "learnpython"
subreddit = reddit.subreddit(subreddit_name)

