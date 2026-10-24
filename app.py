import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x700")
        self.resizable(width=False, height=False)

