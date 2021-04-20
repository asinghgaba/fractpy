Create a Model
==============

A model in ``fractpy`` is an object which represents the method it is using
to generate fractals. 

.. note::
    FractPy currently supports only Newton Fractal method of fractal
    generation for polynomial functions with real powers. More methods are
    currently in development.

To make a Newton Fractal Model for the function
:math:`f(x) = (x^2 - 1)(x^2 + 1)`  all we have to do is pass in the
function as ``str`` to the ``NewtonFractal`` class from module
``fractpy.models``::

    >>> from fractpy.models import NewtonFractal
    >>> model = NewtonFractal("(x**2 - 1)(x**2 + 1)")
    >>> model
    ### FractPy Model ###
    Type: Newton Fractal
    Function: (x**2 - 1)*(x**2 + 1)

.. note::
    For complex values use **I** (upper case i) instead of commonly used
    convention of **i**. For example: function
    :math:`f(x) = (x - 1)(x + i)(x - i)` would be passed as
    ``"(x - 1)(x + I)(x - I)"``.

We can use this model to generate fractals!

