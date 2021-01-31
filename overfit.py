import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
x = [1, 2, 4, 5, 7]
y = [1, 2, 3, 5, 6]
p = interpolate.lagrange(x,y)
print(p)
xp = np.linspace(0,8,100)
yp = p(xp)
plt.scatter(x,y )
plt.plot(xp,yp,'k:')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
