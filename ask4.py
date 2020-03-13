from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk import FreqDist
import matplotlib.pyplot as plt
import nltk
import re


def fileTokens():

	lines = 0 
	terms = 0
	i = 0
	maybe = 0

	with open('user-ct-test-collection-02.txt','r') as file:
		for line in file:
			lines += 1
			i = 0
			maybe = 0
			for word in line.split():
				if(i==0):
					i+=1
					continue
				if(word.find("-") == -1):
					if(maybe == 1):
						if(word.find(":") == -1):
							maybe = 0
							terms += 2
						else:
							maybe = 0
							break
					else:
						terms +=1
				else:
					if(maybe == 1):
						maybe  = 0 
						terms += 1
						break
					else:
						maybe = 1


	mo1 = terms / lines
	print("Average terms of user-ct-test-collection-02.txt: ", mo1)


	lines = 0 
	terms = 0
	i = 0
	maybe = 0

	with open('user-ct-test-collection-03.txt','r') as file:
		for line in file:
			lines += 1
			i = 0
			maybe = 0
			for word in line.split():
				if(i==0):
					i+=1
					continue
				if(word.find("-") == -1):
					if(maybe == 1):
						if(word.find(":") == -1):
							maybe = 0
							terms += 2
						else:
							maybe = 0
							break
					else:
						terms +=1
				else:
					if(maybe == 1):
						maybe  = 0 
						terms += 1
						break
					else:
						maybe = 1


	mo2 = terms / lines
	print("Average terms of user-ct-test-collection-03.txt: ", mo2)



	lines = 0 
	terms = 0
	i = 0
	maybe = 0

	with open('user-ct-test-collection-04.txt','r') as file:
		for line in file:
			lines += 1
			i = 0
			maybe = 0
			for word in line.split():
				if(i==0):
					i+=1
					continue
				if(word.find("-") == -1):
					if(maybe == 1):
						if(word.find(":") == -1):
							maybe = 0
							terms += 2
						else:
							maybe = 0
							break
					else:
						terms +=1
				else:
					if(maybe == 1):
						maybe  = 0 
						terms += 1
						break
					else:
						maybe = 1



	mo3 = terms / lines
	print("Average terms of user-ct-test-collection-04.txt: ", mo3)



	lines = 0 
	terms = 0
	i = 0
	maybe = 0

	with open('user-ct-test-collection-05.txt','r') as file:
		for line in file:
			lines += 1
			i = 0
			maybe = 0
			for word in line.split():
				if(i==0):
					i+=1
					continue
				if(word.find("-") == -1):
					if(maybe == 1):
						if(word.find(":") == -1):
							maybe = 0
							terms += 2
						else:
							maybe = 0
							break
					else:
						terms +=1
				else:
					if(maybe == 1):
						maybe  = 0 
						terms += 1
						break
					else:
						maybe = 1



	mo4 = terms / lines
	print("Average terms of user-ct-test-collection-05.txt: ", mo4)


	              
	mo = (mo1 + mo2 + mo3 + mo4) / 4
	print("Average terms of all is: ", mo)    

fileTokens()