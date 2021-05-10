
# coding: utf-8

# In[20]:


#Python File i/o
import os
os.getcwd()
os.chdir('C:\Classroom\Python')
os.listdir()


# In[23]:


#Python Pandas
import pandas as pd
furniture=pd.read_csv('test.csv')
furniture.head(2)


# In[35]:


#Datasets
#Column names
furniture.columns
furniture.columns[0:2]
#Data types
furniture.dtypes
furniture['Pclass'].dtypes
#Shape
furniture.shape
furniture.shape[0]
furniture.shape[1]
#Individual rows
furniture.head(3)
furniture.tail(2)
#Unique values
furniture.index.unique()
furniture.index.nunique()


# In[47]:


#DataFrames
#pandas.DataFrame( data, index, columns, dtype, copy)
#Creating a DataFrame
df=pd.DataFrame({'company':['Amazon','Apple','Google','Facebook','Microsoft'],
    'CEO':['Jeff Bezos','Tim Cook','Sundar Pichai','Mark Zuckerberg','Satya Nadella'],
    'Founded':[1994,1976,1998,2004,1975]})
df

#Setting Indexes for a DataFrame
df.index=['Third','Second','Fourth','Fifth','First']
df
#Indexing a DataFrame
df['company']
df[['company']]
df[['company','Founded']]

#Slicing a DataFrame
df[0:3]

#More data selection operations
#Using loc and iloc, you can select certain rows in a data set. loc uses string indices; iloc uses integers.
df.loc[['Second','Fifth']]
df.iloc[3]
df.iloc[:,1:4]


# In[70]:


#Manipulating the Datasets
#Changing the data type
furniture.Cost=furniture.Fare.astype(float)
furniture.head(1)

#Creating a frequency distribution
#furniture.index=['A','B','A','A','C']
#furniture.index.value_counts(ascending=True)

#Creating a crosstab
pd.crosstab(furniture.index,furniture.Pclass)

#Choosing one column as index
#df.set_index('company',inplace=True)
df
#df.reset_index(inplace=True)
df
#Sorting data
furniture.sort_values('Fare',ascending=False).head(2)

#Renaming variables
#df.columns=['Company','CEO','Founded']
df
furniture.rename(columns={'Product':'Category'},inplace=True)
furniture

#Dropping rows and columns
furniture.drop('Fare',axis=1)

#Creating new variables
furniture['Gross']=furniture.eval('Fare+(Fare*(0.1))')
furniture.head(2)


# In[73]:


#Describing a Dataset
furniture.describe()
furniture.Gross.max()


# In[76]:


#groupby Function
furniture.groupby('Pclass').Gross.min()
furniture.groupby('Pclass').Gross.agg(['count','min','max','mean'])


# In[81]:


#Filtering
furniture[furniture.index==2]
furniture.loc[furniture.index==2,:]
furniture[furniture.index.isin([1,3])]


# In[85]:


#Missing Values 
furniture.isnull().head(3)
furniture.isnull().sum()


# In[88]:


#Ranking
furniture.rank().head(2)


# In[89]:


#Concatenating DataFrames
#pd.concat([df,furniture])


# In[92]:


#Series
pd.Series([2,4,'c'])
pd.Series({1:'a',2:'b'})


# In[94]:


#Panels
import numpy as np
pd.Panel(np.random.rand(2,4,5))


# In[ ]:


#https://data-flair.training/blogs/python-numpy-tutorial/

