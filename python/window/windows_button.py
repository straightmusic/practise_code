import tkinter as tk

def hello():
    print("Hello World!!")

window = tk.Tk();
window.title("Hello World")
window.geometry("300x100+250+150")

button = tk.Button(window,
                    text = "Hello",
                    command = hello)

button.pack()

window.mainloop()
