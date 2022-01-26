import time

import numpy as np
import matplotlib.pyplot as plti

class AnimateScatter():
    """creates an animated scatter plot which can be updated"""
    def __init__(self, scatter_params=None, model_params=None, filename=None, pathsave=None):
        plti.ion()

        self.xmin = scatter_params["constraints"][0] 
        self.xmax = scatter_params["constraints"][1]
        self.ymin = scatter_params["constraints"][0]
        self.ymax = scatter_params["constraints"][1]

        self.fig, self.ax = plti.subplots()

        self.c = scatter_params["colors"]
        self.func = scatter_params["opt_func"]
        self.t = scatter_params["t"]
    
        #add resolution to eliminate whitespace
        self.x = np.arange(self.xmin, self.xmax+scatter_params["r"], scatter_params["r"])
        self.y = np.arange(self.ymin, self.ymax+scatter_params["r"], scatter_params["r"])
        xx, yy = np.meshgrid(self.x, self.y, sparse=True)
        self.z = self.booth(xx,yy)
        self.update(scatter_params["solutions"])
        
        self.model_name=model_params['model_name']
        self.filename=model_params['meta_name']+'_'+str(model_params['epoch'])+'epoch_'+filename
        self.pathsave=pathsave

    def booth(self, X, Y):
        return ((X)+(2.0*Y)-7.0)**2+((2.0*X)+(Y)-5.0)**2

    def draw_background(self):
        """draw filled contour of function meshgrid"""
        self.ax.contourf( self.x, self.y, self.z)

    def update_canvas(self):
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
    
    def save_plot(self):
        plti.savefig(self.pathsave + "scatter/"+self.model_name+"/"+self.filename + ".png")

    def update(self, pos):
        pos=np.stack(pos)
        self.ax.clear()
        self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        self.draw_background()
        self.ax.scatter(pos[:,0], pos[:,1], s=30, c=self.c)
        self.update_canvas()
        time.sleep(self.t)


