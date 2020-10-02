#!/usr/bin/env python
# coding: utf-8

# In[1]:


#list of 007 movies where Sean Connery features James Bond
moviesSeanConnery = ["Dr. No (1962)",
"From Russia with Love (1963)",
"Goldfinger (1964)",
"Thunderball (1965)",
"You Only Live Twice (1967)",
"Diamonds Are Forever (1971)",
"Never Say Never Again (1983)"] 


# In[2]:


#list of 007 movies where David Neven features James Bond
moviesDavidNeven=["Casino Royale (1967)"] 


# In[3]:


#list of 007 movies where George Lazenby features James Bond
moviesGeorgeLazenby=["On Her Majesty's Secret Service (1969)"] 


# In[4]:


#list of 007 movies where Roger Moore features James Bond
moviesRogerMoore=[ "Live and Let Die (1973)",
"The Man with the Golden Gun (1974)",
"The Spy Who Loved Me (1977)",
"Moonraker (1979)",
"For Your Eyes Only (1981)",
"Octopussy (1983)",
"A View to a Kill (1985)"]


# In[5]:


#list of 007 movies where Timothy Dalton features James Bond
moviesTimothyDalton=[
"The Living Daylights (1987)",
"Licence to Kill (1989)"
]


# In[6]:


#list of 007 movies where Pierce Brosnan features James Bond
moviesPierceBrosnan=[
"GoldenEye (1995)",
"Tomorrow Never Dies (1997)",
"The World Is Not Enough (1999)",
"Die Another Day (2002)"
]


# In[7]:


#list of 007 movies where Daniel Craig features James Bond
moviesDanielCraig=["Casino Royale (2006)",
"Quantum of Solace (2008)",
"Skyfall (2012)",
"Spectre (2015)"]


# In[8]:


# 1) Create a list of lists (movies007). The list will be composed by each list of movies featured 
#by each actor.


# In[9]:


movies007=[]
movies007.append(moviesSeanConnery)
movies007.append(moviesDavidNeven)
movies007.append(moviesGeorgeLazenby)
movies007.append(moviesRogerMoore)
movies007.append(moviesTimothyDalton)
movies007.append(moviesPierceBrosnan)
movies007.append(moviesDanielCraig)
print(movies007)


# In[10]:


#2) How many movies were played by the first actor to play James Bond?


# In[11]:


len(moviesSeanConnery)


# In[12]:


#3) How many movies were played by the last actor to play James Bond?


# In[13]:


len(moviesDanielCraig)


# In[14]:


#4) How many actors played the role of James Bond?


# In[15]:


len(movies007)


# In[16]:


#5) Create a new list with the number of movies played by each actor


# In[18]:


nActor=[len(moviesSeanConnery),len(moviesDavidNeven),len(moviesGeorgeLazenby),len(moviesRogerMoore),len(moviesTimothyDalton),len(moviesPierceBrosnan),len(moviesDanielCraig)]
print(nActor)


# In[19]:


#6) How many movies were played by the actor who appeared most often in movies?


# In[20]:


max(nActor)


# In[21]:


#7) How many movies were played by the actor who appeared in fewer movies?


# In[22]:


min(nActor)


# In[23]:


#8) Create a new list (movies007a) with all the films.


# In[24]:


movies007a=[]
movies007a.extend(moviesSeanConnery)
movies007a.extend(moviesDavidNeven)
movies007a.extend(moviesGeorgeLazenby)
movies007a.extend(moviesRogerMoore)
movies007a.extend(moviesTimothyDalton)
movies007a.extend(moviesPierceBrosnan)
movies007a.extend(moviesDanielCraig)
print(movies007a)


# In[25]:


#9) Sort the elements of the list


# In[27]:


movies007a.sort()
print(movies007a)


# In[28]:


#9) Reverse the order of the list. What will happen if this method is executed twice? 
#Does this method sort the list if it is not sorted?


# In[29]:


movies007a.reverse()
print(movies007a)


# In[30]:


movies007a.reverse()
print(movies007a)


# In[31]:


##Resposta: yes, doing reverse twice will get us back to the original list, in this case, the sorted one


# In[32]:


#10) What is the index of the movie "Spectre (2015)" in the list of movies


# In[33]:


movies007a.index("Spectre (2015)")


# In[34]:


#11) Add the movie "007 and the bad Guy of the climate change (2020)" in the 11th position.


# In[36]:


movies007a.insert(10,"007 and the bad Guy of the climate change (2020)")
print(movies007a)


# In[37]:


#12) It was a mistake. Remove the movie "007 and the bad Guy of the climate change (2020)"


# In[39]:


movies007a.remove("007 and the bad Guy of the climate change (2020)")
print(movies007a)


# In[ ]:




