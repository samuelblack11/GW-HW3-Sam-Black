from collections import Counter
import string
import re

file = open('examplepar.txt','r')
message = file.read()
#print(message)

#Assess the passage for each of the following:

#Approximate word count
#re.split("(?<=[.!?]) +", paragraph)
words = message.split(' ', )
#print(words)
wordcount = len(words)

#Approximate sentence count
#sentences = message.split('.')
sentencecount=message.count('.')
#sentencecount = len(sentences)

#Approximate letter count (per word)
def isaletter(x):
	return x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#lettercount=len(message)
#lettersperword = ('{0:.3f}'.format(lettercount/wordcount))
lettercount=0
for char in message:
	if isaletter(char):
		lettercount+=1
lettersperword = ('{0:.3f}'.format(lettercount/wordcount))


#Average sentence length (in words)
sentencelength=('{0:.3f}'.format(wordcount/sentencecount))

print('\n'' ')
print('Paragraph Analysis: ''\n')
print(f'Approximate word count: {wordcount}')
print(f'Approximate sentence count: {sentencecount}')
print(f'Letter count: {lettercount}')
print(f'Approximate letter count (per word): {lettersperword}')
print(f'Approximate sentence length (in words): {sentencelength}')


file.close()
