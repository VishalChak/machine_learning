import pandas as pd

class ReadingData_Pandas:
	def pd_reader(self, filePath):
		data = pd.read_csv(filePath)
		print(type(data))
		print(type(data))

if __name__ == "__main__":
	train_path = "/home/vishal/ML/Kaggle_Competition/Titanic/train.csv"
	obj = ReadingData_Pandas()
	obj.pd_reader(train_path)
