"""
Amanda Robinson 
1181969 
February 16th 2023 
COMP 1112
"""

#importing a regular expression operating library
import re

#creating a dictionary for my repeat element "https://www.w3schools.com/python/python_dictionaries.asp"
repeat = {}
"""
opening my report file and accessing it as read only and storing it in my 
sample text variable
"""
sample_text = open('sample.txt', 'r')

"""
I am now storing same text but all lower case to a text string variable 
because I want the program to add values together even if they are different
due to capital lettering
"""
text_string = sample_text.read().lower()
"""
Here I am asking the program to essentially find patterns with letters.
I am using the regular expression findall (find all) for the words that match the 
boundaries I created "\b" is used to create those boundaries 
[a-z] is looking for the patters containing those letters and {1-20} of those
characters long from the text_string variable which holds all the words in lower case
"""
match_pattern = re.findall(r'\b[a-z]{1,20}\b', text_string)

"""
Thi is a forloop that creates a word variable from each match pattern and counts 
how many times it appears and add one to the frequent count
"""
for word in match_pattern:
    frequent = repeat.get(word,0)
    repeat[word] = frequent + 1

"""
Here I am looking at the most repeated. 
dict is the function I am using to add to my dictionary where the words are repeated 
I used the lambda function "https://www.w3schools.com/python/python_lambda.asp"
Setting reverse to will order it in a descending order. 
"""
most_repeat = dict(sorted(repeat.items(), key=lambda part: part[1], reverse=True))


#This will return my view object which will contain the keys of my dicitonary

repeat_count = most_repeat.keys()

#I want to build something that looks like a table and to do this I need to know
#the length of each word.
#for words in most_frequent_count:
    #print(len(words))
#The longest word is 13 characters. Meaning I should aim my line to be 
#around the 14 or 15th character point


#I am printing the names of my two collumns so they are well defined

print("Word             Count")

"""
Finally, My last for loop will contine through each word that was saved in my 
dicitionary and then read the length. Itll substract the length from the longest
string kept and then multiply the amount of spaces needed each line to have the 
"|" in the same space to give the illusion of a table. Then it all gets added together and printed
"""
for words in repeat_count:
    space_needed= 13 - len(words)
    space=' '*space_needed
    print(words,space,"| ", most_repeat[words])


"""
To create a new txt file. I simply rand command prompt, opened up my A1=python folder 
and typed "python word_count.py > reportA1.txt"
"""
