class veryBigSnake:
	# constructor
	# now accepts name and type as arguments
	def __init__(self, name="Peter Python", type="python"):
		self.name = name
		self.type = type
		print ("New snake in da house!")
	
	# function to set snake name
	def set_snake_name(self, name):
		self.name = name
		
	# function to set snake type
	def set_snake_type(self, type):
		self.type = type
	# function to display name and type
	def who_am_i(self):
		print ("My name is " + self.name + ", I'm a " + self.type + " and I'm perfect for you! Take me home today!")
