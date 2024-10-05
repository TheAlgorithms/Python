import numpy as np
from scipy.optimize import minimize

class GaussianProcessRegressor:
    def __init__(self, kernel='rbf', noise=1e-8):
        """
        Initialize the Gaussian Process Regressor.
        
        Args:
        kernel (str): The type of kernel to use. Currently only 'rbf' is implemented.
        noise (float): The noise level for the diagonal of the covariance matrix.
        """
        self.kernel = kernel
        self.noise = noise
        self.X_train = None
        self.y_train = None
        self.params = None

    def rbf_kernel(self, X1, X2, l=1.0, sigma_f=1.0):
        """
        Radial Basis Function (RBF) kernel, also known as squared exponential kernel.
        
        K(x, x') = σ^2 * exp(-1/(2l^2) * ||x - x'||^2)
        
        Args:
        X1, X2 (numpy.ndarray): Input arrays
        l (float): Length scale parameter
        sigma_f (float): Signal variance parameter
        
        Returns:
        numpy.ndarray: Kernel matrix
        """
        sqdist = np.sum(X1**2, 1).reshape(-1, 1) + np.sum(X2**2, 1) - 2 * np.dot(X1, X2.T)
        return sigma_f**2 * np.exp(-0.5 / l**2 * sqdist)

    def negative_log_likelihood(self, params):
        """
        Compute the negative log likelihood.
        This is the function we want to minimize to find optimal kernel parameters.
        
        Args:
        params (list): List containing kernel parameters [l, sigma_f]
        
        Returns:
        float: Negative log likelihood
        """
        l, sigma_f = params
        K = self.rbf_kernel(self.X_train, self.X_train, l, sigma_f) + self.noise**2 * np.eye(len(self.X_train))
        return 0.5 * np.log(np.linalg.det(K)) + \
               0.5 * self.y_train.T.dot(np.linalg.inv(K).dot(self.y_train)) + \
               0.5 * len(self.X_train) * np.log(2*np.pi)

    def fit(self, X, y):
        """
        Fit the GPR model to the training data.
        
        Args:
        X (numpy.ndarray): Training input data
        y (numpy.ndarray): Training target data
        """
        self.X_train = X
        self.y_train = y
        
        # Optimize kernel parameters using L-BFGS-B algorithm
        res = minimize(self.negative_log_likelihood, [1, 1], 
                       bounds=((1e-5, None), (1e-5, None)),
                       method='L-BFGS-B')
        self.params = res.x

    def predict(self, X_test, return_std=False):
        """
        Make predictions on test data.
        
        Args:
        X_test (numpy.ndarray): Test input data
        return_std (bool): If True, return standard deviation along with mean
        
        Returns:
        tuple or numpy.ndarray: Mean predictions (and standard deviations if return_std=True)
        """
        l, sigma_f = self.params
        
        # Compute relevant kernel matrices
        K = self.rbf_kernel(self.X_train, self.X_train, l, sigma_f) + self.noise**2 * np.eye(len(self.X_train))
        K_s = self.rbf_kernel(self.X_train, X_test, l, sigma_f)
        K_ss = self.rbf_kernel(X_test, X_test, l, sigma_f) + 1e-8 * np.eye(len(X_test))

        K_inv = np.linalg.inv(K)
        
        # Compute predictive mean
        mu_s = K_s.T.dot(K_inv).dot(self.y_train)
        
        # Compute predictive variance
        var_s = K_ss - K_s.T.dot(K_inv).dot(K_s)
        
        return (mu_s, np.sqrt(np.diag(var_s))) if return_std else mu_s

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    X = np.array([1, 3, 5, 6, 7, 8]).reshape(-1, 1)
    y = np.sin(X).ravel()

    # Create and fit the model
    gpr = GaussianProcessRegressor()
    gpr.fit(X, y)

    # Make predictions
    X_test = np.linspace(0, 10, 100).reshape(-1, 1)
    mu_s, std_s = gpr.predict(X_test, return_std=True)

    print("Predicted mean:", mu_s)
    print("Predicted standard deviation:", std_s)

    # Note: To visualize results, you would typically use matplotlib here
    # to plot the original data, predictions, and confidence intervals