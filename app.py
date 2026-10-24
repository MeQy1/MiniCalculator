import tkinter as tk
from functools import partial
from tkinter import messagebox

BUTTON_POS = "nsew"
BUTTON_COLOR = "black"
BUTTON_BACKGROUND_COLOR = "white"
BUTTON_TEXT_COLOR = "black"
BUTTON_TEXT_SIZE = "12"


class App(tk.Tk):
    operator_pressed = False
    operator = ""
    result = 0
    value_a = 0
    value_b = 0
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x700")
        self.resizable(0, 0)


        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        for el in range(0, 7):
            self.grid_rowconfigure(el, weight=1)

        self.label = tk.Label(self, text="Calculator", font=("Arial", 12))
        self.label.grid(row=0, column=1, sticky="nsew")

        self.results = tk.Label(self, text="0", font=("Arial", 12))
        self.results.grid(row=1, column=1, sticky="nswe")


        self.button = tk.Button(self, text="1", command=partial(self.button_clicked_number,1))
        self.button.grid(row=2, column=0, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="2", command=partial(self.button_clicked_number,2))
        self.button.grid(row=2, column=1, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="3", command=partial(self.button_clicked_number,3))
        self.button.grid(row=2, column=2, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="4", command=partial(self.button_clicked_number,4))
        self.button.grid(row=3, column=0, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="5", command=partial(self.button_clicked_number,5))
        self.button.grid(row=3, column=1, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="6", command=partial(self.button_clicked_number,6))
        self.button.grid(row=3, column=2, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="7", command=partial(self.button_clicked_number, 7))
        self.button.grid(row=4, column=0, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="8", command=partial(self.button_clicked_number, 8))
        self.button.grid(row=4, column=1, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="9", command=partial(self.button_clicked_number, 9))
        self.button.grid(row=4, column=2, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="0", command=partial(self.button_clicked_number, 0))
        self.button.grid(row=5, column=1, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="+", command=partial(self.button_clicked_operator, "+"))
        self.button.grid(row=5, column=0, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="-", command=partial(self.button_clicked_operator, "-"))
        self.button.grid(row=5, column=2, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="*", command=partial(self.button_clicked_operator, "*"))
        self.button.grid(row=6, column=0, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="/", command=partial(self.button_clicked_operator, "/"))
        self.button.grid(row=6, column=1, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="=",command=self.calculate)
        self.button.grid(row=6, column=2, sticky=BUTTON_POS)



    def button_clicked_number(self, number):
        if not self.operator_pressed:
            self.value_a *= 10
            self.value_a += number
            self.results.configure(text=str(self.value_a))
        else:
            self.value_b *= 10
            self.value_b += number
            self.results.configure(text=str(self.value_b))



    def button_clicked_operator(self, operator):
        if self.operator_pressed and self.value_b != 0:
            self.calculate()

        self.operator_pressed = True
        self.operator = operator

    def calculate(self):
        self.operator_pressed = False
        if self.operator == "+":
            self.result = self.value_a + self.value_b
        elif self.operator == "-":
            self.result = self.value_a - self.value_b
        elif self.operator == "*":
            self.result = self.value_a * self.value_b
        elif self.operator == "/":
            if self.value_b == 0:
                messagebox.showerror("Error", "Operator cannot be divided by zero")
            else:
                self.result = self.value_a / self.value_b

        self.value_a = self.result
        self.value_b = 0
        self.results.configure(text=str(self.result))




