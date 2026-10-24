import tkinter as tk
from functools import partial


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
        self.resizable(width=False, height=False)

        self.label = tk.Label(self, text="Calculator", font=("Arial", 12))
        self.label.grid(row=0, column=0, sticky="nsew")

        self.results = tk.Label(self, text="0", font=("Arial", 12))
        self.results.grid(row=1, column=0, sticky="nsew")

        self.button = tk.Button(self, text="Calculate", )
        self.button.grid(row=2, column=0, sticky="nsew")

        self.button = tk.Button(self, text="1", command=partial(self.button_clicked_number,1))
        self.button.grid(row=2, column=1, sticky="nsew")

        self.button = tk.Button(self, text="2", command=partial(self.button_clicked_number,2))
        self.button.grid(row=2, column=2, sticky="nsew")

        self.button = tk.Button(self, text="3", command=partial(self.button_clicked_number,3))
        self.button.grid(row=2, column=3, sticky="nsew")

        self.button = tk.Button(self, text="4", command=partial(self.button_clicked_number,4))
        self.button.grid(row=3, column=1, sticky="nsew")

        self.button = tk.Button(self, text="5", command=partial(self.button_clicked_number,5))
        self.button.grid(row=3, column=2, sticky="nsew")

        self.button = tk.Button(self, text="6", command=partial(self.button_clicked_number,6))
        self.button.grid(row=3, column=3, sticky="nsew")

        self.button = tk.Button(self, text="7", command=partial(self.button_clicked_number, 7))
        self.button.grid(row=4, column=1, sticky="nsew")

        self.button = tk.Button(self, text="8", command=partial(self.button_clicked_number, 8))
        self.button.grid(row=4, column=2, sticky="nsew")

        self.button = tk.Button(self, text="9", command=partial(self.button_clicked_number, 9))
        self.button.grid(row=4, column=3, sticky="nsew")

        self.button = tk.Button(self, text="0", command=partial(self.button_clicked_number, 0))
        self.button.grid(row=5, column=2, sticky="nsew")



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
            self.result = self.value_a / self.value_b



