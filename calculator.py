#!/usr/bin/env python3
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.display = tk.Entry(self.master, width=15, font=("Arial", 32), bd=10, insertwidth=1, bg="#6fa54d", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        row = 1
        col = 0

        buttons = [
            "(", ")", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "C", "0", ".", "="
        ]

        for button in buttons:
            self.build_button(button, row, col)
            col += 1

            if col>3:
                col=0
                row += 1

    def build_button(self, button, row, col):
        butt = tk.Button(self.master, text=button, width=7, font=("Verdana", 14))
        butt.grid(row=row, column=col)

root = tk.Tk()
root.title("Calculator")
root.resizable(width=False, height=False)
my_app = Calculator(root)
root.mainloop()