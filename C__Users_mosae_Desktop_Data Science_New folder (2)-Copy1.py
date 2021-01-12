#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')[0]
df


# In[3]:


df.drop(df[df.Borough=='Not assigned'].index,inplace=True)
df.shape
df


# In[6]:


df1=pd.read_csv(r'C:\Users\mosae\Downloads\Geospatial_Coordinates.csv')
df1


# In[26]:



df_row = pd.concat([df, df2])
df_row


# In[30]:


df.join(df1.set_index('Postal Code'), on='Postal Code')


# In[ ]:




