import tkinter as tk
from tkinter import ttk
from frames import ActionFrame, InputFrame


class GiftApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gift App")
        self.geometry("400x450")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        container = ttk.Frame(self)
        container.grid(sticky="NSEW")
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        start_frame = ActionFrame(container, self)
        start_frame.grid(column=0, row=0, sticky="NSEW", pady=50, padx=50)
        input_frame = InputFrame(container)
        input_frame.grid(column=0, row=0, sticky="NSEW", pady=30, padx=30)


root = GiftApp()
root.mainloop()
