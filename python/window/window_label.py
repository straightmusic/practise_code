import tkinter as tk

window = tk.Tk()
window.title("Hello World")
window.geometry("300x300+250+150")

label = tk.Label(window, 
    text="Hello, World!!",
    bg="#EEBB00",
    font=("Arial, 12"),
    width=15,
    height=2
)
label.pack()

window.mainloop()