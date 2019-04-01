import tweepy

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
for tweet in tweepy.Cursor(api.search,q='#slovenia',result_type='recent',include_entities=True).items(15):
    print("tweet številka",i)
    print(tweet.text)
    i+=1
