from tkinter import *
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import tweepy
import string
import requests
import numpy as np
from PIL import Image

vnos = ""
def pritisk_gumb():
        global vnos
        vnos = vnosna.get()
        generiraj()
        okno.destroy()
    
def pritisk_enter(event): 
    pritisk_gumb()

def generiraj():
        i=1
        tekst=''
        oblika = np.array(Image.open(requests.get('https://publicdomainpictures.net/pictures/190000/velka/cloud-5.jpg', stream=True).raw))       
        if vnos[0] == "#":
                hashtag = vnos+' -filter:retweets'
        else:
                hashtag = '#'+vnos+' -filter:retweets'
        for tweet in tweepy.Cursor(api.search,q=hashtag,result_type=nacin,include_entities=True,tweet_mode='extended').items(100):
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
            tekst+=re.sub(r'[^\w\s?]'.format(a), '',besedilo)+';'
            i+=1

        stopwords = set([x[:-1] for x in list(open("stopwords.txt"))])
        wordcloud = WordCloud(width = 800, height = 800, collocations = False,
                              background_color = "white", stopwords = stopwords,
                              min_font_size = 15, max_font_size = 90, max_words = 1000,
                              random_state = 42, mask = oblika).generate(tekst)

        plt.figure(figsize = (10, 6), facecolor = None)
        plt.imshow(wordcloud, interpolation = "bilinear")
        plt.axis("off")
        plt.tight_layout(pad = 0)
        okno.destroy()
        plt.show()

'''KEYS'''
consumer_key = 'Q6PkFN6qv2N7gAKQ2oYFjVpIZ'
consumer_secret = 'VisvZFHYGmR3D4LAmWjVVkV3N82zY9U7wZJLTW6hBVb4wmbwUH'
access_token = '1107934645675589632-iVnnyAlBPCAmfsGrLmDunsTfk4z97B'
access_secret = '4ML6p3MTF3bEx1zomu1IHkhFCgr4e7QXDHsO2njlQ4fJR'
'''END KEYS'''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#tkinter zacetno okno
okno = Tk()
okno.title("WordCloud - PRO2")
okno.configure(bg = "black")
tekst = Label(okno, text="Twitter hashtag based Wordcloud", bg = "black", fg = "white", font = "Times 16")
tekst.grid(row = 1) #stlaci v navidezno tabelo
vnosna = Entry(okno, width = 40, bg = "white")
vnosna.grid(row = 2, column = 0)
izbira = {"recent", "top"}
nacin = StringVar(okno)
nacin.set("recent")
menu = OptionMenu(okno, nacin, *izbira)
menu.grid(row = 2, column = 1)
gumb = Button(okno, text = "Generiraj", width = 10, command = pritisk_gumb)
gumb.grid(row = 3, column = 0)
vnosna.bind('<Return>', pritisk_enter) # belezim pritisk tipke enter ko vnasam besedilo
okno.mainloop()


