#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) Verify if a value is an integer


# In[2]:


a=2
type(a)


# In[3]:


#2) Verify if a value is even


# In[4]:


a=3
a%2==0


# In[5]:


#3) Insert two numbers. Is the first is bigger than the second?


# In[1]:


num1=input('primeiro numero: ')


# In[2]:


type(num1)


# In[3]:


num1=int(num1)


# In[4]:


num2 = int(input("segundo numero: "))


# In[5]:


type(num2)


# In[6]:


num2=int(num2)


# In[7]:


num1>num2


# In[8]:


#4) Verify if one value is multiple of another


# In[9]:


num1=2
num2=4


# In[10]:


num1%num2==0 or num2%num1==0


# In[11]:


#5) Calculate the interest earn by an investor that invested an amount of capital of 200 during three years 
#with an interest rate of 3%


# In[12]:


capital=200
rate=0.03
time=3
interest=capital*rate*time


# In[13]:


print(interest)


# In[14]:


#6) Capital that an investor obtained after investing an amount of capital of 200 during three years with an 
#interest rate of 3%. (Compound interest)


# In[15]:


capital=200
rate=0.03
time=3
capitalAcum=capital*(1+rate)**time


# In[16]:


print(capitalAcum)


# In[17]:


#7) Calculate your BMI (Body Mass Index)


# In[18]:


M=68
H=1.76
BMI=M/(H**2)
print(BMI)


# In[19]:


#8) Calculate the Golden ration:


# In[20]:


#1. Solve the problem without using libraries
gr=(1+(5**(1/2)))/2
gr


# In[21]:


#2. Use module math (import math) and function sqr (math.sqrt)
import math
gr=(1+math.sqrt(5))/2
gr


# In[23]:


#9) Calculate the NPV (Net present value) of an investment, considering an initial 
#investment of 10000, the following
#Cashflows 2000,3000, 4000, 4000 and 5000 and a discount rate of 10%.


# In[24]:


I=10000
CF1=2000
CF2=3000
CF3=4000
CF4=4000
CF5=5000
rate=0.1


# In[28]:


NPV=((CF1/(1+rate)**1)+(CF2/(1+rate)**2)+(CF3/(1+rate)**3)+(CF4/(1+rate)**4)+(CF5/(1+rate)**5))-I
print(NPV)


# In[29]:


#10) Ask the user to insert name and age. Calculate the birth year. 
#Print a result saying the 'this person was born in.


# In[30]:


#1. Solve the problem without using modules and libraries


# In[31]:


#2. Solve the problem using the date library from module datetime
from datetime import date
name=input('Please insert yout name: ' )


# In[32]:


age=input('Please insert your age: ')


# In[38]:


today=date.today()
birthyear=today.year-int(age)
print(birthyear)


# In[40]:


birthyear=str(birthyear)


# In[41]:


print("This person was born in "+ birthyear)


# In[42]:


#11) Ask the user to insert forenames, surnames. Create a new variable (name) with your complete name


# In[43]:


# Create the following variables:
# nameBig - all the characters of the name are capitalized
# nameTitle - only the first character of each name (word) is capitalized
# nameSmall - all the characters of the name are lowercase.
# nameCapitalized - only the first character of the first name is capitalized


# In[44]:


name="Sofia da Conceição Gomes Guerreiro"
type(name)


# In[45]:


nameBig=print(name.upper())


# In[46]:


nameTitle=print(name.upper().title())


# In[47]:


nameSmall=print(name.lower())


# In[48]:


nameCapitalized=print(name.upper().capitalize())


# In[49]:


#12) Use the following method to show in which character appears the first "da"


# In[55]:


name="Sofia da Conceição Gomes Guerreiro"
name.find('da')


# In[ ]:




