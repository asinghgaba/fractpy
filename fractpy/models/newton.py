"""A class for plotting Newton Fractal."""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

from ..zoom import UpdatingRect
from ..function import Function


rect = UpdatingRect(
            [0, 0], 0, 0, facecolor='none', edgecolor='black', linewidth=1.0)


class NewtonFractal:
    """A class for plotting Newton Fractal for a given function.

    TODO: 1. Explain the process for generating fractals and cite 
    references.
    2. Colours
    3. Newton iteration on top of plot

    Parameters
    ----------
    func : ``sympy`` expression
        The function for which we want to plot fractal (single-
        variable).
    prec_goal : float, optional
        Tolerance for how small the iteration step be relative
        to the point to break the loop for that point i.e. if
        relative difference of the iteration step and the point
        is smaller than this value, it will stop the loop for
        this point.
    nmax : int, optional
        Number of iterations to be run (default is 200). 
        Minimum recommended value is 50, but for some functions
        may required over 500.
    
    Attributes
    ----------
    function : :obj:`fractpy.Function`
        The function for which the Newton Fractal is being
        generated.
    
    See Also
    --------
    fractpy.Function : 
        A class for performing basic calculus operations on
        a function (like finding roots).

    """
    
    def __init__(self, func, prec_goal=1.e-11, nmax=200):
        self.function = func
        self._precision_goal = prec_goal
        self.n = nmax # Number of iterations

    def __repr__(self):
        return f"### FractPy Model ###\nType: Newton Fractal\nFunction: {self.function}"

    @property
    def function(self):
        return self._function
    
    @function.setter
    def function(self, func):
        self._function = Function(func)
        self._roots_list = self._function.roots()
        self._newton_step = self._function._rd_python_function()

    @property
    def roots_list(self):
        return self._roots_list
    
    def _make_list(self):
        """Makes a list of all the points in the plane.
        Has to be called after assigning xvals and yvals.
        """
        self._z_list = []
        for a in self._xvals:
            for b in self._yvals:
                self._z_list.append(a + 1j * b)
                
    def _match_root(self):
        """Matches the point to the root to which it converges."""
        findgoal = 1.e-10 * np.ones(len(self._z_list))
        rootid = -1 * np.ones(len(self._z_list))
        for r in self.roots_list:
            # Check for closeness to each root in the list
            rootid = np.where(np.abs(self._z_list - r * np.ones(len(self._z_list))) < findgoal, 
                              np.ones(len(self._z_list)) * self.roots_list.index(r), rootid)
            
        return rootid
                
    def _prepare_plot(self, xstart, xend, ystart, yend):
        """Prepares the plot data for the given range."""
        self._xvals = np.linspace(xstart, xend, num=self._width)
        self._yvals = np.linspace(ystart, yend, num=self._height)
        self._make_list()

        # Temporary array to be used for comparision:
        temp_list = np.array(self._z_list)
        # Relative difference of iteration step and the point:
        rel_diff = np.ones(len(self._z_list))
        # This counts number of iteration each point took to converge:
        counter = np.zeros(len(self._z_list)).astype(int)
        overall_counter = 0
        prec_goal_list = np.ones(len(self._z_list)) * self._precision_goal
    
        while any(rel_diff) > self._precision_goal and overall_counter < self.n:
            newton_step = self._newton_step(temp_list)
            self._z_list = temp_list - newton_step
            rel_diff = np.abs(newton_step/temp_list)
            temp_list = self._z_list
            # If smaller then the tolerance then don't count:
            counter = counter + np.greater(rel_diff, prec_goal_list)
            overall_counter += 1
        
        data = self._match_root().astype(int)

        ################################
        #mask = data==-1
        #mask = mask.astype(int)
        #mask = np.reshape(mask, (len(self._xvals), len(self._yvals))).T
        #return mask
        ##################################
        # TODO: Shading of the fractals
        #nroot = nroot - 0.99*np.log(counter/np.max(counter))
        
        data = np.reshape(data, (len(self._xvals), len(self._yvals))).T
        return data

    def _ax_update(self, ax):
        """Updates the plot for the zoomed region."""
        ax.set_autoscale_on(False)  # Otherwise, infinite loop
        # Get the number of points from the number of pixels in the window
        w, h = \
            np.round(ax.patch.get_window_extent().size).astype(int)
        # Set the dimensions ratio similar to the initial values
        if w > h:
            self._height = int(self._width * h / w)
        else:
            self._width = int(self._height * w / h)
        # Get the range for the new area
        vl = ax.viewLim
        extent = vl.x0, vl.x1, vl.y0, vl.y1
        # Update the image object with our new data and extent
        im = ax.images[-1]
        im.set_data(self._prepare_plot(*extent))
        im.set_extent(extent)
        ax.figure.canvas.draw_idle()
    
    def plot(self, xstart, xend, ystart, yend, dim=(100, 100)):
        """Plots the fractal for given range and dimensions.

        Parameters
        ----------
        xstart : float
            Lower limit of x-axis
        xend : float
            Upper limit of x-axis
        ystart : float
            Lower limit of y-axis
        yend : float
            Upper limit of y-axis
        dim : list of int, optional
            The dimensions of the plot to be generated (resolution
            of the plot, width X height)(default is (100, 100)).
        """
        self._width = dim[0]
        self._height = dim[1]
        
        plt.figure(figsize=(10, 10))
        plt.matshow(self._prepare_plot(xstart, xend, ystart, yend), fignum=1, origin='lower')
        plt.colorbar()
        plt.show()

    def zoom_plot(self, xstart, xend, ystart, yend, dim=(100, 100)):
        """Plots the fractal in two identical panels. Zooming in
        on the right panel will show a rectangle in the first
        panel, denoting the zoomed region.

        Parameters
        ----------
        xstart : float
            Lower limit of x-axis
        xend : float
            Upper limit of x-axis
        ystart : float
            Lower limit of y-axis
        yend : float
            Upper limit of y-axis
        dim : list of int, optional
            The dimensions of the plot to be generated (resolution
            of the plot, width X height)(default is (100, 100)).
        """
        self._width = dim[0]
        self._height = dim[1]
        Z = self._prepare_plot(xstart, xend, ystart, yend)

        fig1, (ax1, ax2) = plt.subplots(1, 2)
        ax1.imshow(Z, origin='lower',
                extent=(self._xvals.min(), self._xvals.max(), self._yvals.min(), self._yvals.max()))
        ax2.imshow(Z, origin='lower',
                extent=(self._xvals.min(), self._xvals.max(), self._yvals.min(), self._yvals.max()))

        
        rect.set_bounds(*ax2.viewLim.bounds)
        ax1.add_patch(rect)

        # Connect for changing the view limits
        ax2.callbacks.connect('xlim_changed', rect)
        ax2.callbacks.connect('ylim_changed', rect)

        ax2.callbacks.connect('xlim_changed', self._ax_update)
        ax2.callbacks.connect('ylim_changed', self._ax_update)
        ax2.set_title("Zoom here")

        plt.show()

