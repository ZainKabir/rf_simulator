import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

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
a = f.add_subplot(211)
a1 = f.add_subplot(212)
fmcw = Simulator([20, 30, 40, 45], [85, 35, 25, 20])

def animate(i):
    
    a.clear(); a1.clear()
    a.set_title('TOF Profile of Antenna 1'); a1.set_title('TOF Profile of Antenna 2')
    signal = fmcw.set_params([15, 18, 22, 24, 27], 40, extract=True)
    a.plot(signal)   
    a1.plot(signal)

class App(tk.Tk):

    """Main App Settings. """

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

    """Main Page to Display Real Time Plots. """

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
        

