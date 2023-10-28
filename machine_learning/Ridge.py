import numpy as np
from numpy import linalg as la
import time as t

class RidgeRegression() :
  
    def __init__( self, learning_rate, iterations, l2_penality ) :
        self.objvals = []

        # no_of_training_examples, no_of_features        
        self.m, self.n = X.shape

        # weight initialization        
        self.W = np.zeros( self.n )

        self.b = 0        
        self.X = X        
        self.Y = Y

        # gradient descent learning

        for i in range( self.iterations ) :
            Y_pred = self.predict( self.X )
            hh = self.objval(Y,Y_pred,X)

            start = t.time()            
            self.update_weights()
            end = t.time() - start
            self.timeiter.append(end)
            Y_pred = self.predict( self.X )
            hj = self.objval(Y,Y_pred,X)
            self.objvals.append(hh)
            if(abs(hh-hj)<=0.0001e-05):
              break

        time_g1 = (self.timeiter)
        time_iterg1 = time_g1.copy()
        time_iterg1.sort(reverse=True)
        self.timeiter = time_iterg1
        return self

    # Helper function to update weights in gradient descent

    def update_weights( self ) :           
        Y_pred = self.predict( self.X )

        # calculate gradients      
        dW = ( - ( 2 * ( self.X.T ).dot( self.Y - Y_pred ) ) +               
               ( 2 * self.l2_penality * self.W ) ) / self.m     
        db = - 2 * np.sum( self.Y - Y_pred ) / self.m 

        # update weights    
        self.W = self.W - self.learning_rate * dW    
        self.b = self.b - self.learning_rate * db        
        return self

    # Hypothetical function  h( x ) 
    def predict( self, X ) :    
        return X.dot( self.W ) + self.b

    def objval(self ,Y,pred,X):
      h_1 = sum( (Y - pred )**2)
      h_2 = la.norm( self.W,2 )**2
      h_3 = self.l2_penality*h_2
      h = h_3/self.m
      return h
