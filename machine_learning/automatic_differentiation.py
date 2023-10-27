"""
Demonstration of the Automatic Differentiation (Reverse mode).

Reference: https://en.wikipedia.org/wiki/Automatic_differentiation

Author: Poojan Smart
Email: smrtpoojan@gmail.com
"""
from __future__ import annotations

from collections import defaultdict
from enum import Enum
from types import TracebackType
from typing import Any

import numpy as np
from typing_extensions import Self  # noqa: UP035


class OpType(Enum):
    """
    Class represents list of supported operations on Variable for gradient calculation.
    """

    ADD = 0
    SUB = 1
    MUL = 2
    DIV = 3
    MATMUL = 4
    POWER = 5
    NOOP = 6


class Variable:
    """
    Class represents n-dimensional object which is used to wrap numpy array on which
    operations will be performed and the gradient will be calculated.

    Examples:
    >>> Variable(5.0)
    Variable(5.0)
    >>> Variable([5.0, 2.9])
    Variable([5.  2.9])
    >>> Variable([5.0, 2.9]) + Variable([1.0, 5.5])
    Variable([6.  8.4])
    >>> Variable([[8.0, 10.0]])
    Variable([[ 8. 10.]])
    """

    def __init__(self, value: Any) -> None:
        self.value = np.array(value)

        # pointers to the operations to which the Variable is input
        self.param_to: list[Operation] = []
        # pointer to the operation of which the Variable is output of
        self.result_of: Operation = Operation(OpType.NOOP)

    def __repr__(self) -> str:
        return f"Variable({self.value})"

    def to_ndarray(self) -> np.ndarray:
        return self.value

    def __add__(self, other: Variable) -> Variable:
        result = Variable(self.value + other.value)

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.ADD, params=[self, other], output=result)
        return result

    def __sub__(self, other: Variable) -> Variable:
        result = Variable(self.value - other.value)

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.SUB, params=[self, other], output=result)
        return result

    def __mul__(self, other: Variable) -> Variable:
        result = Variable(self.value * other.value)

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.MUL, params=[self, other], output=result)
        return result

    def __truediv__(self, other: Variable) -> Variable:
        result = Variable(self.value / other.value)

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.DIV, params=[self, other], output=result)
        return result

    def __matmul__(self, other: Variable) -> Variable:
        result = Variable(self.value @ other.value)

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.MATMUL, params=[self, other], output=result)
        return result

    def __pow__(self, power: int) -> Variable:
        result = Variable(self.value**power)

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(
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
        return self.op_type == value if isinstance(value, OpType) else False


class GradientTracker:
    """
    Class contains methods to compute partial derivatives of Variable
    based on the computation graph.

    Examples:

    >>> with GradientTracker() as tracker:
    ...     a = Variable([2.0, 5.0])
    ...     b = Variable([1.0, 2.0])
    ...     m = Variable([1.0, 2.0])
    ...     c = a + b
    ...     d = a * b
    ...     e = c / d
    >>> tracker.gradient(e, a)
    array([-0.25, -0.04])
    >>> tracker.gradient(e, b)
    array([-1.  , -0.25])
    >>> tracker.gradient(e, m) is None
    True

    >>> with GradientTracker() as tracker:
    ...     a = Variable([[2.0, 5.0]])
    ...     b = Variable([[1.0], [2.0]])
    ...     c = a @ b
    >>> tracker.gradient(c, a)
    array([[1., 2.]])
    >>> tracker.gradient(c, b)
    array([[2.],
           [5.]])

    >>> with GradientTracker() as tracker:
    ...     a = Variable([[2.0, 5.0]])
    ...     b = a ** 3
    >>> tracker.gradient(b, a)
    array([[12., 75.]])
    """

    instance = None

    def __new__(cls) -> Self:
        """
        Executes at the creation of class object and returns if
        object is already created. This class follows singleton
        design pattern.
        """
        if cls.instance is None:
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

    def append(
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
        partial_deriv = defaultdict(lambda: 0)
        partial_deriv[target] = np.ones_like(target.to_ndarray())

        # iterating through each operations in the computation graph
        operation_queue = [target.result_of]
        while len(operation_queue) > 0:
            operation = operation_queue.pop()
            for param in operation.params:
                # as per the chain rule, multiplying partial derivatives
                # of variables with respect to the target
                dparam_doutput = self.derivative(param, operation)
                dparam_dtarget = dparam_doutput * partial_deriv[operation.output]
                partial_deriv[param] += dparam_dtarget

                if param.result_of and param.result_of != OpType.NOOP:
                    operation_queue.append(param.result_of)

        return partial_deriv.get(source)

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

        if operation == OpType.ADD:
            return np.ones_like(params[0].to_ndarray(), dtype=np.float64)
        if operation == OpType.SUB:
            if params[0] == param:
                return np.ones_like(params[0].to_ndarray(), dtype=np.float64)
            return -np.ones_like(params[1].to_ndarray(), dtype=np.float64)
        if operation == OpType.MUL:
            return (
                params[1].to_ndarray().T
                if params[0] == param
                else params[0].to_ndarray().T
            )
        if operation == OpType.DIV:
            if params[0] == param:
                return 1 / params[1].to_ndarray()
            return -params[0].to_ndarray() / (params[1].to_ndarray() ** 2)
        if operation == OpType.MATMUL:
            return (
                params[1].to_ndarray().T
                if params[0] == param
                else params[0].to_ndarray().T
            )
        if operation == OpType.POWER:
            power = operation.other_params["power"]
            return power * (params[0].to_ndarray() ** (power - 1))

        err_msg = f"invalid operation type: {operation.op_type}"
        raise ValueError(err_msg)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
