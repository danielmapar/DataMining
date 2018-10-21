#!/usr/bin/env python
# coding: utf-8

# In[68]:


import sys
import math
import statistics
import csv 


# In[69]:


def z_score(values):
    
    avg = statistics.mean(values)
    N = len(values)
    
    std = math.sqrt((1/(N-1))* sum([math.pow((x - avg), 2) for x in values]))
    
    norm_vals = []
    
    norm_vals = [(val - avg)/(std) for val in values]
    
    return norm_vals


# In[73]:


#file = open(sys.srgv[1])

file = open("input.txt")

data = [] 
out = []
for line in file:
    data.append([ float(x) for x in line.split()])

num_cols = len(data[0])

for i in range(num_cols):
    column = [x[i] for x in data]
    out.append(z_score(column))
    
out = zip(*out)


# In[74]:


with open('output.txt', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerows(out)


# In[ ]:




