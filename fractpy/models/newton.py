
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

from ..zoom import UpdatingRect
from ..calculus import Function








rect = UpdatingRect(
            [0, 0], 0, 0, facecolor='none', edgecolor='black', linewidth=1.0)







class NewtonFractal:
    '''A class for plotting Newton Fractal for a given function.

    height and width: Dimensions for the image (pixels)
    rel_diff: Function calculating realtive difference i.e. f(x)/f'(x)
    rl: Roots list
    prec_goal: Precision Goal
    nmax: Number of iterations
    '''
    
    def __init__(self, height, width, f, variable, prec_goal, nmax):
        self.height = height
        self.width = width
        
        self.precision_goal = prec_goal
        self.n = nmax

        #self.f = f

        self.func = Function(f, variable)
        self.roots_list = self.func.calculate_roots()
        self.relative_difference = self.func.rd_pfunction()
       
    
    #def _make_func_class(self, f, variable):
        #return Function(f, variable)
    
    def _make_list(self):
        '''Makes a list of all the coordinates.'''
        self.z_list = []
        for a in self.xvals:
            for b in self.yvals:
                self.z_list.append(a + 1j * b)
                
    def _id_root(self):
        '''Matches the point to the root to which it converges'''
        findgoal = 1.e-10 * np.ones(len(self.z_list))
        rootid = -1 * np.ones(len(self.z_list))
        for r in self.roots_list:
            # check for closeness to each root in the list
            rootid = np.where(np.abs(self.z_list - r * np.ones(len(self.z_list))) < findgoal, 
                              np.ones(len(self.z_list)) * self.roots_list.index(r), rootid)
            
        return rootid
                
    def prepare_plot(self, xstart, xend, ystart, yend):
        
        self.xvals = np.linspace(xstart, xend, num=self.width)
        self.yvals = np.linspace(ystart, yend, num=self.height)
        
        self._make_list()

        temp_list = np.array(self.z_list)
        rel_diff = np.ones(len(self.z_list))
        counter = np.zeros(len(self.z_list)).astype(int)
    
        overall_counter = 0
        prec_goal_list = np.ones(len(self.z_list)) * self.precision_goal
    
        while any(rel_diff) > self.precision_goal and overall_counter < self.n:
            diff = self.relative_difference(temp_list)
            self.z_list = temp_list - diff
            rel_diff = np.abs(diff/temp_list)
        
            temp_list = self.z_list
        
            counter = counter + np.greater(rel_diff, prec_goal_list)
        
            overall_counter += 1
        
        
        nroot = self._id_root().astype(int)
        
        #nroot = nroot - 0.99*np.log(counter/np.max(counter))
        
        self.data_contour = np.reshape(nroot, (len(self.xvals), len(self.yvals))).T

        return self.data_contour
        
    def ax_update(self, ax):
        ax.set_autoscale_on(False)  # Otherwise, infinite loop
        # Get the number of points from the number of pixels in the window
        w, h = \
            np.round(ax.patch.get_window_extent().size).astype(int)

        if w > h:
            self.height = int(self.width * h / w)
        else:
            self.width = int(self.height * w / h)
        # Get the range for the new area
        vl = ax.viewLim
        extent = vl.x0, vl.x1, vl.y0, vl.y1
        # Update the image object with our new data and extent
        im = ax.images[-1]
        im.set_data(self.prepare_plot(*extent))
        im.set_extent(extent)
        ax.figure.canvas.draw_idle()
    
    def plot_fractal(self):
        
        self.prepare_plot()
        
        plt.figure(figsize=(10, 10))
        plt.matshow(self.data_contour, fignum=1, origin='lower', cmap='hsv')
        plt.colorbar()

    def zoom_plot(self, xstart, xend, ystart, yend):
        Z = self.prepare_plot(xstart, xend, ystart, yend)

        fig1, (ax1, ax2) = plt.subplots(1, 2)
        ax1.imshow(Z, origin='lower',
                extent=(self.xvals.min(), self.xvals.max(), self.yvals.min(), self.yvals.max()))
        ax2.imshow(Z, origin='lower',
                extent=(self.xvals.min(), self.xvals.max(), self.yvals.min(), self.yvals.max()))

        
        rect.set_bounds(*ax2.viewLim.bounds)
        ax1.add_patch(rect)

        # Connect for changing the view limits
        ax2.callbacks.connect('xlim_changed', rect)
        ax2.callbacks.connect('ylim_changed', rect)

        ax2.callbacks.connect('xlim_changed', self.ax_update)
        ax2.callbacks.connect('ylim_changed', self.ax_update)
        ax2.set_title("Zoom here")

        plt.show()




#x = sym.Symbol('x')
#func = (x**2 - 1) * (x**2 + 1)
#f = Function(func, x)

#md = NewtonFractal(100, 100, func, x, prec_goal, nmax)
#md.zoom_plot(-2, 2, -2, 2)