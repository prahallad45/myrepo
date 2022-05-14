def countfun(str):
    count1=0
    count2=0
    for i in str:
        if(i.islower()):
                count1=count1+1
        elif(i.isupper()):
                count2=count2+1
    print("Total lowercase:")
    print(count1)
    print("Total uppercase:")
    print(count2)

str=input("Enter string:")
countfun(str)