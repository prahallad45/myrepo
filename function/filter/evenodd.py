def even(n):
    if(n%2==0):
        return True
    else:
        return False
def odd(n):
    if(n%2!=0):
        return True
    else:
        return False
#main function
lst=[33,4,54,43,87,57,12,54,1,7,0,4]
evenfilter=filter(even,lst)
oddfilter=filter(odd,lst)
print(evenfilter)
print("GIVEN ELEMENT ={}".format(lst))
evenlist=list(evenfilter)
print("EVEN NUMBER={}".format(evenlist))
oddlist=list(oddfilter)
print("ODD NUMBER={}".format(oddlist))