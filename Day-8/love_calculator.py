def calculate_love_score(name1,name2):
    combined=name1+name2
    print(combined)
    lower=combined.lower()
    print(lower)
    count1=0
    x="true"
    for j in x:
        for i in name1:
            count1=count1+name1.count(i)
    print(count1)
    name2.lower()
    # count2=0
    # for i in name2:
    #     count2=count2+name2.count(i)
    # print(count2)
    # print(str(count1)+str(count2))
    
calculate_love_score("Arindam", "Dinda")