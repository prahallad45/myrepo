def evenodd(x):
    for i in range(0,x+1):
        if i%2==0:
            print(f'even {i}') 
        else:
            print(f'odd {i}')

n=int(input("Enter number:"))
evenodd(n)