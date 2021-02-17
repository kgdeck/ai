#
# k-Means Algorithmus
#   - ohne Vektorisierung/numpy
#   - plain-Python


from sklearn.datasets import make_blobs  # nur für Beispieldatensätze
import random
random.seed(19)
import matplotlib.pyplot as plt

# Quadrat der euklidschen Metrik
def dist_points( a, b ):
    return sum((x-y)**2 for x,y in zip(a,b))

def dist_array( x, y ):
    rc = 0.
    for i in range(len(x)):
        rc += dist_points( x[i], y[i] )
    return rc

# index i mit minimaler dist zwischen x und y[i]
def minidx( x, y ):
    min = 0
    d = dist_points( x, y[0] )
    for i in range(1, len(y)):
        d1 = dist_points( x, y[i] )
        if d1 < d:
            d = d1
            min = i
    return min

#
# hier geht's los
#

maxIterations = 100
k = 5

# generiert beispieldatensatz mit labels
X, labels = make_blobs(n_samples=200, centers=k, random_state=6)

plt.scatter(X[:, 0], X[:, 1], c=labels);
plt.title('Beispieldatensatz')
plt.show()

centers = [X[r] for r in random.sample( range(len(X)), k)]
cluster = [None for x in X]

count = 0
while count<maxIterations and (count==0 or dist_array(centers, old_centers)>0):
    count = count + 1
    old_centers = centers.copy()
    for i in range( len(X)):
        # gesucht: cluster j
        j = minidx( X[i], centers )
        cluster[i] = j        
    
    plt.scatter([x[0] for x in X], [x[1] for x in X], c=cluster )
    plt.scatter([x[0] for x in centers], [x[1] for x in centers], marker='+')
    plt.title('Iteration ' + str(count))
    plt.show()
    
    for c in range( k ):
        sum_x = 0
        sum_y = 0
        ct = 0
        for j in range( len(X) ):
            if cluster[j] == c:
                ct += 1
                sum_x += X[j][0]
                sum_y += X[j][1]
        centers[c] = [ sum_x/ct, sum_y/ct ]
    # fehlt die prüfung, ob irgendein Cluster leer. Dann Datensatz aus X, der dem (leeren) Cluster-Zentrum am nächsten kommt
    # (Frochte 2019, 310/311)

plt.scatter([x[0] for x in X], [x[1] for x in X], c=cluster )
plt.scatter([x[0] for x in centers], [x[1] for x in centers], marker='+')  
plt.title('Resultat')
plt.show()
print('Iterations: {0:d}'.format(count))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels, cluster))
