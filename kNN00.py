import math

#euclid distance
def dist(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# x, y training data,  k for k-NN
def pred(X_tr, Y_tr, k, test):
    #list to be returned
    preds=[]
    for i in range( len(test) ):
        #list of pairs (dist, j) measuring the distance between test[i] and X_tr[j]
        dist_meas = [ (dist(test[i],X_tr[idx]), idx) for idx in range(len(X_tr)) ] 
        #sort according to distance and take first k elements
        dist_sort = sorted(dist_meas)[:k]
        classes = {}
        #count classes to which the first k elements belong to
        for pair in dist_sort:
            idx = pair[1]
            if Y_tr[idx] in classes:
                classes[ Y_tr[idx] ] += 1
            else:
                classes[ Y_tr[idx] ] = 1    
        #sorts according to classes[x] which is the frequency of occurrence
        classes_sort = sorted([(classes[x],x) for x in classes], reverse=True)
        #first pair, second coordinate
        preds.append( classes_sort[0][1] )
    return preds

X_train = [[0,0], [1,1], [2,0], [2,1], [1,3],
           [8,4], [8,5], [7,5], [4,6], [4,7],
           [5,6], [6,3], [7,4], [3,2], [5,5], 
           [2,3], [3,5], [5,4], [6,2], [4,5],
           [6,1], [9,5]]
Y_train = [ 1, 1, 1, 1, 1,
            3, 3, 3, 2, 2,
            2, 3, 3, 1, 2,
            1, 2, 2, 3, 2,
            3, 3 ]

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

fig, ax = plt.subplots()
lcmap = ListedColormap(['red', 'blue', 'green'])


X_test = [[2,3],[2,2],[5,7],[4,4],[7,4]]
predicts = pred(X_train, Y_train, 3, X_test)


#import itertools
#t = [[i/20,j/20] for i in range(200) for j in range(200)]
#predicts2 = pred(X_train, Y_train, 3, t)
#ax.scatter([x[0] for x in t],[x[1] for x in t], c=predicts2, marker='.', cmap=lcmap)

ax.scatter([x[0] for x in X_train], [x[1] for x in X_train], c=Y_train)
ax.scatter([x[0] for x in X_test],[x[1] for x in X_test], c=predicts, s=200, marker='+')
plt.axis([0, 10, 0, 8])
plt.show()
