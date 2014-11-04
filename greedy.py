# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 13:26:43 2014

@author: liuyi103
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pulp as pp


g=nx.DiGraph()
pos={}
sell={}
sw=0
vol={}
p={}
for i in range(100):
    g.add_node(i)
    sell[i]=np.random.randint(0,2)
    pos[i]=np.random.rand(2)
    vol[i]=np.random.rand(1)*5+1
    p[i]=np.random.rand(1)
for i in range(100):
    for j in range(100):
        if sell[i]==1 and sell[j]==0 and np.sum((pos[i]-pos[j])**2)<0.1 and p[i]<p[j]:
            g.add_edge(i,j)


for i in range(100):
    for j in range(i):
        if g.has_edge(i,j) or g.has_edge(j,i):
            tmp=float(min(vol[i],vol[j]))
            if tmp<1:
                continue
            vol[i]-=tmp
            vol[j]-=tmp
            sw+=tmp*abs(p[i]-p[j])
print sw

