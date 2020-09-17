
import praw
import matplotlib.pyplot as plt

reddit = praw.Reddit(client_id='client_id', client_secret='Client_Secret', user_agent='comment_scraper', username='Reddit_Username', password='Reddit_Password')

subreddit_name = "learnpython"
subreddit = reddit.subreddit(subreddit_name)
top_subbreddit = subreddit.top()
count = 0
max = 10000
print('success')
words = []
wordCount = {}
commonWords = {'that','this','and','of','the','for','I','it','has','in',
'you','to','was','but','have','they','a','is','','be','on','are','an','or',
'at','as','do','if','your','not','can','my','their','them','they','with',
'at','about','would','like','there','You','from','get','just','more','so',
'me','more','out','up','some','will','how','one','what',"don't",'should',
'could','did','no','know','were','did',"it's",'This','he','The','we'}
