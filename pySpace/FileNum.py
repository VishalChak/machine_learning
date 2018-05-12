import numpy as np
import math
class FileNum :
	def __init__(Self):
		pass
	def printArr(self):
		a = np.arange(6)
		print("1D array")
		print(a)
		b= np.arange(12).reshape(4,3)
		print("2D Array")
		print(b)
		c= np.arange(720).reshape(2,3,4,5,6)
		print("ND Array")
		print(c)
		print(c.ndim)
		
		n = np.arange(10000)
		print(n)
		n = np.arange(10000).reshape(10,10,10,10)
		print(n)
		
	def basicOperation(self):
		a= np.array([10,20,30,40])
		b= np.arange(4)
		print(b)
		c = a-b
		print(c)
		b= b**2
		print(b)
		ang = 10*np.sin(a)
		print(ang)
		print(a<35)
		print ("Product and DotFucntion")
		A = np.array([[1,1],[0,1]])
		B = np.array([[2,0],[3,4]])
		print ("Elementwise Product..A*B")
		print(A*B)
		print("Matric ProDUCT")
		print(A.dot(B))
		print ("Operation Like *= += mpdify an Existing Array.. Rather Then Create New One")
		
		a = np.ones((2,3),dtype = int)
		b= np.random.random((2,3))
		print (a)
		print(b)
		b +=a
		print("b +=a")
		print(b)
		print("a +=b:   We need Upcasting in this case")
		
		print ("UpCasting")
		a= np.ones(3, dtype = np.int)
		b = np.linspace(0,math.pi,3)
		print (b)
		print(b.dtype)
		c= a+b
		print(c)
		print(c.dtype.name)
		
		d= np.exp(c*1j)
		print(d)
		print(d.dtype.name)
		
		print("Unary Operation On Array")
		a = np.random.random((2,3))
		print(a)
		print("a.sum : ",a.sum())
		print("a.max: ",a.max())
		print("a.min : ",a.min())
		
		print ("Unary Fucn on Axies")
		a= np.arange(12).reshape(3,4)
		print ("a.sum(axis = 0): ", a.sum(axis = 0))
		print ("a.max(axis = 1): ", a.max(axis = 1))
		print ("a.min(axis = 1): ", a.min(axis = 1))
		print ("a.cumsum(axis = 1): ", a.cumsum(axis = 1))
		
if __name__ == "__main__":
	obj = FileNum()
	obj.printArr()
	obj.basicOperation()