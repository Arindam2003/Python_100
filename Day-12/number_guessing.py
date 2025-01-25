import random
import art

print(art.logo1)
print("Welcome To The Number Guessing Game!")
print("Guess the Number between 1 to 100 ")
ok=True
while ok:
    level = (input("Choose Your Difficulty. Type 'easy' or 'hard': ")).lower()
    if level=='easy':
        chance=10
        ok=False
    elif level=='hard':
        chance =5
        ok=False
    else:
        print("Invalid Level")
main_number=int(random.randint(1,100))
# print(main_number)
i=0
while i<chance:
    print(f"You Have {chance-i} attempts to guess the number.")
    your_number = int(input("Guess the number:  "))
    print(your_number)
    if your_number>main_number:
        print("Too High")
        i=i+1
    elif your_number<main_number:
        print("Too Low")
        i=i+1
    else:
        print("Congratulation, You Guess the number")
        break
if i==chance:
    print("Chance Finish!! You Loose the Game ")