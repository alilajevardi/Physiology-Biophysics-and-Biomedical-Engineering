#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# generates a tophat function
def top_hat():
    t_hat = np.zeros(64)
    for i in range(0, 64):
        z = 16.**2 - (i-32.)**2
        if z > 0:
            t_hat[i] = 2*np.sqrt(z)
    return t_hat


# In[3]:


plt.plot(top_hat())
plt.show;


# In[4]:


# Ramachandran- Lakshminarayanan filter for back projection

def ramac_filter(p):
    p_star = np.zeros(64)
    
    for i in range(0,64):
        q = p[i] * 2.467401
        Jc = 1 + i%2
        for j in range(Jc,64,2):
            q = q -p[j] / (i-j)**2
        p_star[i] = q/(np.pi * 0.3333 * 50)
    return p_star


# In[5]:


y = ramac_filter(top_hat())
x = np.arange(0,64)


plt.plot(x, y)
plt.show;


# In[ ]:




