from BinarySearch import *
class Test2: 
	def __init__(self):
		pass
	def printName(self):
		print("I am Test 2")

if __name__ == "__main__":
	n = int(input("Enter Length of List   "))
	obj  = BinarySearch()
	obj.insert(n)
	obj.listSort()
	x= int(input("Enter Key   "))
	obj.Bsearch(x,0,n-1)