
# coding: utf-8

# In[1]:


# pre processing with keras 


# In[3]:


import numpy as np
from random import randint
from sklearn.preprocessing import MinMaxScaler


# In[4]:


train_lables = []
train_sample = []


# In[6]:


for i in range(1000):
    random_younger = randint(13,64)
    train_sample.append(random_younger)
    train_lables.append(0)
    
    random_older = randint(65,100)
    train_sample.append(random_older)
    train_lables.append(1)
    
for i in range(50):
    random_younger = randint(13,64)
    train_sample.append(random_younger)
    train_lables.append(1)
    
    random_older = randint(65,100)
    train_sample.append(random_older)
    train_lables.append(0)


# In[10]:


train_lables = np.array(train_lables)
train_sample = np.array(train_sample)


# In[12]:


scaller = MinMaxScaler(feature_range=(0,1))
scaled_train_sample = scaller.fit_transform((train_sample).reshape(-1,1))


# In[13]:


def get_data():
    return scaled_train_sample, train_lables

