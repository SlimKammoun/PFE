# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 22:10:01 2017

@author: slim
"""
import numpy as np
import  matplotlib.pyplot as pl
### dimentions 1 

### paramètres 
n=50000 # nombre d'échantillion 
pas=1 
L=1000  # temps_max
Lambda =10 #paramètre poisson
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
        h=-1
        while (s<T):
            s += np.random.poisson(Lambda)
            h=h+1
        H.append(h)
    sd_poisson.append( np.log(1+np.std(H)*Lambda)/np.log(T))
    H=(np.array(H)-T/Lambda)
    H=[]
    for i in range(n):
        s=0 
        h=-1
        while (s<T):
            s += np.random.binomial(m,p)
            h=h+1
        H.append(h)
    sd_binomial.append( np.log(1+np.std(H)*(m*p)**1.5/(m*p*q)**0.5)/np.log(T))
    H=(np.array(H)-T/(n*p))
    print( np.log(1+np.std(H)*(m*p)**1.5/(m*p*q)**0.5)/np.log(T))
    H=[]
    for i in range(n):
        s=0 
        h=-1
        while (s<T):
            s += np.random.exponential(beta)
            h=h+1
        H.append(h)
    sd_exonentiel.append( np.log(1+np.std(H)*(beta)**0.5)/np.log(T))
    H=(np.array(H)-T/(n*p))

X=[np.log(TT) for TT in range(5,L,pas)]
Y=[0.5 for TT in range(5,L,pas)]
pl.plot(X,sd_binomial,label='binomiale(10,0.5)')
pl.plot(X,sd_poisson,label='poisson, lambda=10')
pl.plot(X,sd_exonentiel,label='exp, lambda=1/50')
pl.plot(X,Y,label='y=1/2')
pl.legend()
