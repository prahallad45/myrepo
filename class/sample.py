class Prahallad:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'name = {self.name}\n age = {self.age}')

p=Prahallad("prahallad",24)
p.show()

#----------X--------------------x--------------

class Base(object):

	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

class Child(Base):
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	def getAge(self):
		return self.age

class GrandChild(Child):
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	def getAddress(self):
		return self.address	

g = GrandChild("Prahallad Gahir", 23, "odisha")
print(g.getName(), g.getAge(), g.getAddress())
