list1 = [1,2,3,4,[5,6,7]]
for x in list1:
    if type(x) == list: #to check the element is list or not 
        for i in x:
            print(i)