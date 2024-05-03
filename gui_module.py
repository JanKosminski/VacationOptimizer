import tkinter as tk
from functions import *

WHITE = "#ffffff"
FONT_NAME = "Courier"


def gui(function, **args):

    def callback(funct, **c_args):
        # that's illegal but who cares
        a = funct(c_args["arr"], capacity=int(days_input.get()))
        b = print_solution(a, c_args['calendar'], c_args['org_indexes'])
        output.config(text=b)

    # innit window
    window = tk.Tk()
    window.title("Vacation Optimizer")

    window.config(padx=20, pady=20, bg=WHITE)

    # Input the available vacation days
    desc = tk.Label(text="Input the available vacation days", bg=WHITE)
    days_input = tk.Entry(width=28)
    desc.grid(column=0, row=0, sticky="w", columnspan=2)
    days_input.grid(column=0, row=1, sticky="w")
    days_input.insert(0, "20")
    # Run the code
    run_button = tk.Button(text="Run", bg=WHITE, command=lambda: callback(function, **args),
                           width=10) # more illegal code
    run_button.grid(column=1, row=1, sticky="e")
    # output label
    output = tk.Label(text="", bg=WHITE, justify="left")
    output.grid(column=0, row=2, sticky="w")

    window.mainloop()

