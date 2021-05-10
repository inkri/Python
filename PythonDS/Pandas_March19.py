
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data=[{'x':10,'y':12,'z':14},{'x':22,'y':24,'z':28},{'x':32,'y':34,'z':38}]


# In[3]:


df=pd.DataFrame(data)
df


# In[6]:


import os
os.getcwd()
os.chdir("C:\Classroom\Python\Pandas")
df=pd.read_csv("chicago_crime_data.csv")


# In[25]:


df.head(2)
df.tail(2)
df.shape
len(df)
df.columns
#df.info()
df['District'].tail(3)


# In[27]:


#Convert Object to Date type
df['Date']=pd.to_datetime(df['Date'])
df['Updated On']=pd.to_datetime(df['Updated On'])


# In[28]:


df.info()


# In[37]:


#Function
df['Year'].max()
df['Ward'].min()
df['Ward'].sum()
df['Ward'].mean()
df['Ward'].median()


# In[45]:


#Missing Values
df.isna().sum()
a=df['Ward'].mean()
#Filling missing value
df['Ward']=df['Ward'].fillna(value=a)
df.isna().sum()
#Drpping missing values: axis=0 Rows and axis=1 columns
df.dropna(axis=0,inplace=True)
df.isna().sum()
df.head(4)
#Re setting Indexvalues
df.reset_index(inplace=True,drop=True)
df.head(4)


# In[48]:


#Row data
df.iloc[[67]]


# In[50]:


#Rows data in range
df.iloc[2:6]


# In[54]:


#select multiple colums
df[['ID','Ward']].head(2)
df[['ID','Ward']][3:7]


# In[56]:


#Rows and colums selection
df.iloc[2222:2227,2:5]


# In[58]:


#Last row of data frame
df.iloc[[-1]]
#Last column of data frame
df.iloc[2:4,-1]


# In[63]:


#Filtering
df.loc[(df['Ward']<=34)].head(2)


# In[64]:


#2 conditions
df.loc[(df['Ward']>34) & (df['Primary Type']=='THEFT')].tail(2)


# In[65]:


#Split columns
df['lat1'],df['long1']=df['Location'].str.split(',',1).str
df.head(2)


# In[66]:


#Replace function
df['lat1']=df.lat1.str.replace("(","")
df['long1']=df.long1.str.replace(")","")
df.tail(3)


# In[68]:


#Merge two columns into new one
df['geo']=df['lat1']+","+df['long1']
df.head(2)


# In[70]:


#Drop columns
df.drop(['Latitude','Longitude','Location','lat1','long1'],axis=1,inplace=True)
df.head(2)


# In[72]:


#Group by:
groupPT=df.groupby(['Primary Type']).count()
groupPT.head(2)


# In[76]:


#Sort function
sort_District=df.sort_values(by=['District'],ascending=True)
sort_District.head(2)
sort_DistrictRI=df.sort_values(by=['District'],ascending=True).reset_index()
sort_DistrictRI.head(2)
sort_DistrictRIDATE=df.sort_values(by=['Date'],ascending=True).reset_index()
sort_DistrictRIDATE.head(2)


# In[77]:


#Loop
case_number=[]
for i in df['Case Number']:
    case_number.append(i)
print(len(case_number))


# In[78]:


District=[]
Ward=[]
for d1,d2 in zip(df.District,df.Ward):
    District.append(d1)
    Ward.append(d2)
print(len(District),len(Ward))


# In[80]:


#DataFrame split by rows
df1=df.iloc[:200000]
df2=df.iloc[200001:]
print(df1.shape)
print(df2.shape)


# In[81]:


#Concat of dataframes
dffull=pd.concat([df1,df2])
print(dffull.shape)


# In[82]:


#Column splits
dfsptCOL1=df.iloc[:,:5]
dfsptCOL2=df.iloc[:,5:]
print(dfsptCOL1.shape)
print(dfsptCOL2.shape)


# In[83]:


#Join
joindfCOL=pd.concat([dfsptCOL1,dfsptCOL2],axis=1)
print(joindfCOL.shape)


# In[84]:


joindfCOL.columns


# In[87]:


#Change order of colunms
joindfCOL=joindfCOL[['Case Number', 'Date', 'Block', 'IUCR', 'Primary Type',
       'Description', 'Location Description', 'Arrest', 'Domestic', 'Beat',
       'District', 'Ward', 'Community Area', 'FBI Code', 'X Coordinate',
       'Y Coordinate', 'Year', 'Updated On', 'geo','ID']]
joindfCOL.columns
joindfCOL.shape


# In[89]:


#Save the file
joindfCOL.to_csv("Newdata.csv",index=False)

