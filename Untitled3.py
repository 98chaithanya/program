#!/usr/bin/env python
# coding: utf-8

# In[9]:


def average(lst):
    return sum(lst)/len(lst)
lst=[15,9,14,10,30,27]
average=average(lst)
print("average of list=",round(average,1))


# In[11]:


x=5
y=10
print("before swapping")
print("value of x:",x ,"value of y:",y)
x,y=y,x
print("after swappnig")
print("value of x:",x,"value of y:",y)


# In[18]:


n=int(input("enter a number n:"))
temp=str(n)
t1=temp*2
t2=temp*3
result=n+int(t1)+int(t2)
print("value is:",result)


# In[23]:


n=int(input("enter the number n:"))
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reversed number is:",rev)


# In[24]:


n=int(input("enter a numer n:"))
if(n>0):
    print("numer is positive")
elif(n<0):
    print("number is negative")


# In[26]:


sub1=int(input("enter the mark of maths:"))
sub2=int(input("enter the mark of physics:"))
sub3=int(input("enter the mark of chemistry:"))
sub4=int(input("enter the mark of biology:"))
sub5=int(input("enter the mark of english:"))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if(avg>=90):
    print("grade:A+")
elif(avg>=80):
    print("grade:A")
elif(avg>=70):
    print("grade B+")
elif(avg>=60):
    print("grade B")
elif(avg>=50):
    print("grade C+")
elif(avg>=40):
    print("grade C")
elif(avg>=30):
    print("grade D")
        


# In[29]:


n=int(input("enter the number:"))
a=int(input("enter the strting range:"))
b=int(input("enter the ending range:"))
for i in range(a,b+1):
    if(i%n==0):
        print(i)
    


# In[36]:


a=int(input("enter the first number:"))
b=int(input("enter the second number"))
quotient=a//b
remainder=a%b
print("quotient is:",quotient)
print("remainder is:",remainder)


# In[40]:


a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])


# In[49]:


start=int(input("enter the first range:"))
end=int(input("enter the second range:"))
for num in range(a,end+1):
    if num %2!=0:
        print(num, end = " ")


# In[50]:


n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)


# In[52]:


n=int(input("Enter an integer:"))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("Smallest divisor is:",a[0])


# In[53]:


n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)


# In[54]:


n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


# In[57]:


max_num = 20
n = 1
print("Numbers not divisible by 2 and 3")
while n <= max_num:
    if n % 2 != 0 and n % 3 != 0:
        print(n)
    n = n+1


# In[58]:


def seriessum(n):
     
    sum = 0
    for i in range(1, n + 1):
        sum += i * (i + 1) / 2
    return sum
n = 4
print(seriessum(n))
 


# In[59]:


n=int(input("Enter a number: "))
for j in range(1,n+1):
    a=[]
    for i in range(1,j+1):
        print(i,sep=" ",end=" ")
        if(i<j):
            print("+",sep=" ",end=" ")
        a.append(i)
    print("=",sum(a))
 
print()


# In[60]:


n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()


# In[61]:


for i in range (n, 0, -1):
    print((n-i) * ' ' + i * '*')
    


# In[ ]:




