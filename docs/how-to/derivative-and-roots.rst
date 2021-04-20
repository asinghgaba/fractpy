To Find the Derivative and the Roots
====================================

Fractpy has a class ``Function`` which can be used to perform basic calculus
operations on a single-variable function. To initialise an object of this
class we pass in the function as type ``str``. 

For example to initialise with function :math:`f(x) = x^4 - 3x^3 + 2x^2 - 9`::

    >>> from fractpy import Function
    >>> f = Function("x**4 - 4*x**3 + 4*x**2 - 4*x + 3")
    >>> f
    x**4 - 4*x**3 + 4*x**2 - 4*x + 3

.. note::
    For complex values use **I** (upper case i) instead of commonly used
    convention of **i**. For example: function
    :math:`f(x) = (x - 1)(x + i)(x - i)` would be passed as
    ``"(x - 1)(x + I)(x - I)"``.

To Calculate Roots
------------------
Use the method ``roots``, which returns list of the roots::

    >>> f.roots()
    [1, 3, I, -I]

To Find the Derivative:
-----------------------
Use the method ``differentiate``, which returns the derivative of the function
in the form of a ``sympy`` expression::

    >>> f.differentiate()
    4*x**3 - 12*x**2 + 8*x - 4