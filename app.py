import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x700")
        self.resizable(width=False, height=False)

        self.label = tk.Label(self, text="Calculator", font=("Arial", 12))
        self.label.grid(row=0, column=0,sticky="nsew")

        self.label = tk.Label(self, text="0", font=("Arial", 12))
        self.label.grid(row=1, column=0,sticky="nsew")

        self.button = tk.Button(self, text="Calculate",)
        self.button.grid(row=2, column=0,sticky="nsew")
