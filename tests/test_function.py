"""Tests for Function class"""

import unittest

import sympy as sym

from fractpy import Function

x = sym.Symbol("x")


class TestFunction(unittest.TestCase):
    """Tests for the class Function."""

    def test_function_init(self):
        # Test for a valid function
        func = "(x**2 + 1)(x - 1)"
        a = Function(func)
        self.assertEqual(a.function, (x ** 2 + 1) * (x - 1))

        # Test for an invalid function
        func = "x + y"
        with self.assertRaises(TypeError) as mess:
            a = Function(func)
        err = mess.exception
        self.assertEqual(
            "x + y is not a single variable function, it has 2 variables",
            str(err),
        )

    def test_function_repr(self):
        func = "x**2 + x - 4"
        a = Function(func)
        self.assertEqual(a.__repr__(), "x**2 + x - 4")

    def test_roots(self):
        func = "(x + 1)(x - I)(x + I)"
        a = Function(func)
        self.assertEqual(set(a.roots()), set([-1, 1j, -1j]))

    def test_differentiate(self):
        func = "x**4 - 2*x**2 - 4"
        a = Function(func)
        derivative = 4 * x ** 3 - 4 * x
        self.assertEqual(a.differentiate(), derivative)

    def test_relative_difference(self):
        func = "4*x**2 - x"
        a = Function(func)
        rd = (4 * x ** 2 - x) / (8 * x - 1)
        self.assertEqual(a._relative_difference(), rd)

    def test_make_python_function(self):
        func = "x**2 + 1"
        a = Function(func)
        func_0 = a._make_python_function()

        f = x ** 2 + 1
        func_1 = Function("x")._make_python_function(f, x)

        def func_2(x):
            return x ** 2 + 1

        # Check if all functions are equal
        ans_0, ans_1, ans_2 = [], [], []
        for i in range(5):
            ans_0.append(func_0(i))
            ans_1.append(func_1(i))
            ans_2.append(func_2(i))
        self.assertEqual(ans_0, ans_1)
        self.assertEqual(ans_1, ans_2)

    def test_rd_python_function(self):
        func = "x**3 - 2x + 1"
        a = Function(func)
        func_0 = a._rd_python_function()

        def func_1(x):
            return (x ** 3 - 2 * x + 1) / (3 * x ** 2 - 2)

        ans_0, ans_1 = [], []
        for i in range(5):
            ans_0.append(func_0(i))
            ans_1.append(func_1(i))
        self.assertEqual(ans_0, ans_1)
