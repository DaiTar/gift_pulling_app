from tkinter import ttk


class ActionFrame(ttk.Frame):
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
