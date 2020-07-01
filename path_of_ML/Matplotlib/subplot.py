#!/usr/bin/env python
# coding: utf-8

# In[15]:


import random
import matplotlib.pyplot as plt
from matplotlib import style


# In[16]:


style.use("fivethirtyeight")


# In[17]:


fig = plt.figure()


# In[18]:


def create_plots():
    xs = []
    ys = []
    
    for i in range(10):
        x = i
        y = random.randrange(10)
        
        xs.append(x)
        ys.append(y)
    return xs,ys
        


# In[19]:


# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(212)

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=2, colspan=1)
ax2 = plt.subplot2grid((6,1),(2,0),rowspan=2 ,colspan=1)
ax3 = plt.subplot2grid((6,1),(4,0),rowspan=2, colspan=1)


# In[20]:


x,y = create_plots()
ax1.plot(x,y)
x,y = create_plots()
ax2.plot(x,y)
x,y = create_plots()
ax3.plot(x,y)
plt.show()


# In[21]:





# In[22]:





# In[ ]:




