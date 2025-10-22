"""
Base class for neural network optimizers.

This module defines the abstract base class that all optimizers should inherit from
to ensure a consistent interface for parameter updates.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Union


class BaseOptimizer(ABC):
    """
    Abstract base class for all neural network optimizers.
    
    This class defines the common interface that all optimization algorithms
    must implement. It ensures consistency across different optimizer implementations.
    
    Parameters:
        learning_rate: The step size for parameter updates
    """
    
    def __init__(self, learning_rate: float = 0.01) -> None:
        """
        Initialize the optimizer with a learning rate.
        
        Args:
            learning_rate: The learning rate for parameter updates.
                          Must be positive.
                          
        Raises:
            ValueError: If learning_rate is not positive.
            
        Examples:
            >>> # BaseOptimizer is abstract, test via SGD implementation
            >>> from neural_network.optimizers.sgd import SGD
            >>> optimizer = SGD(learning_rate=0.1) 
            >>> optimizer.learning_rate
            0.1
        """
        if learning_rate <= 0:
            raise ValueError(f"Learning rate must be positive, got {learning_rate}")
        
        self.learning_rate = learning_rate
    
    @abstractmethod
    def update(
        self, 
        parameters: Union[List[float], List[List[float]]], 
        gradients: Union[List[float], List[List[float]]]
    ) -> Union[List[float], List[List[float]]]:
        """
        Update parameters using gradients.
        
        This is the core method that each optimizer must implement.
        It takes the current parameters and their gradients, and returns
        the updated parameters.
        
        Args:
            parameters: Current parameter values as list or nested list
            gradients: Gradients of the loss function w.r.t. parameters
            
        Returns:
            Updated parameter values
            
        Raises:
            ValueError: If parameters and gradients have different shapes
        """
        pass
    
    def reset(self) -> None:
        """
        Reset the optimizer's internal state.
        
        This method should be called when starting optimization on a new problem
        or when you want to clear any accumulated state (like momentum).
        Default implementation does nothing, but optimizers with state should override.
        """
        pass
    
    def __str__(self) -> str:
        """String representation of the optimizer."""
        return f"{self.__class__.__name__}(learning_rate={self.learning_rate})"
    
    def __repr__(self) -> str:
        """Detailed string representation of the optimizer."""
        return self.__str__()