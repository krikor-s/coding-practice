
import tkinter as tk

window = tk.Tk()
window.geometry("300x200")
window.title("Counter App")

count = 0

label = tk.Label(window, text = "0")
label.pack()

def increase():
    global count
    count += 1
    label.config(text=str(count))

def decrease():
    global count
    count -= 1
    label.config(text=str(count))

def reset():
    global count
    count = 0
    label.config(text=str(count))

but_i = tk.Button(window, text="Increase", command=increase)
but_i.pack()

but_d = tk.Button(window, text="Decrease", command=decrease)
but_d.pack()

but_r = tk.Button(window, text="Reset", command=reset)
but_r.pack()

window.mainloop()

