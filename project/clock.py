import tkinter as tk
from time import strftime

root = tk.Tk()
root.geometry("200x100")
label = tk.Label(root, font=("ARIAL", 30))
label.pack(expand=True)


def update_clock():  # Renamed the function to avoid shadowing the 'time' module
    string = strftime("%H:%M:%S ")
    label.config(text=string)
    label.after(1000, update_clock)  # Call the renamed function


update_clock()  # Initial call to start the clock update
root.mainloop()  # Corrected: call mainloop as a function
