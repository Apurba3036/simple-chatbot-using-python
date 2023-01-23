import random
import nltk
import time
from googlesearch import search
from nltk.chat.util import Chat, reflections
now=time.ctime()
 
print("1.Google search 2.Chatbot")
p=input("Choose an option: ")

if p=="1":
    search_query=input("Hey! Ask me anything: ")
    for i in search( search_query,tld='co.in', lang='en', tbs='0',  num=10, start=0, stop=10, pause=2.0):
     print(i)
    
elif p=="2":
    pairs = [
    [
        r"hi|hello|hey|meow",
        ["Hello", "Hey there"]
    ],
    [
        r"how are you?|are you ok?",
        ["I'm doing good", "I am fine", "I'm ok"]
    ],
    [
        r"what is your name?",
        ["You can call me Apurba", "My name is Apurba"]
    ],
    [
        r"what is the time?",
        [now]
    ],
    [
        r"how can you help me?",
        ["I'm here to answer your questions, how can I help you today?"]
    ],
    [
        r"quit",
        ["Goodbye, have a nice day!"]
    ],
   ]

    chatbot = Chat(pairs, reflections)
    chatbot.converse()