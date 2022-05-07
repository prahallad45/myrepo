mydict1 = {10:2, 10:34, 30:3, 20:2, 30:1, 40:5}
mydict2 = {}
for x in mydict1:
       if x in mydict2:
              mydict2[x] += 1
              
       else:
              mydict2[x] = 1
              
print(mydict2)