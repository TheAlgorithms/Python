import numpy as np
import pandas as pd

class XGBoostRegressor():
    '''Implementation of XGBoost regressor.
    
    This implementation includes a simplified version of the XGBoost algorithm
    for regression tasks. It includes gradient boosting with decision trees as base learners.
    '''
    
    def __init__(self, params=None, random_seed=None):
        '''Initialize XGBoostRegressor.
        
        Parameters:
            params (dict): Hyperparameters for the XGBoost model.
            random_seed (int): Seed for random number generation.
        '''
        # Set hyperparameters with defaults
        self.params = defaultdict(lambda: None, params)
        self.subsample = self.params['subsample'] or 1.0
        self.learning_rate = self.params['learning_rate'] or 0.3
        self.base_prediction = self.params['base_score'] or 0.5
        self.max_depth = self.params['max_depth'] or 5
        self.random_seed = random_seed
        self.boosters = []
                
    def fit(self, X, y, objective, num_boost_round, verbose=False):
        '''Train the XGBoost model.
        
        Parameters:
            X (pd.DataFrame): Feature matrix.
            y (pd.Series): Target values.
            objective (ObjectiveFunction): Objective function for regression.
            num_boost_round (int): Number of boosting rounds.
            verbose (bool): Whether to print training progress.
        '''
        # Initialize predictions with base score
        current_predictions = np.full_like(y, self.base_prediction)
        for i in range(num_boost_round):
            # Compute negative gradient and hessian
            gradients = objective.gradient(y, current_predictions)
            hessians = objective.hessian(y, current_predictions)
            # Apply subsampling if required
            if self.subsample < 1.0:
                sample_idxs = np.random.choice(len(y), size=int(self.subsample * len(y)), replace=False)
                gradients, hessians = gradients[sample_idxs], hessians[sample_idxs]
            booster = DecisionTreeBooster(X, gradients, hessians, self.params, self.max_depth, self.random_seed)
            # Update predictions using learning rate and booster predictions
            current_predictions += self.learning_rate * booster.predict(X)
            self.boosters.append(booster)
            if verbose: 
                print(f'[{i}] train loss = {objective.loss(y, current_predictions)}')
            
    def predict(self, X):
        '''Make predictions using the trained model.
        
        Parameters:
            X (pd.DataFrame): Feature matrix for prediction.
        
        Returns:
            np.ndarray: Predicted values.
        '''
        # Calculate predictions using all boosters
        return (self.base_prediction + self.learning_rate * 
                np.sum([booster.predict(X) for booster in self.boosters], axis=0))


class DecisionTreeBooster:
    '''Decision tree booster for XGBoost regressor.'''
    
    def __init__(self, X, g, h, params, max_depth, random_seed=None):
        '''Initialize a decision tree booster.
        
        Parameters:
            X (np.ndarray): Feature matrix.
            g (np.ndarray): Gradient values.
            h (np.ndarray): Hessian values.
            params (dict): Hyperparameters for the booster.
            max_depth (int): Maximum depth of the tree.
            random_seed (int): Seed for random number generation.
        '''
        # Set hyperparameters
        self.params = params
        self.max_depth = max_depth
        assert self.max_depth >= 0, 'max_depth must be nonnegative'
        self.min_child_weight = params.get('min_child_weight', 1.0)
        self.reg_lambda = params.get('reg_lambda', 1.0)
        self.gamma = params.get('gamma', 0.0)
        self.colsample_bynode = params.get('colsample_bynode', 1.0)
        self.random_seed = random_seed
        np.random.seed(self.random_seed)
        
        # Set data and indices
        self.X, self.g, self.h = X, g, h
        self.n, self.c = X.shape[0], X.shape[1]
        self.idxs = np.arange(self.n)
        
        # Initialize node value
        self.value = -np.sum(g[self.idxs]) / (np.sum(h[self.idxs]) + self.reg_lambda)
        self.best_score_so_far = 0.
        
        # Recursively build the tree
        if self.max_depth > 0:
            self._maybe_insert_child_nodes()


    @property
    def is_leaf(self):
        '''Check if the node is a leaf.'''
        return self.best_score_so_far == 0.
    
    def _maybe_insert_child_nodes(self):
        '''Recursively insert child nodes to build the tree.'''
        for i in range(self.c):
            self._find_better_split(i)
        if self.is_leaf:
            return
        # Split the data based on the best feature and threshold
        x = self.X.values[self.idxs, self.split_feature_idx]
        left_idx = np.nonzero(x <= self.threshold)[0]
        right_idx = np.nonzero(x > self.threshold)[0]
        # Recur for left and right subtrees
        self.left = DecisionTreeBooster(self.X, self.g, self.h, self.params, 
                                self.max_depth - 1, self.idxs[left_idx])
        self.right = DecisionTreeBooster(self.X, self.g, self.h, self.params, 
                                 self.max_depth - 1, self.idxs[right_idx])

    def _find_better_split(self, feature_idx):
        '''Find the best split for a feature.'''
        x = self.X.values[self.idxs, feature_idx]
        g, h = self.g[self.idxs], self.h[self.idxs]
        sort_idx = np.argsort(x)
        sort_g, sort_h, sort_x = g[sort_idx], h[sort_idx], x[sort_idx]
        sum_g, sum_h = g.sum(), h.sum()
        sum_g_right, sum_h_right = sum_g, sum_h
        sum_g_left, sum_h_left = 0., 0.

        for i in range(self.n - 1):
            g_i, h_i, x_i, x_i_next = sort_g[i], sort_h[i], sort_x[i], sort_x[i + 1]
            sum_g_left += g_i
            sum_g_right -= g_i
            sum_h_left += h_i
            sum_h_right -= h_i
            if sum_h_left < self.min_child_weight or x_i == x_i_next:
                continue
            if sum_h_right < self.min_child_weight:
                break

            gain = 0.5 * ((sum_g_left**2 / (sum_h_left + self.reg_lambda))
                          + (sum_g_right**2 / (sum_h_right + self.reg_lambda))
                          - (sum_g**2 / (sum_h + self.reg_lambda))
                          ) - self.gamma/2 # Eq(7) in the xgboost paper
            if gain > self.best_score_so_far: 
                self.split_feature_idx = feature_idx
                self.best_score_so_far = gain
                self.threshold = (x_i + x_i_next) / 2
                
    def predict(self, X):
        '''Make predictions using the trained booster.'''
        return np.array([self._predict_row(row) for _, row in X.iterrows()])

    def _predict_row(self, row):
        '''Recursively predict a single data point.'''
        if self.is_leaf: 
            return self.value
        child = self.left if row[self.split_feature_idx] <= self.threshold \
            else self.right
        return child._predict_row(row)
