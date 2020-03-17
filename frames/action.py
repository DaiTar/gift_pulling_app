from tkinter import ttk


class ActionFrame(ttk.Frame):
    def __init__(self, parent, controller, show_input):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        button_container = ttk.Frame(self, padding=50)
        button_container.grid(column=0, row=0, sticky="NSEW")

        button_container.columnconfigure(0, weight=1)
        button_container.rowconfigure((0, 1, 2), weight=1)

        first_button = ttk.Button(button_container,
                                  text="Norų pateikimas",
                                  command=show_input,
                                  cursor="hand2")
        first_button.grid(column=0, row=0, sticky="NSEW")
        second_button = ttk.Button(button_container,
                                   text="Dovanų traukimas",
                                   cursor="hand2")
        second_button.grid(column=0, row=1, pady=50, sticky="NSEW")
        third_button = ttk.Button(button_container,
                                  text="Išeiti",
                                  command=controller.destroy,
                                  cursor="hand2")
        third_button.grid(column=0, row=2, sticky="NSEW")
