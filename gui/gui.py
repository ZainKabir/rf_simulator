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
from localize import solve

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(10, 10), dpi=100)
a1 = f.add_subplot(311)
a2 = f.add_subplot(312)
a3 = f.add_subplot(313)
fmcw = Simulator([20, 30, 40, 45], [85, 35, 25, 20])

def animate(i):
    
    a1.clear(); a2.clear(); a3.clear()
    a1.set_title('TOF Profile of Antenna 1') 
    a2.set_title('TOF Profile of Antenna 2')
    a3.set_title('Localized Coordinates')
    
    s1, tof1 = fmcw.set_params([15, 18, 22, 24, 27], 40, extract=True)
    s2, tof2 = fmcw.set_params([15, 18, 22, 24, 27], 40, extract=True)
    t1 = np.mean([15, 18, 22, 24, 27])
    t2 = np.mean([15, 18, 22, 24, 27])
    c = solve(t1, t2)
    
    print c

    # Plots TOFs
    a1.plot(s1)   
    a2.plot(s2)
    # Add reference antennas
    a3.plot(0, 0, 'xr')
    a3.plot(1, 0, 'xr')
    a3.plot(-1, 0, 'xr')
    # Add localized coordinates
    a3.plot(c[0], c[1], 'or')
    a3.set_xlim(-5, 5)
    a3.set_ylim(-2, 5)

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
        

