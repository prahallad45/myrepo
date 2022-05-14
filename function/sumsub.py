
#------------POSITIONAL ARGUMENT
def sum1(x,y):
    a=x+y
    b=x-y
    return a,b


add,sub1=sum1(8,6)#positional argument
print(f'sum ={add}\nsub={sub1}')

#---------------------DEFAULT ARGUMENT

def sum1(x,y=5): #default argument
    a=x+y
    b=x-y
    return a,b


add,sub1=sum1(8)
print(f'sum ={add}\nsub={sub1}')
#------------KEYWORD ARGUMENT
def sum1(x,y):
    a=x+y
    b=x-y
    return a,b

add,sub1=sum1(y=8,x=6)#keyword argument
print(f'sum ={add}\nsub={sub1}')





