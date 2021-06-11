#!/usr/bin/env python
# coding: utf-8

# In[1]:


list=["A","B","c","D","E"]
list[0],list[4]=list[4],list[0]
print(list)


# In[2]:


num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)    


# In[10]:


d={'A':1,'B':2,'C':3}
key=int(input("Enter key to check:"))
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")


# In[17]:


def pyramid(p):
   for m in range(0, p):
      for n in range(0, m+1):
         print("* ",end="")
      print("\r")
p = 10
pyramid(p)


# In[16]:


n = 0
r = 12
for m in range(1, r+1):
   for gap in range(1, (r-m)+1):
      print(end=" ")
   while n != (2*m-1):
      print("* ", end="")
      n = n + 1
   n = 0
   print()


# In[ ]:




