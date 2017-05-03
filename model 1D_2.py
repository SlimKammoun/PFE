# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:06:35 2017

@author: slim
"""

import numpy as np
import  matplotlib.pyplot as pl
from sklearn import linear_model

### dimentions 1 

### paramètres 
n=500 # nombre d'échantillion 
pas=10 
L=2000  # temps_max
Lambda =0.2 #paramètre poisson
(m,p) = (10,0.5) #paramètres binomial
beta=50 #parametre exponentielle  1/lambda
q=1-p
sd_poisson =[]
sd_binomial=[]
sd_exonentiel=[]
for T in range (5,L,pas):
    print T
    H=[]
    for i in range(n):
        s=0 
        h=[0,0,0,0,0]
        while (True):
            s += np.random.poisson(Lambda)
            if s>T:
                break
            h[np.random.randint(3)]+=1
        H.append(max(h))
    sd_poisson.append( np.log(np.std(H)))

X=[np.log(TT) for TT in range(5,L,pas)]
regr = linear_model.LinearRegression()
regr.fit(np.array(X).reshape(-1,1),sd_poisson)
Y=[regr.intercept_+regr.coef_*np.log(TT) for TT in range(5,L,pas)]
pl.plot(X,sd_poisson,label='poisson, lambda='+str(Lambda))
pl.plot(X,Y,label='y='+str(regr.intercept_)[:5]+'+'+str(regr.coef_[0])[:5]+'log(t)')
pl.legend()
