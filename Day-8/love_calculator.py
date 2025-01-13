def calculate_love_score(name1,name2):
    combined=name1+name2
    print(combined)
    lower=combined.lower()
    print(lower)
    first=0
    x="true"
    for j in x:
        for i in combined:
            if(j is i):
                first=first+1
    print(first) 

    second=0
    x="love"
    for j in x:
        for i in combined:
            if(j is i):
                second=second+1
    print(second)

    # print(count1)
    # name2.lower()
    # count2=0
    # for i in name2:
    #     count2=count2+name2.count(i)
    # print(count2)
    print("Love Percentage is: ")
    print(str(first)+str(second))
    
calculate_love_score("Arindam", "Dinda")