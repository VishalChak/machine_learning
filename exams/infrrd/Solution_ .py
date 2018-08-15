
# coding: utf-8

# In[208]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set_style("darkgrid")

base_path = "/home/vishal/datasets/exams/Infrrd/"
train_path = base_path+"train.csv"
test_path =  base_path+"test.csv"

dataset = pd.read_csv(train_path)
dataset.head()


# In[209]:


# Exploratory Analysis

dataset.dtypes  # all are categorical feature


# In[210]:


dataset.describe() 
# No Null values


# In[211]:


dataset['purchasing_cost'].value_counts(dropna = False)
dataset['purchasing_cost'].value_counts(dropna = False).head(10).plot.bar()


# In[212]:


#dataset['repair_cost'].value_counts(dropna = False)
dataset['repair_cost'].value_counts(dropna = False).head(10).plot.bar()


# In[213]:


#dataset['windows'].value_counts(dropna = False)
dataset['windows'].value_counts(dropna = False).plot.bar()


# In[214]:


#dataset['people'].value_counts(dropna = False)
dataset['people'].value_counts(dropna = False).plot.bar()


# In[215]:


dataset['space'].value_counts(dropna = False)
dataset['space'].value_counts(dropna = False).plot.bar()


# In[216]:


dataset['safety'].value_counts(dropna = False)
#dataset['safety'].value_counts(dropna = False).plot.bar()


# In[217]:


dataset['label'].value_counts(dropna = False) # Data is Not balanced
dataset['label'].value_counts(dropna = False).plot.bar()


# In[218]:


# level encodeders

def label_encoder(val, col_dict):
    return col_dict[val]

pc_dict = {'low':1, 'medium':2, 'high': 3, 'very_high': 4}
dataset['pc'] = dataset['purchasing_cost'].apply(label_encoder, args = (pc_dict,))

rc_dict = {'low':1, 'medium':2, 'high': 3, 'very_high': 4}
dataset['rc'] = dataset['repair_cost'].apply(label_encoder, args = (rc_dict,))

windows_dict = {'2':2, '3':3, '4':4, '5more': 5}
dataset['win'] = dataset['windows'].apply(label_encoder, args = (windows_dict,))

people_dict = {'2':2, '4':4, 'more': 6}
dataset['ppl'] = dataset['people'].apply(label_encoder, args = (people_dict,))

space_dict = {'small':1, 'medium':2, 'big': 3}
dataset['spc'] = dataset['space'].apply(label_encoder, args = (space_dict,))

safety_dict = {'low':1, 'med':2, 'high': 3}
dataset['sfty'] = dataset['safety'].apply(label_encoder, args = (safety_dict,))

label_dict = {'unacceptable':1, 'acceptable':2, 'good': 3, 'very_good':4}
dataset['lbl'] = dataset['label'].apply(label_encoder, args = (label_dict,))

dataset.head()


# In[219]:


# Correlation cofficient matrix 
data_vec = dataset[['pc', 'rc','win', 'ppl', 'spc','sfty','lbl']]
data_vec.corr(method= 'spearman')


# In[220]:


# data selection round 1
from sklearn.model_selection import train_test_split
y = data_vec['lbl']
X  = data_vec[['win', 'ppl', 'spc', 'sfty']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)


# In[221]:


# Round 1 # Model 1
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)
clf.fit(X_train,y_train)
#clf.feature_importances_
#clf.score(X_train, y_train)
clf.score(X_test, y_test)


# In[222]:


# Round 1 feature importance graph
y_pos = np.arange(len(X.columns))
feature_importance = clf.feature_importances_
plt.barh(y_pos, feature_importance, align='center', alpha=0.5)
plt.yticks(y_pos, X.columns)
plt.xlabel('importance')


# In[223]:


# round 1 # model 2
from sklearn.svm import LinearSVC
clf_svm = LinearSVC(random_state=0)
clf_svm.fit(X_train, y_train)
clf_svm.score(X_train, y_train)


# In[224]:


# round 1 model 3
from sklearn import svm
clf_mlticlass = svm.SVC(decision_function_shape='ovo')
clf_mlticlass.fit(X_train,y_train)
clf_mlticlass.score(X_train, y_train)


# In[225]:


# Round 1  # Model overfitting test : Testing on test data
clf_mlticlass.score(X_test, y_test)


# In[226]:


# New feature cration (Polynomialy feature creation)


# In[227]:


dataset['win_ppl'] = dataset['win'] * dataset['ppl']
dataset['win_spc'] = dataset['win'] * dataset['spc']
dataset['win_sfty'] = dataset['win'] * dataset['sfty']

dataset['ppl_spc'] = dataset['ppl'] * dataset['spc']
dataset['ppl_sfty'] = dataset['ppl'] * dataset['sfty']

dataset['spc_sfty'] = dataset['spc'] * dataset['sfty']

dataset.head()


# In[228]:


# Round 2 Correlation cofficient matrix 
data_vec = dataset[['pc', 'rc','win', 'ppl', 'spc','sfty','win_ppl','win_spc','win_sfty','ppl_spc','ppl_sfty','spc_sfty','lbl']]
data_vec.corr(method= 'spearman')


# In[229]:


y_2 = data_vec['lbl']
X_2  = data_vec[['win', 'ppl', 'spc', 'sfty', 'win_ppl', 'win_spc','win_sfty','ppl_spc', 'ppl_spc', 'ppl_sfty', 'spc_sfty']]
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X_2, y_2, test_size=0.20, random_state=1)


# In[230]:


# ROund 2 model 1
from sklearn import svm
clf_mlticlass_2 = svm.SVC(decision_function_shape='ovo')
clf_mlticlass_2.fit(X_train_2,y_train_2)
clf_mlticlass_2.score(X_train_2, y_train_2)


# In[231]:


# Remaning Study is: Data balasing [SMOTE], Model selection based f1 score etc


# In[232]:


data_test = pd.read_csv(test_path)
data_test['win'] = data_test['windows'].apply(label_encoder, args= (windows_dict,))
data_test['ppl'] = data_test['people'].apply(label_encoder, args= (people_dict,))
data_test['spc'] = data_test['space'].apply(label_encoder, args= (space_dict,))
safety_dict['medium'] = 2
data_test['sfty'] = data_test['safety'].apply(label_encoder, args= (safety_dict,))
data_test.head()


# In[233]:


data_test['win_ppl'] = data_test['win'] * data_test['ppl']
data_test['win_spc'] = data_test['win'] * data_test['spc']
data_test['win_sfty'] = data_test['win'] * data_test['sfty']

data_test['ppl_spc'] = data_test['ppl'] * data_test['spc']
data_test['ppl_sfty'] = data_test['ppl'] * data_test['sfty']

data_test['spc_sfty'] = data_test['spc'] * data_test['sfty']
data_test.head()


# In[234]:


X_test_2  = data_vec[['win', 'ppl', 'spc', 'sfty', 'win_ppl', 'win_spc','win_sfty','ppl_spc', 'ppl_spc', 'ppl_sfty', 'spc_sfty']]
X_test_2.head()
y_cap = clf_mlticlass_2.predict(X_test_2)
data_test['y']= pd.DataFrame(y_cap)


# In[236]:


# inverse transformation of lebel

inv_label_dict = {1:'unacceptable', 2:'acceptable', 3:'good',4:'very_good'}
data_test['lbl'] = data_test['y'].apply(label_encoder, args= (inv_label_dict,))
data_test.head()

