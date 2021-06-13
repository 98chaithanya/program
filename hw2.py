#!/usr/bin/env python
# coding: utf-8

# In[1]:


ch = input("Please Enter Your Own Character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is Not an Alphabet")


# In[5]:



X = [[1,2,3],  
[4,5,6],  
[7,8,9]]  
Y = [[11,12,13],  
[14,15,16],  
[17,18,19]]  
result = [[0,0,0],  
[0,0,0],  
[0,0,0]]    
for i in range(len(X)):
    for j in range(len(X[0])):  
        result[i][j] = X[i][j] + Y[i][j]  
for r in result:  
    print(r)  


# In[7]:


def add(x, y):  
    return x + y 
def subtract(x, y):
    return x - y 
def multiply(x, y): 
    return x * y 
def divide(x, y): 
    return x / y  
print("Select operation.")  
print("1.Add")  
print("2.Subtract")  
print("3.Multiply")  
print("4.Divide")  
  
choice = input("Enter choice(1/2/3/4):")  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2))  
else:  
   print("Invalid input")  


# In[8]:


a=[]
if len(a)==0:
    print ("list is empty")
else:
    print ("list is not empty")


# In[15]:


list=[45,67,68,76,85,96]
print("list:",list)
list.reverse()
print("reversed list is:",list)


# In[ ]:




