from importlib.metadata import entry_points
import tkinter as tk

def onOK():
    print("Hello {}.".format(entry.get()))

window = tk.Tk()
window.title("Hello World")
window.geometry("300x100+250+150")

label = tk.Label(window, text="姓名")
label.pack()

entry = tk.Entry(window, width=20)
entry.pack()

button = tk.Button(window, text="OK", command=onOK)
button.pack()

window.mainloop()