import tkinter as tk
from tkinter import ttk


class InputFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.name_input = tk.StringVar()
        self.email1_input = tk.StringVar()
        self.email2_input = tk.StringVar()
        self.selected_year = tk.IntVar()

        self.columnconfigure(0, weight=1)

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
        wish_1_label.grid(column=0, row=8, sticky="W", columnspan=2)
        wish_1_entry = tk.Text(self, height=2, width=35)
        wish_1_entry.grid(column=0, row=9, sticky="W", columnspan=2)
        wish_2_label = ttk.Label(self, text="Antrasis noras:")
        wish_2_label.grid(column=0, row=10, sticky="W")
        wish_2_entry = tk.Text(self, height=2, width=35)
        wish_2_entry.grid(column=0, row=11, sticky="W")
        wish_3_label = ttk.Label(self, text="Trečiasis noras")
        wish_3_label.grid(column=0, row=12, sticky="W")
        wish_3_entry = tk.Text(self, height=2, width=35)
        wish_3_entry.grid(column=0, row=13, sticky="W")

        self.wish_1 = wish_1_entry.get("1.0", "end")
        self.wish_2 = wish_2_entry.get("1.0", "end")
        self.wish_3 = wish_3_entry.get("1.0", "end")

        button_frame = ttk.Frame(self)
        button_frame.grid(column=0, row=14, sticky="EW", pady=15)
        button_frame.columnconfigure((0, 1), weight=1)

        confirm_button = ttk.Button(button_frame, text="Pateikti")
        confirm_button.grid(column=0, row=0)
        exit_button = ttk.Button(button_frame, text="Išeiti")
        exit_button.grid(column=1, row=0)
