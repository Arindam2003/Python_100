import random

rock='''
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a 
'''

# print(rock)

paper='''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88
'''

scissor='''
                     88                                                       
                     ""                                                       
                                                                              
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'  
'''


print("Welcome to Rock Paper Scissor !!\n\n") 

#user
inp=int(input("What you Choose? 0 for rock, 1 for paper, 2 for scissor: "))
if(inp==0):
    print("You choose:")
    print(rock)
elif(inp==1):
    print("You choose:")
    print(paper)
elif(inp==2):
    print("You Choose:")
    print(scissor)

#computer
number=random.randint(0,2)

if(number==0):
    print("Computer choose:")
    print(rock)
elif(number==1):
    print("Computer choose:")
    print(paper)
elif(number==2):
    print("Computer Choose:")
    print(scissor)

if(inp==0 and number==0):  #rock and rock
    print("draw")
elif(inp==0 and number==1):   #rock and paper
    print("You Looose")
elif(inp==0 and number==2):   #rock and scissor
    print("You Win")
elif(inp==1 and number==0):   #paper and rock
    print("You Win")
elif(inp==1 and number==1):   #paper and paper
    print("Draw")
elif(inp==1 and number==2):   #paper and scissor
    print("You Loose")
elif(inp==2 and number==0):   #scissor and rock
    print("You Loose")
elif(inp==2 and number==1):   #scissor and paper
    print("You Win")
elif(inp==2 and number==2):
    print("Match Draw")