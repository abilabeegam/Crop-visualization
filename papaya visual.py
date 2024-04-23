#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("final_crop_dataset.csv")
df


# In[14]:


g = df.groupby('Crop')
g


# In[8]:


for Crop, Crop_df in g:
    print (Crop)
    print (Crop_df)


# In[22]:


p = g.get_group('Papaya')
p.set


# In[21]:


p.plot()


# In[ ]:




