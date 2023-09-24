#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#String, Integer, float, boolean
# List [] , tuples ()


# In[ ]:


word: definition


# In[ ]:


key: value


# In[ ]:


a_dict = { key1 : value1, key2: value2}


# In[24]:


a_dict = {'Name': 'Ramakrishna', 
          'Age': 30, 
          40: '432413',
          'Gender' : 'Male', 
          'salary': 150000}
a_dict


# In[2]:


print(type(a_dict))


# In[3]:


a_dict['Name']
# a_dict[key]


# In[4]:


a_dict['Gender']


# In[5]:


a_dict['gender']


# In[12]:


a_dict['city'] = 'Pune'
a_dict


# In[7]:


del a_dict['Gender']


# In[8]:


a_dict


# In[9]:


del a_dict


# In[13]:


a_dict


# In[15]:


b_dict = {'1': 'a',
          2: 'b',
          3: 'c'}
b_dict


# In[25]:


a_dict.keys() # Return keys 


# In[19]:


a_dict.values() # returns elements or objects


# In[22]:


list(a_dict.values())


# In[26]:


c_dict = {'Name': ['Rama','Gnana','Amirta'],
         'Age':[24,25,26]}
c_dict


# In[28]:


c_dict['Age']


# In[29]:


d_dict = {[1,2,3]: 'a'}
d_dict


# In[31]:


a_dict.items() # returns list of tuples


# In[32]:


list(a_dict.items())


# In[33]:


a_dict['Name']


# In[34]:


a_dict['Bank']


# In[38]:


a_dict.get('Bank', 'dsdfdsfs')


# In[39]:


a_dict.get('Name', 'dsdfdsfs')


# In[44]:


d_dict = dict(1 = [10,20,30],
              2 = ['aas','fsd']) ---> not allowed key as integers


# In[50]:


d_dict = dict(Name = [10,20,30], Country = ['aas','fsd'])
d_dict


# In[45]:


a_dict


# In[46]:


b_dict = {'Bank': 'HDFC', 'PAN': 'EEEEC4343G', 'IFSC':232132321}


# In[47]:


a_dict.update(b_dict) # Updating first dict with a second dict.


# In[48]:


a_dict


# In[51]:


len(a_dict)


# In[56]:


dict1 = {'Name': 'Rama',
         2 : '20', 
         'Name': 'Manni'}
dict1 # Duplicates keys are not allowed? 


# In[61]:


del dict1


# In[62]:


len(dict1)


# In[57]:


len(dict1)


# In[58]:


dict1.clear()


# In[59]:


dict1


# In[60]:


len(dict1)


# ## Sets

# In[64]:


# Collection of elements/values -- unique


# In[67]:


a_set = {1,2,3,40,40, 50, 50,50,60,70,80}
a_set


# In[66]:


type(a_set)


# In[69]:


a_list = [10,20,20,30,40,40,40,40,50,60,70,70,80]
len(a_list)


# In[71]:


len(set(a_list)) # finding a unique element in a list/object .. it is useful.


# In[72]:


b_set = {40,50,60,100,120}


# In[74]:


a_set, b_set


# In[75]:


a_set.intersection(b_set) # common elements from both the sets.


# In[76]:


a_set.union(b_set) # Unique elements from both the sets


# In[77]:


a_set.difference(b_set) # return elements of set1 which are not present in set2


# In[78]:


b_set.difference(a_set)


# In[79]:


a_set.symmetric_difference(b_set) # return uncommon elements from both the sets.


# In[ ]:


# Conditions
# If-else 


# In[81]:


x = 2
print(x)


# In[85]:


x == 2


# In[ ]:


if condition:
    print('Ramakrishna')
    printerefdsdsfds
    dsfsdfds
    sdfdsfsd
    sfsdfsdf
    sdffsd
dasdsddsa    
    


# In[92]:


if x == 3:
    print('value of x is 2')
    print('inside the IF condition')
print('X has a different value')


# In[93]:


if x==4:
    print('value of x is 4')
else:
    print('value of x is not 4')


# In[95]:


x = 15

if x==4:
    print('value of x is 4')
elif x==5:
    print('value of x is 5')
elif x>=6:
    print('value of x is >6')
else:
    print('value of x is <4 ')


# In[ ]:





# In[ ]:





# In[90]:


print('X has a different value')


# In[ ]:





# In[ ]:




