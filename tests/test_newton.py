"""Tests for the NewtonFractal class"""

import unittest

import numpy as np
import sympy as sym
import matplotlib
import matplotlib.pyplot as plt

from fractpy.models import NewtonFractal

x = sym.Symbol("x")
i = sym.I


class TestNewtonFractal(unittest.TestCase):
    """Tests for the class Newton Fractal"""

    def test_function_init(self):
        func = "(x - 2)(x - 3*I)(x + 3*I)"
        model = NewtonFractal(func)

        # Test for function
        model_func = model.function.function
        test_func = (x - 2) * (x - 3 * i) * (x + 3 * i)
        self.assertEqual(model_func, test_func)

        # Test for roots_list
        roots_list = set([2, 3j, -3j])
        self.assertEqual(set(model.roots_list), roots_list)

    def test_function_repr(self):
        func = "x**3 - 2*x**2 -4"
        model = NewtonFractal(func)
        output = "### FractPy Model ###\nType: Newton Fractal\nFunction: \
x**3 - 2*x**2 - 4"
        self.assertEqual(model.__repr__(), output)

    def test_make_list(self):
        func = "x**2 + 1"
        model = NewtonFractal(func)
        model._xvals = [i for i in range(3)]
        model._yvals = [i for i in range(3)]
        model._make_list()
        zlist = set(
            [
                0 + 0j,
                0 + 1j,
                0 + 2j,
                1 + 0j,
                1 + 1j,
                1 + 2j,
                2 + 0j,
                2 + 1j,
                2 + 2j,
            ]
        )
        self.assertEqual(set(model._z_list), zlist)

    def test_match_root(self):
        func = "x**2 - 1"
        model = NewtonFractal(func)
        model._xvals = [i for i in range(3)]
        model._yvals = [i for i in range(3)]
        model._make_list()
        rootid = model._match_root()
        test_rootid = np.array([-1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0])
        self.assertTrue((rootid == test_rootid).all())

    def test_prepare_plot(self):
        func = "x**3 - 1"
        model = NewtonFractal(func)
        model._width = 10
        model._height = 10
        data = model._prepare_plot(-2, 2, -2, 2)
        test_data = np.array(
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 2, 0, 0],
                [1, 1, 1, 1, 1, 1, 2, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                [2, 1, 1, 0, 1, 2, 0, 0, 0, 0],
                [1, 2, 2, 0, 2, 1, 0, 0, 0, 0],
                [2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
                [2, 2, 2, 2, 2, 2, 1, 0, 0, 0],
                [2, 2, 2, 2, 2, 2, 2, 1, 0, 0],
                [2, 2, 2, 2, 2, 2, 2, 2, 0, 0],
            ]
        )
        self.assertTrue((data == test_data).all())

    def test_plot(self):
        func = "2x**2 - 8"
        model = NewtonFractal(func)
        p = model.plot(-2, 2, -2, 2, (20, 10))

        # Check dimensions
        self.assertEqual(model._width, 20)
        self.assertEqual(model._height, 10)

        self.assertIsInstance(p, matplotlib.figure.Figure)
        self.assertEqual(
            p.axes[0].title.get_text(),
            "Newton Fractal for $f(x) = 2 x^{2} - 8$",
        )
        plt.close(p)

    def test_zoom_plot(self):
        func = "x**3 - 1"
        model = NewtonFractal(func)
        p = model.zoom_plot(-2, 2, -2, 2, (10, 20))

        self.assertEqual(model._width, 10)
        self.assertEqual(model._height, 20)

        self.assertIsInstance(p, matplotlib.figure.Figure)
        self.assertEqual(
            p.get_children()[-1].get_text(),
            "Newton Fractal for $f(x) = x^{3} - 1$",
        )
        self.assertEqual(len(p.axes), 2)
        self.assertEqual(
            p.axes[1].title.get_text(),
            "Zoom here",
        )
        plt.close(p)
