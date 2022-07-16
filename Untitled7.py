#!/usr/bin/env python
# coding: utf-8

# In[62]:


#exo1 :
l1 = [2,3,6]
x = 1
for i in l1 :
    x = x * i
print(x)


# In[61]:


#exo2 :
l2 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l2.sort(key=lambda tup: tup[1])
print(l2)


# In[40]:


#exo3 :
d1 = {'a': 100, 'b': 200, 'c':300}

d2 = {'a': 300, 'b': 200, 'd':400}

d3 = {}
for key in d2:   #looking if the key exist in both dictionaries 
    if key in d1:
        d3[key] = d2[key]+d1[key]
    else :
        d3[key] = d2[key]   #if the key in d1 is not in d2  we add d2 into d3
for key in d1 :   
    if key in d2 :
        pass
    else :
        d3[key] = d1[key] #if the key in d2 is not in d1 we add d1 into d3

        
print(d3)


# In[63]:


#exo4 :
n = int(input())
l3={}
for i in range (1,n+1) :
    l3[i] = i*i

print(l3)


# In[60]:


#exo5 :
list1= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(list1 ,key=lambda x: float(x[1]), reverse=True))


# In[ ]:




