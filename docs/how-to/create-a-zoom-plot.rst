Create a Zoom Plot
==================

Creating a simple plot for fractals is pretty boring, especially if
you cannot see the beauty of how it repeats itself. 

So ``fractpy`` offers a funtionality in which you can dynamically
zoom in any region of the plot. To create such plot we will use the
method ``zoom_plot`` which creates two identical panels. Zooming in
on the right panel will show a rectangle in the first panel, denoting
the zoomed region. And as done in ``plot`` we will gave to pass in
the initial axes range, along with the resolution of the plot to be
generated, and get the ``matplotlib.figure.Figure``::

    >>> p = model.zoom_plot(-2, 2, -2, 2, (200,200))
    >>> p.show()

This creates a plot like this, which can be zoomed in:

.. image:: /_static/howto_zoom_plot.gif
    :align: center

.. note:: 
    This currently does not work in Jupyter Notebook, and has to be
    run using a python script.