#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1) Construct a list (shoppingList) including 'potatoes', 'carrots', 'cod' and 'sprouts’


# In[2]:


shoppingList=['potatoes','carrots','cod','sprout']


# In[3]:


type(shoppingList)


# In[4]:


#2) Get the second and the last element of the list


# In[5]:


shoppingList[1] 


# In[6]:


shoppingList[-1] 


# In[7]:


#3) Iterate though the list


# In[8]:


for purchase in shoppingList:
    print(purchase)


# In[9]:


#4) Create a new list (studentList)


# In[10]:


studentList=[]


# In[11]:


#5) Add the follwoing elements to the shoppingList: orange and lime


# In[12]:


shoppingList.append('orange')
shoppingList.append('lime')


# In[13]:


print(shoppingList)


# In[14]:


#6) Remove the carrots, the first element and last element of the shoppingList list


# In[15]:


shoppingList.remove('carrots')


# In[16]:


del shoppingList[0]


# In[17]:


del shoppingList[-1]


# In[18]:


print(shoppingList)


# In[19]:


#ou
#shoppingList.pop(1)
#shoppingList.pop(0)
#shoppingList.pop()


# In[20]:


#7) Delete the shoppingList list


# In[21]:


del shoppingList
print(shoppingList)


# In[22]:


#8) Create a list with the double values of all integer number between 1 and 15.


# In[28]:


numberList=[x**2 for x in range (1,16)]
print(numberList)


# In[29]:


#9) Obtain the first 3 elements of the list


# In[30]:


firstThree = numberList [: 3]
print(firstThree)


# In[31]:


#10) What is the result of, Why?


# In[32]:


shoppingList=['potatoes','carrots','cod','sprout']


# In[33]:


shopping = shoppingList   
shoppingListCopy = shoppingList[:]
print(shopping)


# In[34]:


#passa a haver duas listas em que as duas têm os mesmos elementos
#shoppingList[:] returns a copy of the whole sequence


# In[35]:


#12) What is the result of, Why?


# In[36]:


shoppingList=['potatoes','carrots','cod','sprout']
shopping = shoppingList
shoppingList.append("orange")
print(shopping)


# In[37]:


#orange was added to the shoppingList
#adicionou apenas à shoppingList mas a shopping tambem ficou afetada


# In[38]:


#13) Remove all the items from the shoppingList


# In[39]:


shoppingList=['potatoes','carrots','cod','sprout']
shoppingList.clear()
print(shoppingList)


# In[40]:


#shoppingList ficou vazia


# In[41]:


#14) What is the result of, Why?


# In[42]:


newPurchases= ("bananas", "beans", "rice")
print (newPurchases [1])
newPurchases [0] = "apple"


# In[43]:


### resposta: os tuples sao imutáveis logo dá erro


# In[44]:


#15) Create a dictionary including the follwoing elements: orange, apple, pear, grape and peach. 
#Key are 1 to 5. Iterate through key-value pair.


# In[45]:


fruit={1:'orange',2:'apple',3:'pear',4:'grape',5:'peach'}


# In[46]:


for key, value in fruit.items():
    print("The fruit " + str(key) +" is " + value)


# In[47]:


#16) Create a weekList that is composed of several lists, each one corresponding to a day.


# In[48]:


weekList1=[1,2,3]
weekList2=[4,5,6]
weekList3=[7,8,9]
weekList=[weekList1, weekList2, weekList3]
print(weekList)


# In[ ]:




