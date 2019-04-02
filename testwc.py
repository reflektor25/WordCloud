from wordcloud import WordCloud
import matplotlib.pyplot as plt

stopwords = set([x[:-1] for x in list(open("stopwords.txt"))])

tekst = " ".join(list(open("test.txt"))) #temp

wordcloud = WordCloud(width = 800, height = 800,
                      background_color = "white", stopwords = stopwords,
                      min_font_size = 10).generate(tekst)


plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
