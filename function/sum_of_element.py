#list mul
def sum1(lst):
    t = 0
    for x in lst:
        t += x
    return t

print("ENTER LIST OF VALUE SEPERATED BY SPACE:")
lst=[int (x) for x in input().split( )]
print(f' sum of list:{sum1(lst)}')


print("ENTER VALUE SEPERATED BY SPACE:")
s={int (x) for x in input().split( )}
print(f'sum of set:{sum1(s)}')

print("ENTER VALUE SEPERATED BY SPACE:")
t=(int (x) for x in input().split( ))
print(f'sum of tuple:{sum1(t)}')


