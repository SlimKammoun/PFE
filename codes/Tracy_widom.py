# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:08:17 2017

@author: slim
"""

import TracyWidom as TW
import numpy as np
import  matplotlib.pyplot as pl
## creation de la classe
cl=TW.TracyWidom(beta=2)
## choix des points x (-5 à 2) par pas de 0.001
X=(np.array(range(7000))-5000)/1000.0
## fonction de repartition
Y=cl.cdf(X)
### densité
Y2=cl.pdf(X)
rep,=pl.plot(X,Y,label='fonction de repartition')
den,=pl.plot(X,Y2,'r',label='densite')
pl.legend(handles=[rep, den])
pl.legend(bbox_to_anchor=(0.03, 0.98), loc=2, borderaxespad=0.)


pl.show()



n= 400
x=np.array(range(int((n)**0.5),3*int((n)**0.5)))
y=cl.cdf((x-2*n**0.5)/n**(1.0/6))
y2=cl.pdf((x-2*n**0.5)/n**(1.0/6))
pl.plot(x,y)
pl.plot(x,y2)