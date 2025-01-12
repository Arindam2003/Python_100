'''
# import random
from random_word import RandomWords

# WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
# random_word=random.choice(WORDS)  // from random 
r=RandomWords()
random_word=r.get_random_word()  # RandomWords generates
print(random_word)

random_word_length=len(random_word)
chance=random_word_length*2
final_word=[]

while(chance>0):
    user_inp=input("Enter a Word: ")
    if(user_inp in random_word):
        print("Yes")
        index=random_word.index(user_inp)
        print(index)      #index=4
        final_word.insert(index,user_inp)
        print(final_word)
        if(final_word is random_word):
            print("You Won the Game")
    else:
        print("Nop")
        chance=chance-1

print("Lost The Game !!")
'''

import sys
import random 
from hangman_art import stages
from hangman_words import word_list
from hangman_logo import logo

print(f"{logo}\n")

random_word=random.choice(word_list)
# print(random_word)

random_word_length=len(random_word)

placeholder=""
for position in range(1,random_word_length+1):
    placeholder+="_ "
print(placeholder)

chance=6
correct_ans=[]

while(chance>0):
    print(f"************************* {chance}/6 LIVES LEFT  **************************")
    user_inp=input("\nGuess a letter: ").lower()
    if user_inp in correct_ans:
        print(f"Yoou've already Gussed {user_inp}")
    display=""
    if(user_inp in random_word):
        for i in random_word:
            if(user_inp == i ):
                display+=i
                correct_ans.append(i)
            elif (i in correct_ans):
                display+=i
            else:
                display+="_ "
        print(display)
        print(stages[chance])
        # print(f"Moves Remaining - {chance}\n")
        if("_ " not in display):
            print("***************** YOU WIN ********************")
            sys.exit()
    else:
        chance-=1
        print(f"You Guessed {user_inp},that's not in the word. You loose a life")
        for i in random_word:
            if(user_inp == i ):
                display+=i
                correct_ans.append(i)
            elif (i in correct_ans):
                display+=i
            else:
                display+="_ "
        print(display)
        print(stages[chance])
        # print(f"Moves Remaining - {chance}\n")

print(f"**********************IT WAS {random_word}! YOU LOOSE *****************")