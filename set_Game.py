# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:46:37 2017

@author: slim
"""

import itertools
### definition les cartes 
cartes=[]
j=0
for i1 in range(3):
    for i2 in range(3):
        for i3 in range(3):
            for i4 in range(3):
                j=j+1
                cartes=cartes+[[j,[i1,i2,i3,i4]]]
def collection(x):
    
    for j in range(4):
        s=0
        for i in range(3):
            s=s+x[i][1][j]
        if not (s%3==0):
            return False 
    return True 
collections=[]
for i in itertools.combinations(cartes, 3):
    if collection(i):
        collections=collections+[sorted(list(i),key=lambda variable: variable[0])]
number=[0,0,len(collections)]
        
if True:
    collections_2=[]
    for j in collections:
        print (j[0][0])
        for c in cartes:
            if c not in collections_2:
                e=sorted(j+[c],key=lambda variable: variable[0])
                if e not in collections_2:
                    collections_2.append(e)
    collections=collections_2