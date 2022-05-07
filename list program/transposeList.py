def transpose(l1, l2):
    for i in range(len(l1[0])): #here range is 3
        row =[]
        for item in l1: # i contains index position and item contains values
            row.append(item[i]) 
        l2.append(row)
    return l2
 
l1 = [[3,6,2],[1,8,2],[9,4,6]]
l2 = []
print(l1)
print(transpose(l1, l2))