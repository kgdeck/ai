#Ringbeispiel - from the scratch

def mean( a ):
    if len(a)==0: return 0
    return sum(a)/len(a)

#funktioniert für listen und für np.arrays
def lin_koeff( x, y ):
    mn_x = mean( x )
    mn_y = mean( y )
    z = 0. #zaehler
    n = 0. #nenner
    length = len(x)
    for i in range(length):
        z += (x[i]-mn_x) * (y[i]-mn_y)
        n += (x[i]-mn_x)**2
    b = z/n
    a = mn_y - b*mn_x
    return a, b

#funktioniert nur für np.arrays
def lin_koeff_np( x, y ):
    mn_x = mean( x )
    mn_y = mean( y )
    z = sum( np.multiply(x-mn_x, y-mn_y) )
    n = sum( np.multiply(x-mn_x, x-mn_x) )
    b = z/n
    a = mn_y-b*mn_x
    return a, b
    
col_x = [156,158,160,179,156,165,165,166,156,167,160,175,170,155]
col_y = [ 47, 46, 49, 53, 48, 49, 50, 48, 47, 51, 48, 52, 50, 46]

a, b =lin_koeff( xx, yy )
print( a, b )

print( 'Testvergleich: ', mean(col_y), a+b*mean(col_x)) # (mean_x, mean_y) liegen auf der Geraden

import numpy as np
xx = np.array(col_x)
yy = np.array(col_y)
print( lin_koeff_np( xx, yy ) )
