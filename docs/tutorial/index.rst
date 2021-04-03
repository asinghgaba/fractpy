Tutorial: Generating Newton Fractal for a simple function
=========================================================

Introduction to Fractal
-----------------------

A fractal is never ending pattern. Fractals are a type of mathematical 
shape that are infinitely complex. They are created by repeating a 
simple process over and over in an ongoing feedback loop. 

In essence, a Fractal is a pattern that repeats forever, and every part
of the Fractal, regardless of how zoomed in, or zoomed out you are, it
looks very similar to the whole image. A shape does not have to be
exactly identical to be classified as a Fractal. Instead shapes that
display inherent and repeating similarities are the main requirement
for being classified as a Fractal.

Here is an animation [Mandelbrot2010]_ representing the Mandelbrot Set
Fractal one of the most iconic math fractals:

.. image:: /_static/mandelbrot.gif
    :align: center
    :scale: 150

For more background information on fractals: [FractalFoundation2009]_.

Newton Fractal
++++++++++++++

One way of generating fractals is using Newton-Raphson Method, also known
as Newton Fractal. Newton fractals are fractals created in the plane of
complex numbers. An iteration process with Newton’s method is started at
each point on a grid in the complex plane, and a color is assigned to each
point according to which of the roots of a given function the iteration
converges to.

A generalisation of Newton's iteration is:

.. math::

    z_{n+1} = z_n - \frac{f(z_n)}{f'(z_n)}

where :math:`z \in \mathbb{C}` represents any point in the plane,
:math:`n \in \mathbb{N}` represents the number of step, and
:math:`f(z)` is a polynomial or transcendental function.

For :math:`f(z) = z^3 - 1`, the iteration is:

.. math::

    z_{n+1} = z_n - \frac{z^3 - 1}{3z^2}

Let us now see how to plot fractal for this function using ``fractpy``.


Creating a Model
----------------

To generate Newton Fractal for the above function we first have to create
a ``sympy`` expression::

    >>>import sympy as sym
    >>>x = sym.Symbol('x')
    >>>function = x**3 - 1

Now, we make a ``NewtonFractal`` model using ``fractpy``::

    >>>from fractpy.models import NewtonFractal
    >>>model = NewtonFractal(function, x)

Generating Fractal
------------------

To generate the fractal all we have to do now is call the method ``plot``,
and pass in the axes limits::

    >>>xmin, xmax, ymin, ymax = -2, 2, -2, 2
    >>>model.plot(xmin, xmax, ymin, ymax)

This creates the following plot:

.. TODO: Insert Plot