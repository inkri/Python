#Set the path:
#https://chrisalbon.com/
import os
os.getcwd()
os.chdir("C://ALLbooks_notes//PythonPractice")


# In[30]:


#Load data:
import pandas as pd
data=pd.read_csv("data.csv")


# In[31]:


#Data check:
data.head(2)
data.tail(2)


# In[39]:


#Column Names: Check Names, Data Type, Convert Datatype,Shape of Dataframe
print(data.columns)
data['EMI'].head(2)
data.columns[0:5]
#Data type check
print(data.dtypes[:8])
data['Gender'].dtypes
#Shape of dataframe
print(data.shape)
# converting dtypes using astype 
#data["City_Code"]= data["City_Code"].astype(int64) 
data["City_Category"]= data["City_Category"].astype(str) 
data['ID'].astype('str')
print(data['ID'].dtypes)


# In[42]:


data.head(2)


# In[46]:


#Dropping Column:
del data['City_Code']
data.head(2)


# In[47]:


#Renaming Columns
#https://chrisalbon.com/python/data_wrangling/pandas_dropping_column_and_rows/
data = data.rename({'ID': 'New_ID', 'Gender': 'Sex'}, axis=1)
data.head(2)


# In[61]:


#iloc: For Rows and Column selection
# Rows:
data.iloc[0:2]
# Columns:
data.iloc[:,0] 
data.iloc[100:103,0:4] 


# In[70]:


#Loc:Selection of rowd by Index names
#data.set_index("New_ID", inplace=True)
data.head(2)
#data.loc['APPC90493171225']
data.loc[['APPC90493171225','APPD40611263344']]
data.loc[['APPC90493171225','APPD40611263344'],['New_ID','Sex','DOB']]

