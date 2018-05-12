import numpy as np

class PraNum :
	str = ''
	def __init__(self):
		pass
	def temperatute (self):
		celValues = [[25.3,24.8,26.9,23.9,25.3,24.8,26.9,23],[25.3,24.8,26.9,23.9,25.3,24.8,26.9,23.9]]
		cel = np.array(celValues)
		print(cel)
		print (cel.ndim)
		print(cel.shape)
if __name__ == "__main__":
	obj = PraNum()
	obj.temperatute()