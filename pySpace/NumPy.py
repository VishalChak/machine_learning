import numpy as np
class NumPy:
	def __init__(self):
		pass

	def example(self):
		a= np.arange(15).reshape(3,5)
		print("example")		
		print(a)
		print("Shape : ", a.shape)
		print("Ndim : ", a.ndim)
		print("dType : ", a.dtype.name)
		print("ItemSize : ", a.itemsize)
		print("Size : ", a.size)
		print("type : ", type(a))
	
	def arrayCreation (self):
		print("arrayCreation")		
		a = np.array([2,3,4])
		print(a)
		print("DataType Of a", a.dtype)
		b= np.array([1.2,3.5,5.1])
		print("DataType of b" , b.dtype)
		
		b = np.array([(1.5,2,3),(4,5,6)])
		print(b.dtype)
		print(b ) 

		print("Specify Type of Array at the time of Creation")
		c = np.array([[1,2],[3,4]] , dtype =complex)		
		print(c)
		
		print("Create Array with Initail Placew Holder")
		print("Zeros")
		zero = np.zeros((3,4), dtype =int)
		print(zero)
		print(zero.ndim)
		print(zero.dtype)

		print("Ones")
		ones = np.ones((2,3,4), dtype = np.int16)
		print(ones)
		print(ones.ndim)
		print("Empty")
		emp = np.empty( (2,3) )
		print(emp)

		print ("arange")
		arr = np.arange(10,50,5)
		print(arr)
		print(np.arange(1.0,5.0,.6))
	
	def printArr(self):
		print("printArr")
		a = np.arange(6)
		print("1D Array")
		print(a)
		
		a = np.arange(12).reshape(3,4)
		print("2D Array")
		print(a)
		
		a = np.arange(48).reshape(4,3,4)
		print("3D Array")
		print(a)
	def reshapeFu`	```````````

if __name__ == "__main__":
	obj = NumPy()
	obj.example()
	obj.arrayCreation()
	obj.printArr()
