"""A class for performing basic operations on functions."""

import numpy as np
import sympy as sym
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
)


class Function:
    """A class for performing basic operations on
    given single-variable function. The operations
    include finding roots, calculating derivative.

    Parameters
    ----------
    function : str
        The function of interest (has to be a
        single variable function).

    Attributes
    ----------
    function : ``sympy`` expression
        The function of interest.
    variable : :obj:`sympy.Symbol`
        The variable in terms which the function
        is defined.

    Notes
    -----
    This class was mainly developed to be used for
    ``fractpy.models.NewtonFractal`` class.


    """

    def __init__(self, function):
        self.function = function

    def __repr__(self):
        return str(self.function)

    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, func):
        transformations = standard_transformations + (
            implicit_multiplication_application,
        )
        expr = parse_expr(func, transformations=transformations)
        if len(expr.free_symbols) == 1:
            self._function = expr
            self._variable = list(expr.free_symbols)[0]
        else:
            raise TypeError(
                func
                + f" is not a single variable function, \
it has {len(expr.free_symbols)} variables"
            )

    @property
    def variable(self):
        return self._variable

    def roots(self):
        """Calculate roots of the function.

        Returns
        -------
        list
            Roots of the function.
        """
        return np.array(list(sym.solveset(self.function, self.variable)), dtype=complex)

    def differentiate(self):
        """Differentiates the function.

        Returns
        -------
        ``sympy`` expression
            Derivative of the function.
        """
        return sym.diff(self.function, self.variable)

    def _relative_difference(self):
        """Computes the expression required for generating Newton
        fractal i.e. f(x)/f'(x).

        Returns
        -------
        ``sympy`` expression
            The sympy expression for the iteration of Newtons'
            method.
        """
        return self.function / self.differentiate()

    def _make_python_function(self, function=None, variable=None):
        """Converts ``sympy`` expression to python functions.
        This makes it easy to calculate multiple values by passing
        numpy arrays.

        Parameters
        ----------
        function : ``sympy`` expression
            The function which is to be converted (default is
            the function in the object).
        variable : :obj:`sympy.Symbol`
            The variable in terms which the function is defined
            (default is the variable in the object).

        Returns
        -------
        function
            Python function for the given ``sympy`` function.
        """
        if function is None:
            function = self.function
        if variable is None:
            variable = self.variable
        return sym.lambdify(variable, function)

    def _rd_python_function(self):
        """Returns the expression required for generating Newton
        fractal i.e. f(x)/f'(x) in the form of Python function.

        Returns
        -------
        function
            Python function for the iteration of Newtons'
            method.
        """
        rd = self._relative_difference()
        return self._make_python_function(rd, self.variable)
