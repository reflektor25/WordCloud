import re
import wordcloud
import tweepy
import string
'''KEYS'''
consumer_key = 'Q6PkFN6qv2N7gAKQ2oYFjVpIZ'
consumer_secret = 'VisvZFHYGmR3D4LAmWjVVkV3N82zY9U7wZJLTW6hBVb4wmbwUH'
access_token = '1107934645675589632-iVnnyAlBPCAmfsGrLmDunsTfk4z97B'
access_secret = '4ML6p3MTF3bEx1zomu1IHkhFCgr4e7QXDHsO2njlQ4fJR'
'''END KEYS'''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

i=1
tekst=''
for tweet in tweepy.Cursor(api.search,q='#slovenia -filter:retweets',result_type='latest',include_entities=True,tweet_mode='extended').items(5):
    besedilo=tweet.full_text
    #Brez Retweet teksta
    if besedilo[:2]=='RT':
        ind=besedilo.find(':')+1
        besedilo=besedilo[ind:]

    #Brez linkov
    temp=besedilo.split()
    samo_besede=[]
    for el in temp:
        if not el[:4].lower()=='http':
            samo_besede.append(el)
    besedilo=' '.join(samo_besede)

    a = string.punctuation.replace('@', '')
    tekst+=re.sub(r'[^\w\s?]'.format(a), '',besedilo)+'\n'
    i+=1
print(tekst)
