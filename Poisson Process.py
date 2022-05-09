#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import needed libries
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


# generating possion process with lambda > 0, up untile time T
def PoissonProcess(lam,T):
    timeCount = 0  # the total time that has elapsed after each arrival
    val = 0  # value of each poisson process
    Nt = [0]   # a list of values of poisson process
    times = [0]  # a list that contains the arrival times
    while(timeCount <= T):
        x = np.random.exponential(1/lam)
        timeCount = timeCount + x
        if(timeCount <= T):
            val = val + 1
            Nt.append(val)
            times.append(timeCount)
        if(timeCount > T):
            Nt.append(val)
            times.append(T)
    return Nt, times


# PoissonSim = PoissonProcess(1,10)  # simulate poisson process with lambda = 1 on the time interval [0,1]
# PoissonSim

# In[ ]:


# draw the poisson process
Nt = PoissonSim[0]
times = PoissonSim[1]
plt.plot(times, Nt, drawstyle='steps-post')


# In[5]:


# generating a compound possion process with lambda > 0, up untile time T
def CompoundPoissonProcess(lam,T,mu,sigma):
    timeCount = 0
    val = 0
    Nt = [0]
    times = [0]
    while(timeCount <= T):
        x = np.random.exponential(1/lam)
        timeCount = timeCount + x
        if(timeCount <= T):
            Z = np.random.normal(mu, sigma)
            val = val + np.exp(Z)
            Nt.append(val)
            times.append(timeCount)
        if(timeCount > T):
            Nt.append(val)
            times.append(T)
    return Nt, times


# In[ ]:


# plot the compound poisson process with lamda = 1,  mu = 0, sigma = 1 on the time interval [0,10]
CompoundPoissonSim = CompoundPoissonProcess(1,10,0,1)
CNt = CompoundPoissonSim[0]
Ctimes = CompoundPoissonSim[1]
plt.plot(Ctimes, CNt, drawstyle='steps-post')

