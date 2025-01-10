#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

'''
result=""
for i in range (1,nr_letters+1):
    result=result+random.choice(letters)

for i in range (1,nr_symbols+1):
    result=result+random.choice(symbols)
for i in range (1,nr_numbers+1):
    result=result+random.choice(numbers)

print(result)
    
'''

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

result=[]

for i in range (1,nr_letters+1):
    result.append(random.choice(letters))

for i in range (1,nr_numbers+1):
    result.append(random.choice(numbers))

for i in range (1,nr_symbols+1):
    result.append(random.choice(symbols))

print(result)
random.shuffle(result)
print(result)

password = ""

for i in result:
    password+=i

print(password)
