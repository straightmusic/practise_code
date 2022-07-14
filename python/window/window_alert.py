import tkinter as tk
import tkinter.messagebox

def onOK():
    msg = "Hello, {}.".format(entry.get())
    tkinter.messagebox.showinfo(title="alert box", message=msg)

window=tk.Tk()
window.title("window_alert.py")
window.geometry("300x100+250+150")

label = tk.Label(window, text="姓名")
label.pack()

entry = tk.Entry(window, width=20)
entry.pack()

button= tk.Button(window, text="OK", command=onOK)
button.pack()

window.mainloop()