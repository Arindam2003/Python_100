import random
import art

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score==c_score:
        return "Draw"
    elif c_score==0:
        return "You Loose,Computer have BlackJack"
    elif u_score==0:
        return "Win with a Blackjack"
    elif u_score>21:
        return "You Went over,You loose"
    elif c_score>21:
        return "Computer Went over ,You Win"
    elif u_score>c_score:
        return "You Win"
    else:
        return "You Loose"
def play_game():
    user_card=[]
    computer=[]
    is_game_over=False
    computer_score=-1
    user_score=-1
    # x=deal_cards()
    # print(x)

    for _ in range(2):
        user_card.append(deal_cards())
        computer.append(deal_cards())

    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer)
        print(f"Your cards: {user_card}, current score {user_score}")
        print(f"Computer First Card: {computer[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass:").lower()
            if user_should_deal=="y":
                user_card.append(deal_cards())
            else:
                is_game_over=True

    while computer_score !=0 and computer_score<17:
        computer.append(deal_cards())
        computer_score=calculate_score(computer)

    print(f"Your Final Hand: {user_card}, Final score: {user_score}")
    print(f"Computer Final Hand: {computer}, Final score: {computer_score}")
    print(compare(user_score,computer_score))

while(input("Do you want to play a new game of BlackJack ? 'y' or 'n':")).lower()=='y':
    print("\n")
    print(art.logo)
    play_game()

