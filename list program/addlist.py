lst1 = [1,2,3]
lst2 = [4,5,6]
print (lst1)
print (lst2)
 
lst3 = []
for i in range(0, len(lst1)):
    lst3.append(lst1[i] + lst2[i])
print (lst3)