print("Welcome to pizza Delivries!!")
size=input("What is the size you want? S,M,L: ")
peperoni=input("Do you want peperoni? Y or N: ")
extra_cheese=input("Want extra cheese?Y or N: ")
price=0
if(size=='S'):
    price=100
elif(size=="M"):
    price=150
elif(size=="L"):
    price=200

if(peperoni=="Y"):
    price=price+100
elif(peperoni=="N"):
    price=price+0

if(extra_cheese=="Y"):
    price=price+100
elif(extra_cheese=="N"):
    price=price+0


print(f"Your Pizza Price is : {price}")