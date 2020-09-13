#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[40]:


# time = 20 second in 40 steps
t = np.linspace(0., 20, 40)


# In[41]:


# Initial values

L = 20.
w = 500.
Qb = 150.
Qd = 500.
b0 = 100.


# In[42]:


alpha = 0.05*(1/Qb - 1/Qd)
Z = np.exp(-alpha*w*L)/Qd - 1/Qb
b = b0*(np.exp(-alpha*w*L)/Qd - np.exp(-alpha*w*t)/Qb)/Z
d = b0*(np.exp(-alpha*w*L)/Qd - np.exp(-alpha*w*t)/Qd)/Z


# In[43]:


plt.plot(t, b, 'r', t, d, 'b')
plt.show()


# In[44]:


beta = 0.05*((1/Qb) + (1/Qd));
d1 = b0*Qd*(1 - np.exp(-beta*w*t))/(Qb + Qd);
b1 = d1 + b0*np.exp(-beta*w*t);


# In[45]:


plt.plot(t, b1, 'r', t, d1, 'b')
plt.show()


# In[ ]:




