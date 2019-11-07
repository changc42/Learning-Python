class person:
	def __init__(self, f=None, l=None, a=None):
		self.first_name = f
		self.last_name = l
		self.age = a
		
	def vocalize(self):
		print("I am person")
		
class student(person):
	def __init__(self, f=None, l=None, a=None, s=None):
		person.__init__(self,f,l,a)
		self.school = s
		
	def vocalize(self):
		print("I am student")
		
	

if __name__ == "__main__":
	x = student("bob" , None, 25, "qc")
	y = person();
	x.vocalize();
	y.vocalize();