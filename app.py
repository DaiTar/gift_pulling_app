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

        self.frames = dict()

        action_frame = ActionFrame(container, self, lambda: self.show_frame(InputFrame))
        action_frame.grid(column=0, row=0, sticky="NSEW")
        input_frame = InputFrame(container, lambda: self.show_frame(ActionFrame))
        input_frame.grid(column=0, row=0, sticky="NSEW")

        self.frames[ActionFrame] = action_frame
        self.frames[InputFrame] = input_frame

        self.show_frame(ActionFrame)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


root = GiftApp()
root.mainloop()
