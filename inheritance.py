
#single inheritance
class Pg:
	def display(self):
		print("ROHIT")

class Raj(Pg):
	def display1(self):
		print("SHARMA")

c=Raj()
c.display()
c.display1()


#------------------------
class Parents:
	def __init__(self,fname,fage):
		self.name=fname
		self.age=fage
	def show(self):
		print(self.name,self.age)

class Child(Parents):
	def __init__(self, fname, fage):
		Parents.__init__(self,fname, fage)
		self.lname="gahir"

	def view(self):
		print(f'age={self.age},lastname={self.lname},first name={self.name}')

obj=Child('prahallad',24)
obj.view()
obj.show() #THROUGH CHILD CLASS OBJ WE CAN ACCESS THE PARENTS CLASS METHODS


#-----------multilevel inheritance-------------
class Grantparent:
	def show1(self):
		print("this is grantparents")

class Parent(Grantparent):
	def show2(self):
		print("this is parent")

class Child(Parent):
	def show3(self):
		print("this is child")

obj=Child()
obj.show3()
obj.show2()
obj.show1()



