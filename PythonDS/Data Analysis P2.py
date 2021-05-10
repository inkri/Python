
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


fname='C:/Classroom/Python/train.csv'
data=pd.read_csv(fname)
print(data[0:1])
print(len(data))


# In[9]:


data.head()


# In[10]:


data.count()


# In[13]:


#Use fuction to check age
data['Age'].min(),data['Age'].max()


# In[20]:


#Check levels of target feature
print(data['Survived'].value_counts())
print(data['Survived'].value_counts() * 100/len(data))
print(data['Sex'].value_counts())
print(data['Pclass'].value_counts())


# In[24]:


#Graphs
get_ipython().run_line_magic('matplotlib', 'inline')
alpha_color=0.5
data['Survived'].value_counts().plot(kind='bar')


# In[25]:


data['Survived'].value_counts().plot(kind='bar',color=('b','r'),alpha=alpha_color)


# In[27]:


data['Pclass'].value_counts().sort_index().plot(kind='bar',alpha=alpha_color)


# In[28]:


data.plot(kind='scatter',x='Survived',y='Age')

