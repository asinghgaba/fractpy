

import sympy as sym

from fractpy.models.newton import NewtonFractal

x = sym.Symbol('x')
function = x**3 - 1

model = NewtonFractal(20, 20, function, x, 1.e-11, 200)
model.zoom_plot(-2, 2, -2, 2)