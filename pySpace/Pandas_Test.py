import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Pandas_Test:
	
	def read_Data_by_url(self,url):
		data = pd.read_csv(url,index_col = 0)
		#print(data.head())
		#print(data.tail())
		#print(data.shape)
		return data
	def seaborn_plot(self,data):
		print(data.head())
		sns.pairplot(data, x_vars=['TV','Radio','Newspaper'], y_vars = 'Sales')
	

if __name__ == "__main__":
	obj = Pandas_Test()
	url_path = "http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv"
	data = obj.read_Data_by_url(url_path)
	obj.seaborn_plot(data)
