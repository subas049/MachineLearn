#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats as stats


# In[3]:


import seaborn as sns


# In[48]:


tips = sns.load_dataset('tips')


# In[56]:


tips = tips[:22]
tips


# In[59]:


tips.describe()

Mean (mu) == 20 -- H0
mean (mu) != 20 -- HA
# In[61]:


stats.ttest_1samp(tips['total_bill'], popmean=22, alternative="less")


# In[25]:


import numpy as np
SE = 6.320880/np.sqrt(22)


# In[26]:


(18.436818 - 15) / SE


# In[51]:


tips_female = tips[tips['sex'] == 'Female']
tips_male = tips[tips['sex'] == 'Male']


# In[52]:


print(tips_female.shape)
print(tips_male.shape)

H0 == female totalbill mean and male totalbill mean is equal 
HA : female totalbill mean and male totalbill mean is not equal
# In[53]:


stats.ttest_ind(tips_female['total_bill'], tips_male['total_bill'])


# In[54]:


import matplotlib.pyplot as plt


# In[55]:


plt.boxplot(tips_female['total_bill'])


# In[ ]:




