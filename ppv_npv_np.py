import matplotlib.pyplot as plt
#einfacher mit numpy
import numpy as np

#SP specifity, SE sensitivity, PV prevalence

#pos.pred.value
def ppv( sp, se, pv ):
    return (se*pv)/(se*pv + (1-pv)*(1-sp))

#neg.pred.value
def npv( sp, se, pv ):
    return (sp*(1-pv))/(1-(se*pv + (1-pv)*(1-sp)))
    
se = 0.8
sp = 0.8

xa = np.linspace(0, 1, 100)

u = ppv(sp,se,xa) 
v = npv(sp,se,xa) 
plt.plot(xa, u, 'g')  
plt.plot(xa, v, 'y') 
plt.show()
