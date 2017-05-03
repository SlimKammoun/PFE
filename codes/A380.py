# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:55:46 2017

@author: slim
"""

import  matplotlib.pyplot as pl
import numpy as np
import TracyWidom as TW
import math
from multiprocessing import Pool
p = Pool(4)
c=[]
cx=[]
s343=[(i,j)  for i  in range(45,51)+range(52,66)+range(68,79)+range(81,88) for j in['A','B','C','D','E','F','G','H','J','K'] ]
s303=[(i,j)  for i  in range(41,45)+[79,80,88] for j in['A','B','C','H','j','K'] ]
s040=[(i,j)  for i  in range(41,45) for j in['D','E','F','G'] ]
s242=[(i,j)  for i  in [67] for j in['B','C','D','E','F','G','H','J'] ]
s003=[(i,j)  for i  in [66] for j in['H','J','k'] ]
sieges=s343+s303+s040+s242+s003

def attend(a,b):
        col1=['A','B','C','D','E']
        col2=['F','G','H','I','J']
        c1= a[0]>=b[0]
        c11=a[1]in col1 and b[1]in col1
        c12=a[1]in col2 and b[1]in col2
      
        return c1 and (c11 or c12) 
def attente(sec):
        att=[]
        for i in range(len(sec)):
            s=0
            for j in range(i):
                if attend(sec[i],sec[j]):
                    s=max(s,att[j])
            att.append(s+1)        
        return max(att)
def cdf(x):
    return cl.cdf(x)**2
def pdf(x):
    return (cdf(x+0.001)-cdf(x-0.001))*1000/2    
def moy():
    return sum([x*pdf(x) for  x in np.array(range (-1000,1000))/100.0])/100.0
##    cl=TW.TracyWidom(beta=2)
n1=len(sieges)    
n=10000
cl=TW.TracyWidom(beta=2)
print moy()
res=[attente(np.random.permutation(sieges)) for i in xrange(n)]
correction = (moy()*(n1/2.0)**(1.0/6)+math.sqrt(2*n1))/np.average(res)
pl.hist(res, range = (min(res)-2, max(res)+2), bins=max(res)-min(res)+5,label='Histogramme simulation A380')
x=np.array(range(100*min(res)-200,100*(max(res))+200))/100.0
y=n*cdf((x*correction-(2*n1)**0.5)/(n1/2.0)**(1.0/6) )
y2=n*pdf((x*correction-(2*n1)**0.5)/(n1/2.0)**(1.0/6))/(n1/2.0)**(1.0/6)
pl.plot(x,y,label='Repartition:F2^2 ')
pl.plot(x,y2,label='Distribution:F2^2 ')
x=range(min(res),max(res))
y=[len([ j for j in res if j<=i]) for i in x ]
pl.plot(x,y,'b*',label='FCC simulation A380')
pl.legend(bbox_to_anchor=(1.1, 0.8), loc=2, borderaxespad=0.)


## estimation 