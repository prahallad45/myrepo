x = "prahallad" #global

def myfunc():
  x = "gahir" #local 
  print(x,id(x))

myfunc()
print(x,id(x))

#-----------
def myfunc1():
    global x
    x=22
    print(x,id(x))
x=10
myfunc1()
print(x,id(x))