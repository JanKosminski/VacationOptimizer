import tkinter as tk

WHITE = "#ffffff"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


def gui(function, *kwargs):
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
    run_button = tk.Button(text="Run", bg=WHITE, command=lambda: function(*kwargs, capacity=int(days_input.get())),
                           width=10)
    run_button.grid(column=1, row=1, sticky="e")
    # output lablel
    output = tk.Label(text="", bg=WHITE)
    output.grid(column=0, row=2, sticky="w")

    window.mainloop()
