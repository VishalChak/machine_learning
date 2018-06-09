
# coding: utf-8

#     
# #Full Scale Intelligence Quotient
# #Verbal IQ
# #Performance IQ

# In[1]:

import pandas
data = pandas.read_csv('C:/MJ_Syn/Manisha_Notes/Training/ML_Python/Code/Data/brain_size.csv', sep=';', na_values=".")
data 


data.shape    # 40 rows and 8 columns



data.columns  # It has columns 



print(data['Gender'])  # Columns can be addressed by name   

# Simpler selector
data[data['Gender'] == 'Female']['VIQ'].mean()



groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
     print((gender, value.mean()))



groupby_gender.mean()




#Hypothesis testing
from scipy import stats
#One sample t test
stats.ttest_1samp(data['VIQ'], 0)




#2-sample t-test: testing for difference across populations
female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
stats.ttest_ind(female_viq, male_viq) 




#Paired tests: repeated measurements on the same indivuals
stats.ttest_ind(data['FSIQ'], data['PIQ'])




stats.ttest_rel(data['FSIQ'], data['PIQ']) 



stats.ttest_1samp(data['FSIQ'] - data['PIQ'], 0)




#Wilcoxon signed-rank test
stats.wilcoxon(data['FSIQ'], data['PIQ']) 




#One Way ANOVA
import pandas as pd

data = pd.read_csv('C:/MJ_Syn/Manisha_Notes/Training/ML_Python/Code/Data/PlantGrowth.csv', sep=',', na_values=".")
data.head()




#Create a boxplot
data.boxplot('weight', by='group', figsize=(12, 8))
 
ctrl = data['weight'][data.group == 'ctrl']
 
grps = pd.unique(data.group.values)

d_data = {grp:data['weight'][data.group == grp] for grp in grps}
 
k = len(pd.unique(data.group))  # number of conditions
N = len(data.values)  # conditions times participants
n = data.groupby('group').size()[0] #Participants in each condition




from scipy import stats
 
F, p = stats.f_oneway(d_data['ctrl'], d_data['trt1'], d_data['trt2'])





import statsmodels.api as sm
from statsmodels.formula.api import ols
 
mod = ols('weight ~ group',
                data=data).fit()
                
aov_table = sm.stats.anova_lm(mod, typ=2)
print aov_table






