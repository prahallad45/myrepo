even=lambda n: n%2==0
odd=lambda n: n%2!=0

#main program
print("ENTER LIST OF NUMBER SEPERATED BY SPACE:")
lst=[int(val)for val in input().split( )]
evenlst=list(filter(even,lst))
oddlst=list(filter(odd,lst))
print("GIVEN NUMBER=",lst)
print("EVEN NUMBER=",evenlst)
print("ODD NUMBER=",oddlst)
