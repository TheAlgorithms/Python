import numpy as np 
import pandas as pd 	

'''P(Y|X) = (P(X|Y)* P(Y))/P(X) #Bayes Theorem  
We are gonna ignore P(X), as it does not depend on Y and hence has no role in optimising P(Y|X), 
since we are more concerned with relative values of probabilities of classes rather than actual probability of classes

likelihood : P(X = x1,x2,x3 | Y)
prior : P(Y)
posterior : P(Y|X )'''

def prior_prob(Y_train, target): 
    # Calculating P(Y)
    return np.sum(Y_train ==target)/float(Y_train.shape[0])

def cond_prob(X_train,Y_train, feature_col, feature_val, target):

    # Calculating P(X|Y) for all X's that belong to a given Y
    X_train =X_train[Y_train ==target]
    numerator = np.sum(X_train[:,feature_col]==feature_val) #Sum of all the values that have X corresponding to Y
    denominator = np.sum(Y_train == target )
    
    return numerator/ float(denominator) #P(X|Y)

def predict (X_train, Y_train, X_test):
    classes = np.unique(Y_train)
    
    n_feat =X_train.shape[1] #columns
    post_prob =[]
    
    for target in classes: 
        likelihood =1.0 #initialising
        
        for f in range(n_feat):
            conditional_prob = cond_prob(X_train, Y_train, f, X_test[f], target)
            #Since P(x1|Y) is independent of P(x2|Y) so, we are just going to ,multiply the terms P(x1|Y)...
            likelihood *= conditional_prob
            
        prior = prior_prob(Y_train, target)
        
        posterior = likelihood*prior
        post_prob.append(posterior)
        
    pred =np.argmax(post_prob) #returns the indices of max posterior probability ; basically the class with max probability, hence the predicted class
    
    return pred