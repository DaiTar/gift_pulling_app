import tkinter as tk
from tkinter import ttk


class GiftApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gift App")
        self.geometry("400x400")
        self.resizable(0, 0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        container = ttk.Frame(self)
        container.grid(sticky="NSEW")
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        # start_frame = MainFrame(container, self)
        # start_frame.grid(column=0, row=0, sticky="NSEW", pady=50, padx=50)
        input_frame = InputFrame(container)
        input_frame.grid(column=0, row=0, sticky="NSEW", pady=30, padx=30)


class MainFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2), weight=1)

        first_button = ttk.Button(self, text="Norų pateikimas")
        first_button.grid(column=0, row=0, sticky="NSEW")
        second_button = ttk.Button(self, text="Dovanų traukimas")
        second_button.grid(column=0, row=1, pady=50, sticky="NSEW")
        third_button = ttk.Button(self, text="Išeiti", command=controller.destroy)
        third_button.grid(column=0, row=2, sticky="NSEW")


class InputFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.name_input = tk.StringVar

        name_label = ttk.Label(self, text="Vardas: ")
        name_label.grid(column=0, row=0, sticky="W")
        name_entry = ttk.Entry(self, width=15, textvariable=self.name_input)
        name_entry.grid(column=0, row=1)


root = GiftApp()
root.mainloop()
