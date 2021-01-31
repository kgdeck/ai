#SP specifity, SE sensitivity, PV prevalence


#pos.pred.value
def ppv( sp, se, pv ):
    return (se*pv)/(se*pv + (1-pv)*(1-sp))

#neg.pred.value
def npv( sp, se, pv ):
    return (sp*(1-pv))/(1-(se*pv + (1-pv)*(1-sp)))

def ppv_npv( sp, se, pv ):
    return ppv( sp, se, pv ), npv( sp, se, pv )

se = 0.8
sp = 0.8
pv = 0.01
print( ppv_npv( sp, se, pv ))


import matplotlib.pyplot as plt
xa = [x*0.01 for x in range(100)]

a = [ppv(sp,se,x) for x in xa]
b = [npv(sp,se,x) for x in xa]
plt.plot(xa, a, 'r')  
plt.plot(xa, b, 'b') 
plt.show()
