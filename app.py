import tkinter as tk
from tkinter import ttk


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text box")

root = MainApp()

root.mainloop()
