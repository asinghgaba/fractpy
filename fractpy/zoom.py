"""This class is used for plotting zoom_plot in fractals."""
from matplotlib.patches import Rectangle


class UpdatingRect(Rectangle):  # pragma: no cover
    """This class is used for ``fractpy.models.NewtonFractal.zoom_plot()``."""

    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()
