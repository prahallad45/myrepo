#print harsha and count each character and replace a with anyother letter.
lst = [{'a':1, 'b':2, 'c':{1:2, 2:{'a':5, 'b':7, "c":'harsha'}}}]
print(lst[0]['c'][2]["c"]) #indexing to get harsha from the list
x = lst[0]['c'][2]["c"] 
print({i:x.count(i) for i in x}) #here i is the key and x.count(i) is value .
b=x.replace('a','i')
print(b)