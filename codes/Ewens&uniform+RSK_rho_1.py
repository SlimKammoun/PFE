# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 13:35:59 2017

@author: mkammoun.lct
"""

import numpy as np
import  matplotlib.pyplot as pl
from bisect import bisect
import math
n=200
n2=10000


def per(theta,n):
    perm=[]
    for i in range(1,n+1):
        if np.random.binomial(1,theta/(float(theta)+i-1))==1:
            perm.append(i)
        else:
            j=np.random.randint(i-1)
            k=perm[j]
            perm[j]=i
            perm.append(k)
    return perm

per(0.1,1000)    
def RSK(p):
    '''Given a permutation p, spit out a pair of Young tableaux'''
    P = []; Q = []
    def insert(m, n=0):
        '''Insert m into P, then place n in Q at the same place'''
        for r in range(len(P)):
            if m > P[r][-1]:
                P[r].append(m); 
                return
            c = bisect(P[r], m)
            P[r][c],m = m,P[r][c]
        P.append([m])
        return P

    for i in range(len(p)):
        insert(int(p[i]), i+1)
    return map(len,P)



def pointspos(per):
    rsk=RSK(per)
    return [rsk[i]-i-1  for i in range(len(rsk)) if (rsk[i]-i -1) >=0]
pointspos([1,2,3])
## seulement les points entre [-3 rac(n) et  3 rac(n)]
alea1={}
alea2={}
for i in range(int(3*n**0.5)+1):
    alea1[i]=0
    alea2[i]=0     


for j in range(n2):
    per_unif=np.random.permutation(range(1,np.random.poisson(n)+1))
    per_ewens=per(0.1,np.random.poisson(n))
    print j
    p1=pointspos(per_unif)
    p2=pointspos(per_ewens)
    for i in p1 :
        if i<3*n**0.5:
            alea1[i]+=1
    for i in p2 :
        if i<3*n**0.5:
            alea2[i]+=1
x=range(int(3*n**0.5+1))
a1=np.array([alea1[i]for i in x])/float(n2)
a2=np.array([alea2[i]for i in x])/float(n2)
x2=np.array(range(int(1000*2*n**0.5+1)))/1000
a3=np.array(np.arccos(np.array(x2)/(2*n**0.5)))/math.pi
pl.plot(x,a1,"*",label="uniform")
pl.plot(x,a2,"+",label="Ewens")
pl.plot(x2,a3,label="approximation sinus")
pl.legend()