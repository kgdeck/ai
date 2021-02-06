#euclid distance
def dist(v1, v2):
    z = sum( (x1-x2)**2 for x1, x2 in zip(v1, v2))
    return z ** 0.5

# x, y training data,  k for k-NN
def predict(X_tr, Y_tr, k, to_predict):
    preds = []
    for p in to_predict:
        #dist_meas = [ [dist(p, X_tr[i] ), Y_tr[i] ] for i in range(len(X_tr))]
        dist_meas = [ [dist(p, x1 ), y1 ] for x1, y1 in zip(X_tr, Y_tr)]
        dist_sort = sorted( dist_meas )
        dist_sort_k = dist_sort[:k]
        cls = {}
        for _, c in dist_sort_k:
            if c in cls: cls[ c ] += 1
            else:       cls[ c ] = 1
        cl_sorted = sorted([[cls[c], c] for c in cls], reverse=True)
        preds.append( cl_sorted[0][1] )
    return preds

X_train = [[0,0], [1,1], [2,0], [2,1], [1,3],
           [8,4], [8,5], [7,5], [4,6], [4,7],
           [5,6], [6,3], [7,4], [3,2], [5,5], 
           [2,3], [3,5], [5,4], [6,2], [4,5],
           [6,1], [9,5], [9,4]]
Y_train = [ 1, 1, 1, 1, 1,
            3, 3, 3, 2, 2,
            2, 3, 3, 1, 2,
            1, 2, 2, 3, 2,
            3, 3, 2 ]

X_pred = [[2,3],[2,2],[5,7],[4,4],[7,4], [9,4]]

predicts = predict( X_train, Y_train, 4, X_pred )

import matplotlib.pyplot as plt
plt.scatter([x[0] for x in X_train], [x[1] for x in X_train], c=Y_train)
plt.scatter([x[0] for x in X_pred],[x[1] for x in X_pred], c=predicts, s=400, marker='+')
plt.axis([0, 10, 0, 8])
plt.show()
