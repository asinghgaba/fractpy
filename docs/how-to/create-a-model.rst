Create a model
==============

A model in ``fractpy`` is an object which represents the method it is using
to generate fractals. However, currently ``fractpy`` only supports Newton
Fractal (More to be added soon).

To generate a Newton Fractal model, we first have to create a ``sympy``
expression for the function of which we want to generate the fractal.

To make a ``sympy`` expression for :math:`f(x) = (x^2 - 1)(x^2 + 1)`, we
use the following code::

    >>>import sympy as sym
    >>>x = sym.Symbol('x')
    >>>function = (x**2 - 1) * (x**2 + 1)

.. seealso::

    ``sympy`` for further information on expressions.

Now to make a Newton Fractal Model, all we have to do is pass in the
``sympy`` expression along with the variable ``x`` to the ``NewtonFractal``
class from ``fractpy.models``::

    >>>from fractpy.models import NewtonFractal
    >>>model = NewtonFractal(function, x)

We can use this model to generate fractals!

