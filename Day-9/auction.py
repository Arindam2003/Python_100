import art
print(art.secrete)
print(art.auction)
all_bid={}
yes_no=True
while(yes_no):
    name=str(input("Enter Bidder Name: "))
    bid=int(input("Your Bid: "))
    all_bid[name]=bid
    # print(all_bid)
    yes_no=str(input("'Yes' for continue,,'No' for break:\n").lower())
    if(yes_no=="no"):
        yes_no=False
    # elif(yes_no=='yes'):
    #     # print("\n"*50)

max=0
for key in all_bid:
    max=all_bid[key]
    max_bidder=key
print(f"\n\nMax Bid is-{max} and the bidder is {max_bidder}\n\n\n")


