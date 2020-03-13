from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk import FreqDist
import matplotlib.pyplot as plt
import nltk
import re
import math

def fileTokens():

	fileObject = open("pridebook.txt", "r")

	book = fileObject.read();
	print("Book Size = ", len(book))

	#remove punctuation except for apostrophes
	book = re.sub(r"[^\w\d'\s]+",'',book) 

	#tokenize book words
	bookTokens = word_tokenize(book)

	#frequency of tokens
	freq = nltk.FreqDist(bookTokens)

	#number of tokens
	rank = len(freq)

	#list with most common tokens first
	freq = freq.most_common()
	#print(freq)

	sumConst = []
	for i in range(1, rank + 1):
		sumConst.append(freq[i - 1][1] * i)

	#create and show graph
	plotX = []
	plotY = []
	for i in range(0, 50):
		plotY.append(sumConst[i])
		plotX.append(i + 1)

	plt.plot(plotX, plotY)
	plt.show()

	#average constant calculation
	averageSum = 0;
	for i in range(0, 50):
		averageSum += sumConst[i]

	average = averageSum / 50

	print("Constant value is: ", average)

	print("Number of tokens = ", len(bookTokens))

	freqFifty = nltk.FreqDist(bookTokens)
	freqFifty = freqFifty.most_common(50)
	print("Most 50 common: ", freqFifty)

	#create and show graph
	plotX = []
	plotY = []
	for i in range(0, 50):
		plotY.append(freqFifty[i][1])
		plotX.append(i + 1)

	plt.plot(plotX, plotY)
	plt.show()

	

fileTokens()