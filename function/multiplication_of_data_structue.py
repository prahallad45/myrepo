#list mul
def mult(lst):
    t = 1
    for x in lst:
        t *= x
    return t

print("ENTER LIST OF VALUE SEPERATED BY SPACE:")
lst=[int (x) for x in input().split( )]
print(f'mul of list{mult(lst)}')

print("ENTER VALUE SEPERATED BY SPACE:")
s={int (x) for x in input().split( )}
print(f'mul of set:{mult(s)}')

print("ENTER VALUE SEPERATED BY SPACE:")
t=(int (x) for x in input().split( ))
print(f' mul of tuple:{mult(t)}')


