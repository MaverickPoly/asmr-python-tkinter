import tkinter as tk
from tkinter import ttk
import datetime



def show_time():
    time = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
    label.configure(text=time)
    window.after(1000, show_time)


def func(event):
    print(event)


def motion(event):
    print(event)
    print(type(event))


window = tk.Tk()
window.title("Digital Clock")
window.geometry("600x700")

# Tabs
notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

notebook.pack(expand=True, fill='both')

# Tab1
label = tk.Label(tab1, font=("Comicsans", 50))
label.pack(expand=True)
show_time()

# Tab2
tk.Button(tab2, text="TK Button", command=func).pack(expand=True)
ttk.Button(tab2, text="TTK Button", command=func).pack(expand=True)

window.bind("<Motion>", motion)
window.bind("<Button>", motion)


window.mainloop()
