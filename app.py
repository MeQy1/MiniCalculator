import tkinter as tk
from functools import partial
from tkinter import messagebox

BUTTON_POS = "nsew"
BUTTON_BACKGROUND_COLOR = "#e9edc9"
BUTTON_TEXT_COLOR = "black"
BUTTON_TEXT_SIZE = "12"
BUTTON_RELIEF = "flat"
APP_FONT = ("Times new roman",12,"italic","bold")


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
        self.configure(bg="#e9edc9")


        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        for el in range(0, 7):
            self.grid_rowconfigure(el, weight=1)

        self.label = tk.Label(self, text="Calculator", font=APP_FONT,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR)
        self.label.grid(row=0, column=1, sticky="nsew")

        self.results = tk.Label(self, text="0", font=APP_FONT,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR)
        self.results.grid(row=1, column=1, sticky="nswe")


        self.button = tk.Button(self, text="1",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_number,1))
        self.button.grid(row=2, column=0, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="2",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_number,2))
        self.button.grid(row=2, column=1, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="3",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_number,3))
        self.button.grid(row=2, column=2, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="4",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_number,4))
        self.button.grid(row=3, column=0, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="5",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_number,5))
        self.button.grid(row=3, column=1, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="6",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_number,6))
        self.button.grid(row=3, column=2, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="7",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_number, 7))
        self.button.grid(row=4, column=0, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="8",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_number, 8))
        self.button.grid(row=4, column=1, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="9",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_number, 9))
        self.button.grid(row=4, column=2, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="0",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_number, 0))
        self.button.grid(row=5, column=1, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="+",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_operator, "+"))
        self.button.grid(row=5, column=0, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="-",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_operator, "-"))
        self.button.grid(row=5, column=2, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="*",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_operator, "*"))
        self.button.grid(row=6, column=0, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="/",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=partial(self.button_clicked_operator, "/"))
        self.button.grid(row=6, column=1, sticky=BUTTON_POS)

        self.button = tk.Button(self, text="=",font=APP_FONT,relief=BUTTON_RELIEF,bg = BUTTON_BACKGROUND_COLOR,fg=BUTTON_TEXT_COLOR, command=self.calculate)
        self.button.grid(row=6, column=2, sticky=BUTTON_POS)



    def button_clicked_number(self, number):
        if not self.operator_pressed:
            if self.value_a > 10000000:
                return
            self.value_a *= 10
            self.value_a += number
            self.results.configure(text=str(self.value_a))
        else:
            if self.value_b > 10000000:
                return
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

        if self.result > 1000000000:
            messagebox.showerror("Error", "Sorry man i cant 😓😓😓😓😓😓 math is hard yk")
            self.result = self.value_a
            self.value_b = 0
            self.results.configure(text=str(self.result))
            return

        self.value_a = self.result
        self.value_b = 0
        self.results.configure(text=str(self.result))




