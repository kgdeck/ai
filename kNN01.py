import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
 
np.random.seed(33)

def distance(x1, x2):
    return np.sqrt(np.sum((x1-x2)**2))

def predict(X_train, Y_train, k, X_test):
        
        # list to store all our predictions
        preds = []
        
        # loop over all observations in the test set
        for i in range(len(X_test)):            
            
            # calculate the distance between the test point and all other points in the training set
            #dist = np.array([distance(X_test[i], x_t) for x_t in X_train])
            x = [(dist(X_test[i],X_train[idx]), idx) for idx in range(len(X_train))]
            
            dist_sorted = sorted(x)[:k]
            
            # get the neighbors
            neighbors = {}
 
            # for each neighbor find the class
            for pair in dist_sorted:
                idx = pair[1]
                if Y_train[idx] in neighbors:
                    neighbors[Y_train[idx]] += 1
                else:
                    neighbors[Y_train[idx]] = 1
            
            sorted_nb_ct = sorted([(neighbors[k],k) for k in neighbors], reverse=True)
            preds.append( sorted_nb_ct[0][1] )
            
        return preds

data,target = make_classification(n_samples=300, n_classes=2)
X_train, X_test, Y_train, Y_test = train_test_split(data, target, test_size=0.2)
preds = predict(X_train, Y_train, 10, X_test )

print('Accuracy:', accuracy_score(Y_test, preds))
print(confusion_matrix(Y_test, preds))

#import matplotlib.pyplot as plt
#fig, ax = plt.subplots()
#ax.scatter([x[0] for x in X_train], [x[1] for x in X_train], c=Y_train)
#ax.scatter([x[0] for x in X_test],[x[1] for x in X_test], c=preds, s=200, marker='+')
#plt.show()
