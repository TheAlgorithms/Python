import numpy as np
import sys

class NeuralNetMLP():
    """Feedforward neural network/MLP classifier."""
    def __init__(self, n_hidden=30, l2=0,epochs=100, eta=0.001, shuffle=True,minibatch_size=1, seed=None):
         self.n_hidden = n_hidden
         self.l2 = l2
         self.epochs = epochs
         self.eta = eta
         self.shuffle = shuffle
         self.minibatch_size = minibatch_size
         self.random = np.random
     
    def _onehot(self, y, n_classes):
        """Encode class labels with One-Hot encoding"""
        onehot = np.zeros((n_classes, y.shape[0]))
        for idx, val in enumerate(y.astype(int)):
            onehot[val, idx] = 1
        return onehot.T
    
    def _sigmoid(self, z):
        """Compute sinmoid function"""
        return 1/(1+np.exp(-np.clip(z, -250, 250)))

    def _forward(self, X):
        """ Compute forward propagation step"""
        # Hidden layer
        z_h = np.dot(X, self.w_h) + self.b_h
        a_h = self._sigmoid(z_h)
        # Output layer
        z_out = np.dot(a_h, self.w_out) +  self.b_out
        a_out = self._sigmoid(z_out)
        return z_h, a_h, z_out, a_out

    def _compute_cost(self, y_enc, output):
        """Compute (Logistic Loss)cost function"""
        #Regularization term
        L2_term = self.l2*(np.sum(self.w_h**2)+np.sum(self.w_out**2))
        #Logistic loss + regularizer
        cost = np.sum(-y_enc*(np.log(output))-((1-y_enc)*np.log(1-output))) + L2_term
        return cost

    def predict(self, X):
        """Predict the class label"""
        z_h, a_h, z_out, a_out = self._forward(X)
        y_pred = np.argmax(z_out, axis=1)
        return y_pred

    def fit(self, X_train, y_train, X_valid, y_valid):
        """Learn weights from training data"""
        n_output = np.unique(y_train).shape[0]
        n_features = X_train.shape[1]

        #Weights initialization - Hidden layer
        self.b_h = np.zeros(self.n_hidden)
        self.w_h = self.random.normal(loc=0, scale=0.1,size=(n_features, self.n_hidden))

        #Weights initialization - output layer
        self.b_out = np.zeros(n_output)
        self.w_out = self.random.normal(loc=0, scale=0.1,size=(self.n_hidden, n_output))

        epoch_strlen = len(str(self.epochs))
        self.eval_ = {'cost': [], 'train_acc': [], 'valid_acc': []}

        y_train_enc = self._onehot(y_train, n_output)

        #Iterate over training epochs
        for i in range(self.epochs):
            indices = np.arange(X_train.shape[0])
            if self.shuffle:
                self.random.shuffle(indices)
            #Iterate over mini-batches
            for start_idx in range(0, indices.shape[0]-self.minibatch_size+1, self.minibatch_size):
                batch_idx = indices[start_idx:start_idx+self.minibatch_size]

                #Forward propagation
                z_h, a_h, z_out, a_out = self._forward(X_train[batch_idx])

                #Back propagation
                delta_out = a_out - y_train_enc[batch_idx]
                sigmoid_derivative_h = a_h*(1-a_h)
                delta_h = (np.dot(delta_out, self.w_out.T)*sigmoid_derivative_h)

                grad_w_h = np.dot(X_train[batch_idx].T, delta_h)
                grad_b_h = np.sum(delta_h, axis=0)
                
                grad_w_out = np.dot(a_h.T, delta_out)
                grad_b_out = np.sum(delta_out, axis=0)

                #Regularization and weight updates
                delta_w_h = grad_w_h + self.l2*self.w_h
                delta_b_h = grad_b_h

                self.w_h -= self.eta*delta_w_h
                self.b_h = self.eta*delta_b_h

                delta_w_out = grad_w_out+self.l2*self.w_out
                delta_b_out = self.eta*grad_b_out
                
                self.w_out -= self.eta*delta_w_out
                self.b_out = self.eta*delta_b_out

                # ------ Evaluation after each epoch --------
                z_h, a_h, z_out, a_out = self._forward(X_train)
                cost = self._compute_cost(y_enc=y_train_enc,output=a_out)
                y_train_pred = self.predict(X_train)
                y_valid_pred = self.predict(X_valid)
                
                train_acc = ((np.sum(y_train ==y_train_pred)).astype(np.float) / X_train.shape[0])
                valid_acc = ((np.sum(y_valid ==y_valid_pred)).astype(np.float) /X_valid.shape[0])
                sys.stderr.write('\r%0*d/%d | Cost: %.2f | Train/Valid Acc.: %.2f%%/%.2f%% '%(epoch_strlen, i+1, self.epochs,cost,train_acc*100, valid_acc*100))              
                sys.stderr.flush()
                self.eval_['cost'].append(cost)
                self.eval_['train_acc'].append(train_acc)
                self.eval_['valid_acc'].append(valid_acc)
            
            return self