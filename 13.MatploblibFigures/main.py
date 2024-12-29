import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


window = tk.Tk()
window.title("Matplotlib & Tkinter")

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4, 5], [1, 4, 27, 512, 3125], label="Sample Line")
ax.set_title("Sample Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.legend()

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(expand=True, fill="both")


window.mainloop()

