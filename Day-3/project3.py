print("Welcome To Treasure Island!!\n")
print('''
 ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
''')
print()
direction=input("Which direction you will go?? left or right: ")
if(direction=="left"):
    work=input("What you want to do?? Swim or wait: ")
    if(work=="wait"):
        med=input("Which you door choose? Red or Blue or Yellow: ")
        if(med=="Red"):
            print("Burned by fire.!\nGame Over!")
        elif(med=="Blue"):
            print("Eated by beasts.\n Game Over!!")
        elif(med=="Yellow"):
            print("You Win")
        else:
            print("Game Over!!")
    else:
        print("Attacked by giant!!")
else:
    print("Fall into a hole.\nGame Over!")
