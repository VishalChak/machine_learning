



# Import Library

import pandas as pd


# Read data from a url

url = "https://vincentarelbundock.github.io/Rdatasets/csv/datasets/HairEyeColor.csv"

df = pd.read_csv(url)


# Type of the df object

type(df)



# Column names

list(df)



# Show first few rows

df.head()



# Show last few rows

df.tail()



# Data type of each column

df.dtypes



# Return number of columns and rows of dataframe

df.shape



#  Number of rows

len(df.index)



# Number of columns

len(df.columns)



# Basic statistics

df.describe()



# Extract first three rows

df[0:3]

# or
    
#df.iloc[:3]



# Filter for black hair

#df[df['Hair']=="Black"]

     # or
    
df.query("Hair =='Black'")



# Filter for males who have black hair

#df[(df['Hair']=="Black")  & (df["Sex"]=="Male")]


# or
df.query("Hair == 'Black' & Sex =='Male'")




#WAP to Filter for those who have brown eye or black hair


#Ans:
z = df[(df['Hair']=="Black") | (df["Eye"]=="Brown")]


# or
z = df.query("Hair == 'Black' | Eye =='Brown'")

z.head(6)




# Filter for eye color of blue, hazel and green

df[df.Eye.isin(['Blue','Hazel','Green'])].head()




# Select one column

df[["Eye"]].head()

# or

df.Eye.head()



# Select two columns

df[["Eye","Sex"]].head()




# Unique Eye colors

df["Eye"].unique()




# Maximum of the "Freq" column

df.Freq.max()




# Call functions on multiple columns 

import numpy as np

pd.DataFrame({'Max_freq': [df.Freq.max()],              'Min_freq': [df.Freq.min()],             'Std_freq': [np.std(df.Freq)]})




# Maximum Frequency by Sex

df.groupby("Sex").agg({"Freq":"max"})




#Display max Freq by color




df.groupby("Eye").agg({"Freq":"max"})




# Count by Eye color and Sex

df.groupby(["Eye","Sex"]).agg({"Freq":"count"}).rename(columns={"Freq":"Count"})



# Call functions for grouping

df.assign(Gt50 = (df.Freq > 50)).groupby("Gt50").agg({"Gt50":"count"}).rename(columns ={"Gt50":"Count"})



# Do the analysis on selected rows only

pd.DataFrame({'Max_freq': [df[0:10].Freq.max()],              'Min_freq': [df[0:10].Freq.min()],             'Std_freq': [np.std(df[0:10].Freq)]})




# Remove a column

df.drop('Unnamed: 0', 1).head()




# Return the first occurance

df.query("Eye == 'Blue'")[:1]




# Return the last occurance

df.query("Eye == 'Blue'")[-1:]




# Return a count

df[df.Eye.isin(['Blue','Hazel']) & (df.Sex=="Male")].shape[0]




# Count for each group

df[df.Eye.isin(['Blue','Hazel']) & (df.Sex=="Male")].groupby(["Eye","Sex"]).agg({"Freq":"count"}).rename(columns={"Freq":"Count"})



# Order in ascending order

df.sort_values(by='Freq').tail(6)



# Order in descending order

df.sort_values(by='Freq', ascending = False).tail(6)




# "Freq" in descending and "Eye" in ascending

df.sort_values(by=['Freq','Eye'], ascending = [False,True]).tail(6)




# Rename columns

df.rename(columns = {"Freq":"Frequency","Eye":"Eye_Color"}).tail()




# Unique rows

df[["Eye","Sex"]].drop_duplicates()




# Create new column

df.assign(Eye_Hair =df.Eye + df.Hair)[["Eye","Hair","Eye_Hair"]].head()






