#!/usr/bin/env python
# coding: utf-8

# In[8]:


import point
import generator
import time


# In[9]:


t1 = time.time()


# In[14]:


n = 10000000
inct = LCG(1, 1103515245, 12345, pow(2,32),1000)
x_in = []
y_in = []
x_out = []
y_out = []
orig = inct.give_sequence()
l = []
for i in orig:
    a = i/inct.modulus
    l.append(a)

# In[12]:

number = 0
for j in range(1,n):
    x = inct.give_next_random_number()
    x = 2*(x/inct.modulus) - 1
    y = inct.give_next_random_number()
    y = 2*(y/inct.modulus) - 1
    pt = rectangle(x,y)    
    if pt.distance_from_origin() <= 1:
        number += 1
        x_in.append(x)
        y_in.append(y)
    else:
        x_out.append(x)
        y_out.append(y)


# In[ ]:



# In[ ]:
print(number)

ratio = number/n

print('Ratio :', ratio)


# In[ ]:





# In[ ]:





# In[ ]:


print("Time Taken : " , (time.time() - t1))

