import praw
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

reddit = praw.Reddit(client_id='client_id', client_secret='Client_Secret', user_agent='comment_scraper', username='Reddit_Username', password='Reddit_Password')

subreddit_name = input("Enter the name of the subreddit")
subreddit = reddit.subreddit(subreddit_name)
top_subbreddit = subreddit.top()
count = 0
max = 1000
words = []
wordCount = {}
commonWords = {'these','they','that','this','and','of','the','for','I','it','has','in',
                'you','to','was','but','have','they','a','is','','be','on','are','an','or',
                'at','as','do','if','your','not','can','my','their','them','they','with',
                'at','about','would','like','there','You','from','get','just','more','so',
                'me','more','out','up','some','will','how','one','what',"don't",'should',
                'could','did','no','know','were','did',"it's",'This','he','The','we',
                'all','when','had','see','his','him','who','by','her','she','our','thing','-',
                'now','what','going','been','we',"I'm",'than','any','because','We','even',
                'said','only','want','other','into','He','what','i','That','thought',
                'think',"that's",'Is','much'}

for submission in subreddit.top(limit=50):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        count += 1
        if(count == max):
            break
        word = ""
        for letter in top_level_comment.body:
            if(letter == ' '):
                if(word and not word[-1].isalnum()):
                    word = word[:-1]
                if not word in commonWords:
                    words.append(word)
                word = ""
            else:
                word += letter
    if(count == max):
            break

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

sortedList = sorted(wordCount, key = wordCount.get, reverse = True)

keyWords = []
keyCount = []
amount = 0

for entry in sortedList:
    keyWords.append(entry)
    keyCount.append(wordCount[entry])
    amount += 1
    if (amount == 10):
        break

labels = keyWords
sizes = keyCount

#Uncomment to plot using MatPlotLib
#plt.title('Top comments for: r/' + subreddit_name)
#plt.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
#plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#plt.show()


sns.set_palette('magma')
series = pd.Series(sizes, index = labels, name = "Plot")
series.plot.pie(subplots=True, autopct="%.2f", figsize=(10,6))
plt.show()
