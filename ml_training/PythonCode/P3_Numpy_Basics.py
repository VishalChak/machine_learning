


import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])
print A
Af = np.array([1, 2, 3], float)
print Af




np.arange(0, 1, 0.2)



np.linspace(0, 2*np.pi, 4)



A = np.zeros((2,3))



A.shape




np.random.random((2,3))




a = np.random.normal(loc=1.0, scale=2.0, size=(2,2))




np.savetxt("a_out.txt", a)



# save to file
b = np.loadtxt("a_out.txt")



A = np.zeros((2, 2))
print A



a = np.arange(10).reshape((2,5))  #Array Attributes
print a.ndim # 2 dimension
print a.shape # (2, 5) shape of array
print a.size # 10 # of elements
print a.T # transpose
print a.dtype # data type




#Array broadcasting with scalars
A = np.ones((3,3))
print A




print 3 * A - 1


# In[ ]:



