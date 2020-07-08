#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


# In[3]:


style.use('fivethirtyeight')


# In[6]:


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


# In[7]:


def animate(i):
    graph_data = open("example.txt","r").read()
    lines = graph_data.split("\n")
    xs = []
    ys = []
    for line in lines:
        if len(line)> 1:
            x, y = line.split(",")
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs,ys)


# In[ ]:


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

