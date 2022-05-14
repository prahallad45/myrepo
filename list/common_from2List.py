a=[3,4,6,1]
b=[1,7,9,3]
print(set(a).intersection(b))


#using function
a=[3,4,6,1]
b=[1,7,9,3]
def common(a,b): 
    c = [x for x in a if x in b] 
    return c
d=common(a,b)
print(d)