import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
import ttk

import numpy as np
from sweep import Simulator


LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(10, 10), dpi=100)
a = f.add_subplot(111)

def animate(i):
    
    a.clear()
    fmcw = Simulator([20, 30, 40, 45], [15, 18, 22, 24, 27], [85, 35, 25, 20], 40)
    signal = fmcw.extract_movement()
    a.plot(signal)

class App(tk.Tk):

    """Docstring for App. """

    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "Simulator")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        frame = MainPage(container, self)
        self.frame = frame
        frame.grid(row=0, column=0, sticky="nsew")

class MainPage(tk.Frame):

    """Docstring for Main. """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()

        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

app = App()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
        

