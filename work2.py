#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_date = input("Enter a date : ")
dd,mm,yy = my_date.split('/')
dd=int(dd)
mm=int(mm)
yy=int(yy)
if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
   max_val = 31
elif(mm==4 or mm==6 or mm==9 or mm==11):
   max_val = 30
elif(yy%4==0 and yy%100!=0 or yy%400==0):
   max_val = 29
else:
   max_val = 28
if(mm<1 or mm>12 or dd<1 or dd> max_val):
   print("The date is invalid")
elif(dd==max_val and mm!=12):
   dd=1
   mm=mm+1
   print("The incremented date is : ",dd,mm,yy)
elif(dd==31 and mm==12):
   dd=1
   mm=1
   yy=yy+1
   print("The incremented date is : ",dd,mm,yy)
else:
   dd=dd+1
   print("The incremented date is : ",dd,mm,yy)


# In[2]:


principle_amt = float(input("Enter the principle amount..."))
my_time = int(input("Enter the time in years..."))
my_rate = float(input("Enter the rate..."))
my_simple_interest=(principle_amt*my_time*my_rate)/100
print("The computed simple interest is :")
print(my_simple_interest)


# In[4]:


year = int(input("Enter a year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} is a leap year".format(year))  
       else:  
           print("{0} is not a leap year".format(year))  
   else:  
       print("{0} is a leap year".format(year))  
else:  
   print("{0} is not a leap year".format(year))  


# In[5]:


cm=int(input("Enter the height in centimeters:"))
inches=0.394*cm
feet=0.0328*cm
print("The length in inches",round(inches,2))
print("The length in feet",round(feet,2))


# In[6]:


celsius=int(input("Enter the temperature in celcius:"))
f=(celsius*1.8)+32
print("Temperature in farenheit is:",f)


# In[7]:


n=int(input("Enter an integer:"))
print("Factors are:")
i=1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1


# In[8]:


n=int(input("Enter an integer:"))
print("The divisors of the number are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i)


# In[9]:


n=int(input("Enter the number to print the tables for:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)


# In[10]:


n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
sum1=0
sum2=0
sum3=0
for j in b:
    if(j>0):
        if(j%2==0):
            sum1=sum1+j
        else:
            sum2=sum2+j
    else:
        sum3=sum3+j
print("Sum of all positive even numbers:",sum1)
print("Sum of all positive odd numbers:",sum2)
print("Sum of all negative numbers:",sum3)


# In[11]:


n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
c=[]
d=[]
for i in b:
    if(i%2==0):
        c.append(i)
    else:
        d.append(i)
c.sort()
d.sort()
count1=0
count2=0
for k in c:
    count1=count1+1
for j in d:
    count2=count2+1
print("Largest even number:",c[count1-1])
print("Largest odd number",d[count2-1])


# In[12]:


n=int(input("Enter the number:"))
tmp=n
k=0
while(n>0):
    k=k+1
    n=n//10
b=str(tmp)
c=str(k)
d=c+b[k-1]
print("The new number formed:",int(d))


# In[13]:


lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
for i in range (lower,upper+1):
    if(i%7==0 and i%5==0):
        print(i)


# In[15]:


n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")


# In[16]:


n=int(input("Enter number of rows: "))
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()


# In[17]:


n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")


# In[18]:


sum1=0
num=int(input("Enter a number:"))
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum1=sum1+f
    num=num//10
if(sum1==temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")


# In[19]:


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1=min1+1


# In[1]:


def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
  
a = 60
b = 48
  
# prints 12
print("The gcd of 60 and 48 is : ", end="")
print(hcf(60, 48))


# In[3]:


import math
print("Enter the coefficients of the form ax^3 + bx^2 + cx + d")
lst=[]
for i in range(0,4):
    a=int(input("Enter coefficient:"))
    lst.append(a)
x=int(input("Enter the value of x:"))
sum1=0
j=3
for i in range(0,3):
    while(j>0):
        sum1=sum1+(lst[i]*math.pow(x,j))
        break
    j=j-1
sum1=sum1+lst[3]
print("The value of the polynomial is:",sum1)


# In[4]:


x=int(input('Enter number 1: '))
y=int(input('Enter number 2: '))
sum1=0
sum2=0
for i in range(1,x):
    if x%i==0:
        sum1+=i
for j in range(1,y):
    if y%j==0:
        sum2+=j
if(sum1==y and sum2==x):
    print('Amicable!')
else:
    print('Not Amicable!')


# In[5]:


import math
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is: ",round(area,2))


# In[7]:


m1=float(input("Enter the first mass: "))
m2=float(input("Enter the second mass: "))
r=float(input("Enter the distance between the centres of the masses: "))
G=6.673*(10**-11)
f=(G*m1*m2)/(r**2)
print("Hence, the gravitational force is: ",round(f,2),"N")


# In[8]:


num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  


# In[9]:


lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[10]:


def printno(upper):
    if(upper>0):
        printno(upper-1)
        print(upper)
upper=int(input("Enter upper limit: "))
printno(upper)


# In[11]:


import math
def sin(x,n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return sine
x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
print(round(sin(x,n),2))


# In[12]:


import math
def cosine(x,n):
    cosx = 1
    sign = -1
    for i in range(2, n, 2):
        pi=22/7
        y=x*(pi/180)
        cosx = cosx + (sign*(y**i))/math.factorial(i)
        sign = -sign
    return cosx
x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
print(round(cosine(x,n),2))


# In[13]:


n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)


# In[14]:


n=int(input("Enter the number of terms: "))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print("The sum of series is",round(sum1,2))


# In[1]:


n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
sum1=1
for i in range(2,n+1):
    sum1=sum1+((x**i)/i)
print("The sum of series is",round(sum1,2))


#  import math
# n=int(input("Enter the number of terms: "))
# sum1=1
# for i in range(1,n+1):
#     sum1=sum1+(1/math.factorial(i))
# print("The sum of series is",round(sum1,2))

# In[ ]:


import math
n=int(input("Enter the number of terms: "))
sum1=1
for i in range(1,n+1):
    sum1=sum1+(1/math.factorial(i))
print("The sum of series is",round(sum1,2))


# In[ ]:


import math
n=int(input("Enter the number of terms: "))
sum1=1
for i in range(1,n+1):
    sum1=sum1+(1/math.factorial(i))
print("The sum of series is",round(sum1,2))


# In[1]:


a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
k=0
num=int(input("Enter the number to be counted:"))
for j in a:
    if(j==num):
        k=k+1
print("Number of times",num,"appears is",k)


# In[2]:


def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
 
 
n = int(input('Enter n: '))
print('Number of set bits:', count_set_bits(n))


# In[3]:


def is_power_of_two(n):
    """Return True if n is a power of two."""
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0
 
 
n = int(input('Enter a number: '))
 
if is_power_of_two(n):
    print('{} is a power of two.'.format(n))
else:
    print('{} is not a power of two.'.format(n))


# In[4]:


def clear_rightmost_set_bit(n):
    """Clear rightmost set bit of n and return it."""
    return n & (n - 1)
 
 
n = int(input('Enter a number: '))
ans = clear_rightmost_set_bit(n)
print('n with its rightmost set bit cleared equals:', ans)


# In[5]:


def get_gray_codes(n):
    """Return n-bit Gray code in a list."""
    if n == 0:
        return ['']
    first_half = get_gray_codes(n - 1)
    second_half = first_half.copy()
 
    first_half = ['0' + code for code in first_half]
    second_half = ['1' + code for code in reversed(second_half)]
 
    return first_half + second_half
 
 
n = int(input('Enter the number of bits: '))
codes = get_gray_codes(n)
print('All {}-bit Gray Codes:'.format(n))
print(codes)


# In[6]:


def binary_to_gray(n):
    """Convert Binary to Gray codeword and return it."""
    n = int(n, 2) # convert to int
    n ^= (n >> 1)
 
    return bin(n)[2:]
 
 
g = input('Enter binary number: ')
b = binary_to_gray(g)
print('Gray codeword:', b)


# In[ ]:




