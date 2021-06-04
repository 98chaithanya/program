#!/usr/bin/env python
# coding: utf-8

# In[2]:


numberset={1,2,3,46,7,3,}
print(numberset)


# In[3]:


empty_set={}
print(type(empty_set))


# 

# In[4]:


empty_set= set()
print(type(empty_set))


# In[5]:


my_set={1.0,"hello",(1,2,3)}
print(my_set)


# In[7]:


set_with_lists=set([1,2,3])
print(type(set_with_lists))
print(set_with_lists)


# In[13]:


my_set=set()
my_set.update([9,12])
my_set.update((3,5))
my_set.update("SIKANDER")

print(my_set)


# In[14]:


A={1,2,3,4,5,6,7}
B={3,4,6,8,4,5,7}
print('union=',A|B)
print('intersection=',A&B)
print('difference=',A-B)
print('symmetric difference=',A^B)


# In[4]:


studentList={'danish','jaison','sangeetha','uma','amritha''lohitha','prasad','aswathi'}
placedstudentList={'sangeetha','uma','amritha''lohitha'}
notplacedstudentList=set(studentList)-set(placedstudentList)
print("student yet to get job\n",notplacedstudentList)


# In[ ]:




