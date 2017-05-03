# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:29:36 2017

@author: slim
"""
import numpy as np
import  matplotlib.pyplot as pl

n=1000
n2=4000
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
def attente(sec):
        att=[]
        for i in range(len(sec)):
            s=0
            for j in range(i):
                if sec[i]>sec[j]:
                    s=max(s,att[j])
            att.append(s+1)        
        return max(att)
res=[]
for j in range (n2):
    a=per(0.1,n)
    res.append(attente(a))
    print j
import TracyWidom as TW
cl=TW.TracyWidom(beta=2)
x=np.array(range(100*min(res)-200,100*(max(res))+200))/100.0
y=n2*cl.cdf((x-2*n**0.5)/n**(1.0/6) )
y2=n2*cl.pdf((x-2*n**0.5)/n**(1.0/6))/n**(1.0/6)
pl.hist(res, range = (min(res)-2, max(res)+2), bins=max(res)-min(res)+5,label='Histogramme des effectif')
pl.plot(x,y,label='Repartition:Tracy-widom ')
pl.plot(x,y2,label='Distribution:Tracy-widom ')
x=range(min(res),max(res))
y=[len([ j for j in res if j<=i]) for i in x ]
pl.plot(x,y,'b*',label='ECC plus longues sous-suite croissante')
pl.legend(bbox_to_anchor=(1.1, 0.8), loc=2, borderaxespad=0.)
