import numpy as np
import csv
class NumFile:
	def __init__(self):
		pass
	def csvReader(self,filePath):
		lines = csv.reader(open(filePath, "r+"))
		dataSet = list(lines)
		#for i in range (len(dataSet)):
		#	print(dataSet[i])
		cel = np.array(dataSet)
		print (cel.shape)
if __name__ == "__main__":
	filePath = "D:/Python/Naive_Bayes/pima-indians-diabetes.data.csv"
	obj = NumFile()
	obj.csvReader(filePath)