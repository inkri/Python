
# coding: utf-8

# In[1]:


#numpy
import numpy as np


# In[8]:


#1-D Array
my_list=[1,2,3,4]
print(type(my_list))
print(my_list)
x=np.array(my_list)
print(type(x))
print(x)


# In[20]:


#2/Multi-D Array
y=np.array([[1,2,3,4],[5,6,7,8]],dtype='float')
print(type(y))
print(y)
print(y.size)
print(y.shape)
print(y.ndim)
print(y.dtype)
yy=y.astype('int')
print(yy.dtype)


# In[45]:


#Built in functions
x1=np.zeros((2,3))
print(x1)
x2=np.ones((2,2))
print(x2)
x3=np.eye((3))
print(x3)
x4=np.diag([1,2,3])
print(x4)
x5=np.arange(0,10)
print(x5)
x6=np.linspace(0,3,7)
print(x6)
print(len(x6))
[1,2]*3
x7=np.array([1,2]*3)
print(x7)
x8=np.repeat([1,2],3)
print(x8)


# In[54]:


#Stacking
onces=np.ones((2,3))
print(onces)
twos=onces*2
print(twos)
t1=np.vstack([onces,twos])
print(t1)
t2=np.hstack([onces,twos])
print(t2)


# In[56]:


#Pandas
import pandas as pd
from pandas import Series, DataFrame 


# In[71]:


#Series
data=Series([-1,-2,0,1,2,3,4])
print(data.dtype)
print(type(data))
print(data.shape)
print(len(data))
print(data.ndim)
print(data.size)
print(data)
print(data[0:2])
print(data.values)
print(data.index)


# In[82]:


dat=Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(dat)
print(dat[0])
print(dat['a'])
print(dat[['a','d']])
print(dat[0]>0)
print(dat*2)


# In[89]:


#numpy
import numpy as np
print(np.exp(dat))
city={'Delhi':7.8,'Bangalore':18,'Mumbai':25}
data=Series(city,index=['Pune','Chennai','Patna','Mumbai','Bangalore'])
print(data)


# In[93]:


#DataFrame
sold=[{'c_id':1,'name':'ram','age':23},
     {'c_id':2,'name':'rama','age':27},
     {'c_id':3,'name':'sam','age':29},
     {'c_id':4,'name':'ramy','age':33},
     {'c_id':5,'name':'ramit'},]
print(sold)
df=DataFrame(sold)
print(df)


# In[99]:


#Accessing rows and columns
print(df.loc[0])
print(df['name'])
print(df.loc[3,'name'])
print(df.loc[2:3,['name','c_id']])


# In[103]:


#boolean indexing
df1=df['name']=='ramy'
print(df1)
print(df[df1])


# In[116]:


#DataFrame modification
df['Uage']=df['age']*df['c_id']
print(df)
del df['Uage']
print(df)
df1=df.drop(4)
print(df1)
df.drop(3,inplace=True)
print(df)
df.loc[0,'name']='Abhi'
print(df)

