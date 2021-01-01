#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


#Create Series using List 
lst1=['VK','RS','MSD','SD','SR']
label=[1,2,3,4,5]
s1=pd.Series(index=label,data=lst1)
s1


# In[5]:


#Create Series using dict 
d={1:'VK',2:'RS',3:'MSD',4:'SD',5:'SR'}
s2=pd.Series(d)
s2


# In[6]:


np.random.rand(5,4)


# In[8]:


#Creating a dataframe
df1=pd.DataFrame(np.random.rand(5,4))
df1


# In[9]:


df2=pd.DataFrame(np.random.rand(5,4),[1,2,3,4,5],['VK','RS','MSD','SD'])
df2


# In[10]:


#Creating a dataframe
df3=pd.DataFrame(np.random.rand(5,4),['A','B','C','D','E'],['VK','RS','MSD','SD'])
df3


# In[11]:


df3.iloc[3]


# In[14]:


#Access row of a dataframe
df3.loc[['A','B']]


# In[16]:


df3


# In[18]:


#Access column of a dataframe
df3[['VK','SD']]


# In[19]:


df3['Total']=df3['VK']+df3['RS']+df3['MSD']+df3['SD']
df3


# In[20]:


#Create a new column with name="VK+SD"and val=df3['VK']+df3['SD']
df3['VK+SD']=df3['VK']+df3['SD']
df3


# In[21]:


#Create a new column with name="VK+SD+MSD" and val=df3['VK']+df3['SD']+df3['MSD']
df3['VK+SD+MSD']=df3['VK']+df3['SD']+df3['MSD']
df3


# In[22]:


df3['Total1']=df3['VK']+df3['RS']+df3['MSD']+df3['SD']
df3


# In[23]:


#Drop total1 column
df3.drop('Total1',axis=1,inplace=True)
df3


# In[25]:


df3.drop('VK+SD',axis=1,inplace=True)
df3


# In[26]:


#pick a single value
df3['VK']['A']


# In[28]:


#Conditional pick
df3[df3>0.5]


# In[29]:


df3


# In[30]:


#Pandas with CSV(Reading,storing.....)


# In[32]:


#Reading csv file using Pandas
df4=pd.read_csv("C:\\Users\\AMAN BIRADAR\\Downloads\\Python\\iris.csv")
df4


# In[33]:


#Find Nan value
df4.isnull()


# In[36]:


df3


# In[37]:


df3.to_csv("C:\\Users\\AMAN BIRADAR\\Downloads\\Python\\df3.csv")


# In[38]:


df4.columns


# In[39]:


#Group in pandas is used to group values to apply agg function
df4.groupby('species').sum()


# In[40]:


df4.groupby('species').min()


# In[41]:


df4.groupby('species').max()


# In[42]:


df4.groupby('species').mean()


# In[44]:


#DAY--2--PANDAS---#


# In[45]:


#Series object/Creating series in Pandas using list
l1=['VK','RS','MSD','SD','SR']
s1=pd.Series(data=l1)
s1


# In[47]:


#Series object/creating series in pandas using list
l1=['VK','RS','MSD','SD','SR']
lab=[1,2,3,4,5]
s1=pd.Series(data=l1,index='la')
s1


# In[48]:


#Series object/creating series in pandas using dict
d={1:'VK',2:'RS',3:'MSD',4:'SD',5:'SR'}
s2=pd.Series(d)
s2


# In[49]:


np.random.rand(5,4)


# In[51]:


#creating dataframe
df1=pd.DataFrame(np.random.rand(5,4))
df1


# In[53]:


#Creating Dataframe
df2=pd.DataFrame(np.random.rand(5,4),['A','B','C','D','E'],['VK','RS','MSD','SD'])
df2


# In[54]:


#Pick particular row from dataframe using index value 
df2.iloc[1]


# In[55]:


df2.loc['B']


# In[56]:


df2.loc[['A','B']]


# In[57]:


#Picking single columns


# In[58]:


df2['VK']


# In[59]:


#Picking multiple columns
df2[['VK','RS']]


# In[60]:


#creating new column
df2['Total']=df2['VK']+df2['RS']+df2['MSD']+df2['SD']
df2


# In[64]:


#Student task:create 5 different columns
df=pd.DataFrame(np.random.rand(5,5),['Running','Jumping','Swiming','Skiping','Reading'],['Ram','Shyam','Rita','Georg','Carl'])
df


# In[65]:


df2


# In[66]:


#drop'Total' from dataframe
df2.drop('Total',axis=1,inplace=True)
df2


# In[69]:


#Reading CSV File-----------------
df3=pd.read_csv("C:\\Users\\AMAN BIRADAR\\Downloads\\Python\\iris.csv")
df3


# In[70]:


print(type(df3))


# In[71]:


df3.isnull().any()


# In[72]:


df3.info()


# In[73]:


df3.describe()


# In[74]:


df3.head(5)


# In[76]:


df3.to_csv("C:\\Users\\AMAN BIRADAR\\Downloads\\Python\\df3.csv")
print("File is saved....!!!")


# In[77]:


#------GROUP BY----------------
#It is group values to apply aggrt.functions count,min,max,mean,sum


# In[78]:


df3.groupby('species').min()


# In[80]:


df3.groupby('species').max()


# In[81]:


df3.groupby('species').mean()
#Observation--If PL and PW are very less than flew is setosa

