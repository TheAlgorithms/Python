"""
Demonstration of the Automatic Differentiation (Reverse mode).

Reference: https://en.wikipedia.org/wiki/Automatic_differentiation

Author: Poojan smart
Email: smrtpoojan@gmail.com

Examples:

>>> with GradientTracker() as tracker:
...     a = Variable([2.0, 5.0])
...     b = Variable([1.0, 2.0])
...     m = Variable([1.0, 2.0])
...     c = a + b
...     d = a * b
...     e = c / d
>>> print(tracker.gradient(e, a))
[-0.25 -0.04]
>>> print(tracker.gradient(e, b))
[-1.   -0.25]
>>> print(tracker.gradient(e, m))
None

>>> with GradientTracker() as tracker:
...     a = Variable([[2.0, 5.0]])
...     b = Variable([[1.0], [2.0]])
...     c = a @ b
>>> print(tracker.gradient(c, a))
[[1. 2.]]
>>> print(tracker.gradient(c, b))
[[2.]
 [5.]]

>>> with GradientTracker() as tracker:
...     a = Variable([[2.0, 5.0]])
...     b = a ** 3
>>> print(tracker.gradient(b, a))
[[12. 75.]]
"""
from __future__ import annotations

from enum import Enum
from types import TracebackType

import numpy as np
from typing_extensions import Self


class Variable:
    """
    Class represents n-dimensional object which is used to wrap
    numpy array on which operations will be performed and gradient
    will be calculated.
    """

    def __init__(self, value) -> None:
        self.value = np.array(value)

        # pointers to the operations to which the Variable is input
        self.param_to: list[Operation] = []
        # pointer to the operation of which the Variable is output of
        self.result_of: Operation = Operation(OpType.NOOP)

    def __str__(self) -> str:
        return f"Variable({self.value})"

    def numpy(self) -> np.ndarray:
        return self.value

    def __add__(self, other: Variable) -> Variable:
        result = Variable(self.value + other.value)

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.add_operation(OpType.ADD, params=[self, other], output=result)
        return result

    def __sub__(self, other: Variable) -> Variable:
        result = Variable(self.value - other.value)

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.add_operation(OpType.SUB, params=[self, other], output=result)
        return result

    def __mul__(self, other: Variable) -> Variable:
        result = Variable(self.value * other.value)

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.add_operation(OpType.MUL, params=[self, other], output=result)
        return result

    def __truediv__(self, other: Variable) -> Variable:
        result = Variable(self.value / other.value)

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.add_operation(OpType.DIV, params=[self, other], output=result)
        return result

    def __matmul__(self, other: Variable) -> Variable:
        result = Variable(self.value @ other.value)

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.add_operation(
                    OpType.MATMUL, params=[self, other], output=result
                )
        return result

    def __pow__(self, power: int) -> Variable:
        result = Variable(self.value**power)

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.add_operation(
                    OpType.POWER,
                    params=[self],
                    output=result,
                    other_params={"power": power},
                )
        return result

    def add_param_to(self, param_to: Operation) -> None:
        self.param_to.append(param_to)

    def add_result_of(self, result_of: Operation) -> None:
        self.result_of = result_of


class OpType(Enum):
    """
    Class represents list of supported operations on Variable for
    gradient calculation.
    """

    ADD = 0
    SUB = 1
    MUL = 2
    DIV = 3
    MATMUL = 4
    POWER = 5
    NOOP = 6


class Operation:
    """
    Class represents operation between single or two Variable objects.
    Operation objects contains type of operation, pointers to input Variable
    objects and pointer to resulting Variable from the operation.
    """

    def __init__(
        self,
        op_type: OpType,
        other_params: dict | None = None,
    ) -> None:
        self.op_type = op_type
        self.other_params = {} if other_params is None else other_params

    def add_params(self, params: list[Variable]) -> None:
        self.params = params

    def add_output(self, output: Variable) -> None:
        self.output = output

    def __eq__(self, value) -> bool:
        if isinstance(value, OpType):
            return self.op_type == value
        return False


class GradientTracker:
    """
    Class contains methods to compute partial derivatives of Variable
    based on the computation graph.
    """

    instance = None

    def __new__(cls) -> Self:
        """
        Executes at the creation of class object and returns if
        object is already created. This class follows singleton
        design pattern.
        """
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.enabled = False

    def __enter__(self) -> Self:
        self.enabled = True
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.enabled = False

    def add_operation(
        self,
        op_type: OpType,
        params: list[Variable],
        output: Variable,
        other_params: dict | None = None,
    ) -> None:
        """
        Adds Operation object to the related Variable objects for
        creating computational graph for calculating gradients.

        Args:
            op_type: Operation type
            params: Input parameters to the operation
            output: Output variable of the operation
        """
        operation = Operation(op_type, other_params=other_params)
        param_nodes = []
        for param in params:
            param.add_param_to(operation)
            param_nodes.append(param)
        output.add_result_of(operation)

        operation.add_params(param_nodes)
        operation.add_output(output)

    def gradient(self, target: Variable, source: Variable) -> np.ndarray | None:
        """
        Reverse accumulation of partial derivatives to calculate gradients
        of target variable with respect to source variable.

        Args:
            target: target variable for which gradients are calculated.
            source: source variable with respect to which the gradients are
            calculated.

        Returns:
            Gradient of the source variable with respect to the target variable
        """

        # partial derivatives with respect to target
        partial_deriv = {target: np.ones_like(target.numpy())}

        # iterating through each operations in the computation graph
        operation_queue = [target.result_of]
        while len(operation_queue) > 0:
            operation = operation_queue.pop()
            for param in operation.params:
                # as per the chain rule, multiplying partial derivatives
                # of variables with respect to the target
                dparam_doutput = self.derivative(param, operation)
                dparam_dtarget = dparam_doutput * partial_deriv[operation.output]
                if param in partial_deriv:
                    partial_deriv[param] += dparam_dtarget
                else:
                    partial_deriv[param] = dparam_dtarget

                if param.result_of:
                    if param.result_of != OpType.NOOP:
                        operation_queue.append(param.result_of)

        if source in partial_deriv:
            return partial_deriv[source]
        return None

    def derivative(self, param: Variable, operation: Operation) -> np.ndarray:
        """
        Compute the derivative of given operation/function

        Args:
            param: variable to be differentiated
            operation: function performed on the input variable

        Returns:
            Derivative of input variable with respect to the output of
            the operation
        """
        params = operation.params

        derivative = None

        if operation == OpType.ADD:
            derivative = np.ones_like(params[0].numpy(), dtype=np.float64)
        elif operation == OpType.SUB:
            if params[0] == param:
                derivative = np.ones_like(params[0].numpy(), dtype=np.float64)
            else:
                derivative = -np.ones_like(params[1].numpy(), dtype=np.float64)
        elif operation == OpType.MUL:
            derivative = (
                params[1].numpy().T if params[0] == param else params[0].numpy().T
            )
        elif operation == OpType.DIV:
            if params[0] == param:
                derivative = 1 / params[1].numpy()
            else:
                derivative = -params[0].numpy() / (params[1].numpy() ** 2)
        elif operation == OpType.MATMUL:
            derivative = (
                params[1].numpy().T if params[0] == param else params[0].numpy().T
            )
        elif operation == OpType.POWER:
            power = operation.other_params["power"]
            derivative = power * (params[0].numpy() ** (power - 1))
        return derivative


if __name__ == "__main__":
    import doctest

    doctest.testmod()
