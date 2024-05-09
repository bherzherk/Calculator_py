#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        self.display = tk.Entry(self.master, width=15, font=("Arial", 32), bd=10, insertwidth=1, bg="#6fa54d", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)
        self.current = ''
        self.operation_verif = False
        self.op = ''
        self.total = 0.0

        row = 1
        col = 0

        buttons = [
            "sqrt", "pwr2", "%", "/",
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

        self.master.bind("<Key>", self.key_press)
    
    def key_press(self, event):
        key = event.char

        if key == "\r": #enter
            self.compute()
            return
        elif key == "\x08": # backspace
            self.clear_display()
            return
        elif key == "p":
            self.power_2()
        elif key == "s":
            self.square_root()
        elif key in "1234567890" or key == "%" or key == "." or key in "+-/*":
            self.press_but(key)


    def clear_display(self):
        self.display.delete(0, "end")
        self.current = ''
        self.operation_verif = False
        self.op = ''
        self.total = 0.0

    def compute(self):
        if self.current and self.op:
            if self.op == "+":
                self.total += float(self.current)
            elif self.op == "-":
                self.total -= float(self.current)
            elif self.op == "*":
                self.total *= float(self.current)
            elif self.op == "/":
                self.total /= float(self.current)
            elif self.op == "%":
                self.total = (self.total*float(self.current))/100


        self.display.delete(0, "end")
        self.display.insert("end", self.total)

    def power_2(self):
        if self.operation_verif:
            self.operation_verif = False

        if self.current:
            self.total = float(self.current)
            self.total = self.total**2
        
        self.current = ''
        self.display.delete(0, "end")
        self.display.insert("end", self.total)
    
    def square_root(self):
        if self.operation_verif:
            self.operation_verif = False

        if self.current:
            self.total = float(self.current)
            self.total = self.total**0.5
        self.current = ''

        self.display.delete(0, "end")
        self.display.insert("end", self.total)

    def press_but(self, key):
        if self.operation_verif:
            self.operation_verif = False

        self.display.insert("end", key)

        if key in "1234567890" or key == ".":
            self.current += key
        else:
            if self.current:
                if not self.op:
                    self.total = float(self.current)
                self.current = ''
        
            self.operation_verif = True
            self.op = key

    def build_button(self, button, row, col):
        my_cmd = None
        if button == "C":
            my_cmd = lambda: self.clear_display()
        elif button == "=":
            my_cmd = lambda: self.compute()
        elif button == "pwr2":
            my_cmd = lambda: self.power_2()
        elif button == "sqrt":
            my_cmd = lambda: self.square_root()
        else:
            my_cmd = lambda: self.press_but(button)

        butt = tk.Button(self.master, text=button, width=7, command=my_cmd, font=("Verdana", 14))
        butt.grid(row=row, column=col)

root = tk.Tk()
messagebox.showinfo("Instructions", "WELCOME\n Here some instruction when use kwyboard \nEnter: = \nBackspace: C \np: pwr2 \ns: sqrt")
root.title("Calculator")
root.resizable(width=False, height=False)
my_app = Calculator(root)
root.mainloop()