"""A class for plotting Mandelbrot Fractal."""
import numpy as np
import matplotlib.pyplot as plt

from fractpy.zoom import UpdatingRect


class MandelbrotFractal:
    """A class for plotting Mandelbrot Fractal.

    TODO: more information and relevant papers

    Parameters
    ----------
    
    """

    def __init__(self, thresh=4, power=2, nmax=200):
        self._threshold = thresh
        self._power = power
        self.n = nmax

    def __repr__(self):
        return(
            f"### Fractpy Model ###\n"
            f"Type: Mandelbrot Fractal\n"
        )

    def _make_list(self):
        """Makes a list of all the points in the plane.
        Has to be called after assigning xvals and yvals.
        """
        self._z_list = []
        for a in self._xvals:
            for b in self._yvals:
                self._z_list.append(a + 1j * b)
    
    def _prepare_plot(self, xstart, xend, ystart ,yend):
        """Prepares the plot data for the given range."""
        self._xvals = np.linspace(xstart, xend, num=self._width)
        self._yvals = np.linspace(ystart, yend, num=self._height).reshape(-1, 1)
        self._z_vals = self._xvals + 1.0j * self._yvals

        z = np.ones(self._z_vals.shape) * complex(0, 0)
        # This counts the number of iteration each point took to converge:
        counter = np.zeros(self._z_vals.shape).astype(int)
        overall_counter = 0
        mask = np.ones(self._z_vals.shape, dtype=bool)

        while abs(z).any() < self._threshold and overall_counter < self.n:
            z[mask] = z[mask]**self._power + self._z_vals[mask]
            mask = (np.abs(z) < self._threshold)
            counter += mask
            overall_counter += 1
        # print(counter)
        # data = np.where(abs(z) < temp_list, 0, 1)
        # data = counter
        # data = np.reshape(data, (len(self._xvals), len(self._yvals))).T
        return counter

    def _ax_update(self, ax):  # pragma: no cover
        """Updates the plot for the zoomed region."""
        ax.set_autoscale_on(False)  # Otherwise, infinite loop
        # Get the number of points from the number of pixels in the window
        w, h = np.round(ax.patch.get_window_extent().size).astype(int)
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

        Returns
        -------
        :obj:`matplotlib.figure.Figure`
        """
        self._width = dim[0]
        self._height = dim[1]

        fig, ax = plt.subplots()
        ax.matshow(
            self._prepare_plot(xstart, xend, ystart, yend),
            origin="lower",
            extent=(
                self._xvals.min(),
                self._xvals.max(),
                self._yvals.min(),
                self._yvals.max(),
            ),
        )
        title = f"Mandelbrot Fractal"
        ax.set_title(title)
        plt.tight_layout()

        return fig

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

        Returns
        -------
        :obj:`matplotlib.figure.Figure`
        """
        self._width = dim[0]
        self._height = dim[1]
        Z = self._prepare_plot(xstart, xend, ystart, yend)

        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.matshow(
            Z,
            origin="lower",
            extent=(
                self._xvals.min(),
                self._xvals.max(),
                self._yvals.min(),
                self._yvals.max(),
            ),
        )
        ax2.matshow(
            Z,
            origin="lower",
            extent=(
                self._xvals.min(),
                self._xvals.max(),
                self._yvals.min(),
                self._yvals.max(),
            ),
        )

        rect = UpdatingRect(
            [0, 0], 0, 0, facecolor="none", edgecolor="black", linewidth=1.0
        )
        rect.set_bounds(*ax2.viewLim.bounds)
        ax1.add_patch(rect)

        # Connect for changing the view limits
        ax2.callbacks.connect("xlim_changed", rect)
        ax2.callbacks.connect("ylim_changed", rect)

        ax2.callbacks.connect("xlim_changed", self._ax_update)
        ax2.callbacks.connect("ylim_changed", self._ax_update)
        ax2.set_title("Zoom here")

        title = f"Mandelbrot Fractal"
        fig.suptitle(title)
        plt.tight_layout()

        return fig


