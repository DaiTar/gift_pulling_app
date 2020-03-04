import tkinter as tk
from tkinter import ttk


class GiftApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gift App")
        self.geometry("400x400")
        self.resizable(False, False)
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

        self.name_input = tk.StringVar()
        self.email1_input = tk.StringVar()
        self.email2_input = tk.StringVar()
        self.selected_year = tk.IntVar()

        name_label = ttk.Label(self, text="Vardas:")
        name_label.grid(column=0, row=0, sticky="W")
        name_entry = ttk.Entry(self, width=20, textvariable=self.name_input)
        name_entry.grid(column=0, row=1, sticky="W")
        name_entry.focus()
        email1_label = ttk.Label(self, text="Elektroninis paštas:")
        email1_label.grid(column=0, row=2, sticky="W")
        email1_entry = ttk.Entry(self, width=40, textvariable=self.email1_input)
        email1_entry.grid(column=0, row=3, sticky="W")
        email2_label = ttk.Label(self, text="Pakartoti elektroninį paštą:")
        email2_label.grid(column=0, row=4, sticky="W")
        email2_entry = ttk.Entry(self, width=40, textvariable=self.email2_input)
        email2_entry.grid(column=0, row=5, sticky="W")
        year_label = ttk.Label(self, text="Metai:")
        year_label.grid(column=0, row=6, sticky="W")
        year_selection = ttk.Combobox(self,
                                      textvariable=self.selected_year,
                                      values=(2020, 2021, 2022, 2023, 2024, 2025, 2026),
                                      state="readonly")
        year_selection.current(0)
        year_selection.grid(column=0, row=7, sticky="W")
        wish_1_label = ttk.Label(self, text="Pirmasis noras:")
        wish_1_label.grid(column=0, row=8, sticky="W")
        wish_1_entry = tk.Text(self, height=2, width=35)
        wish_1_entry.grid(column=0, row=9, sticky="W")
        wish_2_label = ttk.Label(self, text="Antrasis noras:")
        wish_2_label.grid(column=0, row=10, sticky="W")
        wish_2_entry = tk.Text(self, height=2, width=35)
        wish_2_entry.grid(column=0, row=11, sticky="W")

        self.wish_1 = wish_1_entry.get("1.0", "end")
        self.wish_2 = wish_2_entry.get("1.0", "end")


root = GiftApp()
root.mainloop()
