print("ENTER LIST OF NUMBER SEPERATED BY SPACE:")
lst=[int(x) for x in input().split( )]
evenlst=list(filter(lambda n: n%2==0,lst))
oddlst=list(filter(lambda n: n%2!=0,lst))
print("GIVEN LIST=",lst)
print("EVEN NUMBER=",evenlst)
print("ODD NUMBER=",oddlst)