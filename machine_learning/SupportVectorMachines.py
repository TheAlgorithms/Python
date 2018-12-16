"""
Implementation of both Linear and Non-Linear Support Vector Machines.

************************* Linear SVMs *********************************

Input: - Data = List of tuples (vector, label), label = '1' or '-1'
       - C = Upper Bound C (numerical)

Output: - A trained Linear SVM is created which can:
          - Be evaluated by calling 'evaluate(Data)'.
          - Predict a single vector by calling 'predict(s)'.
          - Print Training info by calling 'getInfo()'.

***********************************************************************

************************** Non-Linear SVMs ****************************

Input: - Data = List of tuples (vector, label), label = '1' or '-1'
       - C = Upper Bound C (numerical)
       - Kernel = Kernel Function "RBF" or "Polynomial"
       - gamma: Parameter gamma

Output: - A trained Linear SVM is created which can:
          - Be evaluated by calling 'evaluate(Data)'.
          - Predict a single vector by calling 'predict(s)'.
          - Print Training info by calling 'getInfo()'.

***********************************************************************

**************************** Modules Needed ***************************

- numpy: for matrix operations.
- cvxopt: for Quadratic Programming.

***********************************************************************

****************************** Info ***********************************

- SVM is the parent class of both LinearSVM and NonLinearSVM classes,
  which both contain a constructor, 'predict', 'evaluate' and 'getInfo'.
  Each class object constitutes a Support Vector Machine.

- All other functions outside of the classes, except 'generateDataset',
  are used for the training of the Support Vector Machines.
  
- 'generateDataset' is used for a quick demonstration of the Support Vector Machines.

***********************************************************************

"""




import math
import numpy as np
import time
import random
from cvxopt import matrix as c_matrix
from cvxopt import solvers as c_solvers

    
class SVM():
    
    def __init__(self, Data, C):    
        self.x = np.array([x[0] for x in Data]) # Each row of the matrix represents a Vector Xi
        self.y = np.array([float(y[1]) for y in Data]) # Each cell of the vector represents a scalar Yi  
        self.C = C
        
    def evaluate(self, Data):
        
        print("\nEvaluating for %d Points..."%(len(Data)))
        correct = 0
        
        for sample in Data:
            data, label = sample[0], sample[1]
            if self.predict(data) == label:
                correct += 1
        
        acc = correct*100/len(Data)
        print("Accuracy: %.2f%%"%(acc))
        return acc
    
    def getInfo(self):      
        
        print("\n%d Support Vectors:\n"%(len(self.SupportVectors) - 1))
        i = 1
        while i < len(self.SupportVectors):
            print("\tSupport Vector #%d: %s, alpha = %.2f"%(i, self.SupportVectors[i][0], self.alphas[i]))
            i += 1
            
        print("\nBias: %.2f"%self.b)
        print("Upper Bound C: %.2f"%self.C)
            
        

class LinearSVM(SVM):
    
    def __init__(self, Data, C):   
        print("\nTraining Linear SVM for %d points in %d dimensions..."%(len(Data), len(Data[0][0])))
        startTime = time.time()
        super().__init__(Data, C)   
        self.alphas, self.SupportVectors = getAlphas(self.x, self.y, self.C, None, 0)
        self.w = getWeightVector(self.SupportVectors, self.alphas)
        self.b = getBias(self.SupportVectors, self.w)
        t = time.time() - startTime
        
        if t <= 60:
            print("Training completed in %d seconds."%int(t))
        else:
            minutes, seconds = t/60, t % 60
            print("Training completed in %d minutes and %d seconds."%(minutes, seconds))
        
    
    def predict(self, s):
        
        v = (self.w @ s) + self.b
        
        if v >= 0:
            return 1
        else:
            return -1
        
    def evaluate(self, Data):
        return super().evaluate(Data)
        
    def getInfo(self):
        super().getInfo()
        print("Weight Vector: %s"%self.w)
        

class NonLinearSVM(SVM):
    
    def __init__(self, Data, C, Kernel, gamma):   
        print("\nTraining Non-Linear SVM for %d points using %s Kernel Function..."%(len(Data), Kernel))
        startTime = time.time()
        super().__init__(Data, C)    
        self.Kernel, self.gamma = Kernel, gamma
        self.alphas, self.SupportVectors = getAlphas(self.x, self.y, self.C, Kernel, gamma)
        self.b = getKernelBias(self.SupportVectors, self.alphas, Kernel, gamma)
        
        t = time.time() - startTime
        if t <= 60:
            print("Training completed in %d seconds."%int(t))
        else:
            minutes, seconds = t/60, t % 60
            print("Training completed in %d minutes and %d seconds."%(minutes, seconds))
        
    
    def evaluate(self, Data):
        return super().evaluate(Data)


    def predict(self, s):
        
        SVX, SVY = self.SupportVectors[:, 0], self.SupportVectors[:, 1]
        
        v = self.b

        for i in range(len(SVY)):
            v += self.alphas[i]*SVY[i]*KernelFunction(SVX[i], s, self.Kernel, self.gamma)       
         
        if v >= 0:
            return 1
        else:
            return -1       
        
    def getInfo(self):
        super().getInfo()
        print("Kernel Function: %s"%self.Kernel)
        print("gamma: %s"%self.gamma)


def getAlphas(X, Y, C, Kernel, gamma):
    """
    'c_solvers.qp' minimizes the problem: (1/2)*(a.T)*H*a + (q.T)*a,
    for vector a, under the constraints: (1*) G*a <= h,
                                         (2*) A*a = b.
    
    Because we have to maximize -(1/2)*(a.T)*H*a + (q.T)*a,
    where q.T is a vector of positive ones,
    we can solve the same problem by minimizing (1/2)*(a.T)*H*a + (q'.T)*a,
    where q'.T is a vector of negative ones.
    
    For constraint (1*) which is 0 <= a <= C:
    - G is constituted of two parts:
        a) A diagonal matrix of negative ones for -a <= 0 which is equal to 0 <= a, 
        b) A diagonal matrix of positive ones for a <= C.
    - h has a zero value for the first N cells, while a value 'C' 
      for the rest of the cells.
    
    As for constraint (2*) which is a*y.T = 0:
    -A is the Y Vector
    -b is the value zero (a zero vector of size 1).    
    
    """
    N = len(Y)
    
    # Minimize (1/2)*(a.T)*H*a + (q.T)*a
    if Kernel == None:
        H = getHMatrix(X, Y)
    else:
        H = getKernelHMatrix(X, Y, N, Kernel, gamma)    
    
    H = c_matrix(H) # H Matrix
    q = c_matrix(-np.ones((N, 1))) # Negative Ones Vector
    # Subject to: G*a <= h
    G = c_matrix(np.vstack((np.eye(N)*(-1), np.eye(N))))
    h = c_matrix(np.hstack((np.zeros(N), np.ones(N) * C)))
    # Subject to: A*a = b
    A = c_matrix(Y.reshape(1, -1)) # Y Vector reshaped
    b = c_matrix(np.zeros(1)) # Zero Vector of size one
    
    # Changing default settings 
    c_solvers.options['show_progress'] = False
    c_solvers.options['abstol'] = 1e-10
    c_solvers.options['reltol'] = 1e-10
    c_solvers.options['feastol'] = 1e-10
    
    solution = c_solvers.qp(H, q, G, h, A, b)
      
    alphas = []
    SupportVectors = []

    i = 0
    while i < len(solution['x']):
        if solution['x'][i] > 1e-3: # All alphas bellow 0.001 are considered zero.
            alphas.append(solution['x'][i])
            SupportVectors.append((X[i], Y[i]))
        i += 1
    
    return np.array(alphas), np.array(SupportVectors)


def getHMatrix(X, Y):
    """ Each cell H[i][j] corresponds to Y[i]*Y[j]*X[i]*X[j].T """
    Z = np.multiply(X, Y.reshape(-1, 1)) # Mulitiply them element-wise so you get Yi*Xi on each row
    H = Z @ Z.T # Matrix Multiplication of Z with its transpose so we get symmetric matrix H
    return H


def getKernelHMatrix(X, Y, N, Kernel, gamma):
    
    H = np.zeros((N, N))
    
    for i in range(N):
        for j in range(i, N):
            H[i][j] = Y[i]*Y[j]*(KernelFunction(X[i], X[j], Kernel, gamma))
            H[j][i] = H[i][j]
    
    return H


def getWeightVector(SupportVectors, alphas):

    SVX = np.array([x[0] for x in SupportVectors])
    SVY = np.array([y[1] for y in SupportVectors])
    
    w = (np.multiply(alphas, SVY)) @ SVX # w = Y*a*X
    return w


def getBias(SupportVectors, w):
    
    bias = []
    
    for sv in SupportVectors:
        bias.append(sv[1] - w @ sv[0].T) # y - w*X.T for support vectors
    
    return sum(bias)/len(bias)


def getKernelBias(SupportVectors, alphas, Kernel, gamma):
    
    SVX, SVY = SupportVectors[:, 0], SupportVectors[:, 1]

    bias = []

    for i in range(len(SVY)):
        v = SVY[i]
        for j in range(len(SVY)):
            v -= alphas[j]*SVY[j]*KernelFunction(SVX[j], SVX[i], Kernel, gamma)
        bias.append(v)
     
    return sum(bias)/len(bias)


def KernelFunction(X, Y, Kernel, gamma):
    
    if Kernel == "Polynomial":
        return math.pow(1 + (X @ Y.T), gamma)
    elif Kernel == "RBF":
        return math.exp((-1) * gamma * math.pow(np.linalg.norm(X - Y), 2))
    
    

def generateDataset(N):
    
    Dataset = []  
    i = 0  
    while i < N:

        x1 = round(random.uniform(0.01, 0.99), 2)
        x2 = round(random.uniform(0.01, 0.99), 2)
        
        if x1 + x2 <= 0.9:
            label = -1
        elif x1 + x2 >= 1.1:
            label = 1
        else:
            continue
        
        i += 1
        Dataset.append(([x1, x2], label))
        
    random.shuffle(Dataset)
    return Dataset

"""
************************** Demonstration ****************************

A Training and Testing set are generated via 'generateDataset'.
Each set contains 1000 tuples where each tuple has a vector
in its first position as a numpy array, while its second position
holds the label '1' or '-1' (int). The samples which are generated
are linearly separable, but SVM can be used for the classification
of non-seperable samples too. Usually the best accuracy is achieved
using a Non-Linear SVM with Kernel = 'RBF'.

*********************************************************************
"""

def main():
    
    Training = generateDataset(1000)
    Testing = generateDataset(1000)
    
    # Linear SVM
    LSVM = LinearSVM(Data = Training, C = 100)
    LSVM.getInfo()
    LSVM.evaluate(Testing)
    
    # Non-Linear SVM
    LSVM = NonLinearSVM(Data = Training, C = 100, Kernel = "RBF", gamma = 0.1)
    LSVM.getInfo()
    LSVM.evaluate(Testing)



if __name__== "__main__":
    main()