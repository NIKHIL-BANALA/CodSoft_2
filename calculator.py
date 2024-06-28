import tkinter as tk
from math import sqrt, factorial

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "<_":
        entry.delete(len(entry.get()) - 1, tk.END)
    elif text == "!":
        try:
            num = int(entry.get())
            result = str(factorial(num))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "√":
        try:
            num = float(entry.get())
            result = str(sqrt(num))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#f5f5f5")
root.geometry("400x500")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

mainframe = tk.Frame(root, bg="#f5f5f5")
mainframe.grid(sticky="nsew")
mainframe.grid_rowconfigure(0, weight=1)
mainframe.grid_rowconfigure(1, weight=1)
mainframe.grid_rowconfigure(2, weight=1)
mainframe.grid_rowconfigure(3, weight=1)
mainframe.grid_rowconfigure(4, weight=1)
mainframe.grid_rowconfigure(5, weight=1)
mainframe.grid_columnconfigure(0, weight=1)
mainframe.grid_columnconfigure(1, weight=1)
mainframe.grid_columnconfigure(2, weight=1)
mainframe.grid_columnconfigure(3, weight=1)

entry = tk.Entry(mainframe, font=("Helvetica", 20), bd=10, insertwidth=4, width=14, borderwidth=4, relief="flat")
entry.grid(row=0, column=0, columnspan=4, pady=20, sticky="nsew")

buttons = [
    ("C", 1, 0), ("√", 1, 1), ("/", 1, 2), ("<_", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("!", 5, 0), ("0", 5, 1), (".", 5, 2), ("=", 5, 3)
]

def create_rounded_button(parent, text, row, col):
    button = tk.Button(parent, text=text, font=("Helvetica", 20), bd=0, relief="flat")
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", on_button_click)
    button.configure(bg="#ffffff", fg="#000000", activebackground="#c0c0c0", activeforeground="#000000")
    button.bind("<Enter>", lambda e: e.widget.configure(bg="#c0c0c0"))
    button.bind("<Leave>", lambda e: e.widget.configure(bg="#ffffff"))
    return button

for (text, row, col) in buttons:
    create_rounded_button(mainframe, text, row, col)

root.mainloop()
