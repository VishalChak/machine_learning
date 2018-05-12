import numpy as np
import matplotlib.pyplot as plt

class lessBasic:
	def histoGram(self):
		mu,sigma = 2,0.5
		v= np.random.normal(mu,sigma,1000)
		print(v)
		plt.hist(v,bins=50,normed = 1)
		plt.show()
		(n, bins) = np.histogram(v, bins=50, normed=True)
		plt.plot(.5*(bins[1:]+bins[:-1]), n)
		plt.show()
		
if __name__ == "__main__":
	obj = lessBasic()
	obj.histoGram()