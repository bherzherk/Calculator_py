#!/usr/bin/env python3
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.display = tk.Entry(self.master, width=15, font=("Arial", 32), bd=10, insertwidth=1, bg="#6fa54d")
        self.display.grid(row=0, column=0)

root = tk.Tk()
root.title("Calculator")
my_app = Calculator(root)
root.mainloop()