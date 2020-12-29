# Hierarchisches Clustering - Beispiel einer from-the-scratch Implementierung 
#   Python basic, 2-dim, ohne numpy, ohne Vektorisierung
#

import math
import matplotlib.pyplot as plt

#Euklidsche Metrik (2-dim)
#
def dist(x, y):
    return math.sqrt( (x[0]-y[0])**2 + (x[1]-y[1])**2)

#Schwerpunkte der Cluster
#
#  Beispiel: clusters = [[p_1, p_2, p_3], [p_4, p_5], [p_6, p_7, p_8], [p_9]] , p_i aus R x R    (4 cluster)
#                         
#            return     [       c_1,          c2,            c3,         c4 ], cendroid pro cluster
#
def centroids( clusters ):
    rc = [None for c in clusters]
    for i in range(len(clusters)):
        sum_x = 0
        sum_y = 0
        n=0
        for x in X:
            if x in clusters[i]:
                sum_x += x[0]
                sum_y += x[1]
                n += 1
        if n>0 :
            sum_x /= n
            sum_y /= n
        rc[ i ] = [sum_x, sum_y]
    return rc

#
#  ermittelt i, j, d  mit  i<j und d = |cs[i], cs[j]| minimal (und (i,j) minimal)
#
def mindist( cs ):
    if len(cs)<=1: return -1, -1, 0
    
    for i in range( len(cs) ):
        for j in range( i+1, len(cs) ):
            d_n = dist( cs[i], cs[j] )
            if (i==0 and j==1) or d_n < d:
                rc_i = i
                rc_j = j
                d = d_n
    return rc_i, rc_j, d

#Testdaten
X = [[14,15],
     [18,14],
     [60,78],
     [24,10],
     [30,30],
     [85,70],
     [71,80],
     [70,55],
     [10,80],
     [15,75]]

#Plot
labels = range(1, len(X)+1)
plt.figure(figsize=(10, 7))
plt.subplots_adjust(bottom=0.1)
plt.scatter([x[0] for x in X], [x[1] for x in X], label='True position')
for label, x, y in zip(labels, [x[0] for x in X], [x[1] for x in X]):
    plt.annotate( label, xy=(x, y), xytext=(-3, 3), textcoords='offset points', ha='right', va='bottom')
plt.show()

#
# hier beginnt 'main'
#every x builds a cluster    
clusters = [ [X[i]] for i in range(len(X))]
print( clusters )
count = 0
while len(clusters)>1 and count<len(X):
    count += 1
    clusters_centroids = centroids( clusters )
    i,j,d = mindist( clusters_centroids )
    #merge cluster i and j
    c_m = clusters[i] + clusters[j]
    print( '{:3d} {:5.2f} {:s} + {:s} -> {:s}'.format(count,d,str(clusters[i]),str(clusters[j]),str(c_m)) )
    clusters[i] = None
    clusters[j] = None
    clusters[i] = c_m
    del clusters[j]
    print( clusters )
    
