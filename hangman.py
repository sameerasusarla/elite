#requests library for importing data from html sites
import requests
import random

def find_index(word, ch):
    return [index for index, ltr in enumerate(word) if ltr == ch]
        
def replace_letters(user_word,indices,word):
    for i in indices:
        user_word[i] = word[i]

def decision():
    chance=0
    while(chance<10):
        user_letter=input('Enter a letter: ')
        if user_letter in word:
            indices = find_index(word,user_letter)
            replace_letters(user_word,indices,word)
            print(''.join(user_word))
        else :
            chance+=1
            print("please try again!")
        if '_' not in user_word:
            print("YOU WON!")
            break

word_site="https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
words = response.content.splitlines()
word = str(random.choice(words))
word = word[2:len(word)-1]
user_word=[]
for blank in range(0,len(word)):
    user_word.append('_')
print(user_word)
decision()
if '_' in user_word :
    print("YOU LOST!")
    print(word)

