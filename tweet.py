import tweepy       #from api
import nltk         #import vader_lexicon for checking the polarities of a sentence.

c_k =''             #consumer _key after registration in twitter api
c_s = ''            #consumer_secret after registration in twitter api

a_k =  ''           #access_token after registration in twitter api
a_s = ''            #access_token_secret after registration in twitter api

auth  = tweepy.OAuthHandler(c_k,c_s)   #authentication
auth.set_access_token(a_k,a_s)

api = tweepy.API(auth)

public_tweets = api.search('Virat')    #search for the tweetbased on the context


from nltk.sentiment.vader import SentimentIntensityAnalyzer     #for analyzing a sentence in tweet it returns a dictionary like this

# {'pos':some_value  , 'neg': some_value  ,  'neu': 'some_value'  ,  'compound': some_value}

#pos = positive
#neg = negative
#neu = neutral
#compound = cummulative_score

sid = SentimentIntensityAnalyzer()

for i in public_tweets :            #iterate through each tweet and analyzed it either it is +,- or +- 
    a=i.text
    print(a,'\n')
    analyse = sid.polarity_scores(a)
    print(analyse)
