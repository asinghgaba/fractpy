"""This class is used for plotting zoom_plot in fractals."""
from matplotlib.patches import Rectangle


class UpdatingRect(Rectangle):
    def __call__(self, ax):
        self.set_bounds(*ax.viewLim.bounds)
        ax.figure.canvas.draw_idle()