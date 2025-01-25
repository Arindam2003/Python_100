#Display
from art import logo,vs
from game_data import data
import random

def format_data(account):
    """#Formate data generate data """
    account_name=account["name"]
    account_des=account["description"]
    account_country=account["country"]
    return f"{account_name}, a {account_des}, from {account_country}"

def check_ans(user_guess,a_follower,b_follower):
    if a_follower>b_follower:
        if user_guess=='a':
            return True
        else:
            return False
    else:
        if user_guess == 'b':
            return True
        else:
            return False

print(logo)
score=0
#Generate a random account from me data
account_b=random.choice(data)
flag=True
while flag:
    account_a=account_b
    account_b=random.choice(data)
    if account_a == account_b:
        account_b=random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")


    #ask user to guess
    guess =(input("Who has more follower? Type 'A' or 'B': ")).lower()

    print("\n"*20)
    print(logo)
    #check the user is correct or wrong
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct=check_ans(guess,a_follower_count,b_follower_count)

    #give user feedback of their guess

    #score keeping
    if is_correct:
        score += 1
        print(f"You are Right! Current score {score}")
    else:
        print(f"Sorry, that's Wrong. Final score: {score}")
        flag=False
#Make the game reapeat if user is write

# Position B become the next at position A.

