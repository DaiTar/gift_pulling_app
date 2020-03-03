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

        start_frame = MainFrame(container, self)
        start_frame.grid(column=0, row=0, sticky="NSEW", pady=50, padx=50)


class MainFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2), weight=1)

        first_button = ttk.Button(self, text="Norų pateikimas")
        first_button.grid(column=0, row=0, sticky="NSEW")
        second_button = ttk.Button(self, text="Dovanų traukimas")
        second_button.grid(column=0, row=1, pady=50, sticky="NSEW")
        third_button = ttk.Button(self, text="Išeiti", command=self.controller.destroy)
        third_button.grid(column=0, row=2, sticky="NSEW")


root = GiftApp()
root.mainloop()
