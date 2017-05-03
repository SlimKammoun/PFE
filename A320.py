# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:55:46 2017

@author: slim
"""

import  matplotlib.pyplot as pl
import numpy as np
import TracyWidom as TW
import math

sieges=[(i,j)  for i  in range(1,31) for j in['A','B','C','D','E','F'] ]
def attend(a,b):
    c1= a[0]>=b[0]
   ## c11=a[1]in['A','B','C'] and b[1]in['A','B','C']
    ##c12=a[1]in['E','F','G'] and b[1]in['E','F','G']
   ## c2= a[0]>b[0]
    return c1 
def attente(sec):
    att=[]
    for i in range(len(sec)):
        s=0
        for j in range(i):
            if attend(sec[i],sec[j]):
                s=max(s,att[j])
        att.append(s+1)        
    return max(att)

cl=TW.TracyWidom(beta=2)
n1=len(sieges)    
n=100
res=[attente(np.random.permutation(sieges)) for i in xrange(n)]
correction = (-1.771086807411*n1**(1.0/6)+2*math.sqrt(n1))/np.average(res)
pl.hist(res, range = (min(res)-2, max(res)+2), bins=max(res)-min(res)+5,label='Histogramme simulation A320')
x=np.array(range(100*min(res)-200,100*(max(res))+200))/100.0
y=n*cl.cdf((x*correction-2*n1**0.5)/n1**(1.0/6) )
y2=n*cl.pdf((x*correction-2*n1**0.5)/n1**(1.0/6))/n1**(1.0/6)
pl.plot(x,y,label='Repartition:Tracy-widom ')
pl.plot(x,y2,label='Distribution:Tracy-widom ')
x=range(min(res),max(res))
y=[len([ j for j in res if j<=i]) for i in x ]
pl.plot(x,y,'b*',label='FCC simulation A320')
pl.legend(bbox_to_anchor=(1.1, 0.8), loc=2, borderaxespad=0.)
