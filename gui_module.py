import tkinter as tk
from functions import *


class VacationApp:
    def __init__(self, function, **kwargs):
        self.function = function
        self.args = kwargs
        self.white = "#ffffff"

        self.window = tk.Tk()
        self.window.title("Vacation Optimizer")
        self.window.config(padx=20, pady=20, bg=self.white)

        self._setup_ui()
        self.window.mainloop()

    def _setup_ui(self):
        desc = tk.Label(text="Input the available vacation days", bg=self.white)
        desc.grid(column=0, row=0, sticky="w", columnspan=2)

        self.days_input = tk.Entry(width=28)
        self.days_input.grid(column=0, row=1, sticky="w")
        self.days_input.insert(0, "20")

        run_button = tk.Button(text="Run", bg=self.white, command=self.run_optimization, width=10)
        run_button.grid(column=1, row=1, sticky="e")

        self.output = tk.Label(text="", bg=self.white, justify="left")
        self.output.grid(column=0, row=2, sticky="w")

    def run_optimization(self):
        try:
            capacity = int(self.days_input.get())
        except ValueError:
            self.output.config(text="Invalid input. Integer required.")
            return

        a = self.function(self.args["arr"], capacity=capacity)
        b = print_solution(a, self.args['calendar'], self.args['org_indexes'])
        self.output.config(text=b)


def gui(function, **args):
    app = VacationApp(function, **args)