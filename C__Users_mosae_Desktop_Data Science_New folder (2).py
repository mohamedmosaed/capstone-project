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


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




