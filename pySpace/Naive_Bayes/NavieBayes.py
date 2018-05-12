import csv
import random
class NavieBayes:
	def loadCsv(self,filename):
		lines = csv.reader(open(filename, "r+"))
		dataset = list(lines)
		for i in range(len(dataset)):
			dataset[i] = [float(x) for x in dataset[i]]
		return dataset
	def splitDataset(self,dataset,splitRatio):
		trainSize = int(len(dataset)* splitRatio)
		trainSet = []
		copy = list(dataset)
		count = 0
		while len(trainSet) < trainSize:
			count = count+1
			index = random.randrange(len(copy))
			trainSet.append(copy.pop(index))
		return [trainSet, copy]
	def separateByClass(self, dataset) : 
		separated = {}
		for i in range (len(dataset)) : 
			vector = dataset[i]
			if (vector[-1] not in separated) : 
				separated [vector[-1]] = []
			separated [vector [-1]].append(vector)
		return separated
if __name__ == "__main__":
	obj = NavieBayes()
	fileName = "D:\\Python\\Naive_Bayes\\pima-indians-diabetes.data.csv"
	dataset = obj.loadCsv(fileName)
	print('Loaded data file {0} with {1} rows'.format(fileName, len(dataset)))
	dataset = [[1], [2], [3], [4], [5], [6], [7], [8]]
	splitRatio = 0.67
	train, test = obj.splitDataset(dataset, splitRatio)
	print('Split {0} rows into train with {1} and test with {2}'.format(len(dataset), train, test))
	dataset = [[1,20,1], [2,21,0], [3,22,1]]
	separated = obj.separateByClass(dataset)
	print('Separated instances: {0}'.format(separated))