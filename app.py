import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gift app")
root.geometry("400x400")
root.resizable(0, 0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = ttk.Frame(root, padding=50)
main_frame.grid(column=0, row=0, sticky="NSEW")

main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure((0, 1, 2), weight=1)

first_button = ttk.Button(main_frame, text="Norų pateikimas")
first_button.grid(column=0, row=0, sticky="NSEW")
second_button = ttk.Button(main_frame, text="Dovanų traukimas")
second_button.grid(column=0, row=1, pady=50, sticky="NSEW")
third_button = ttk.Button(main_frame, text="Išeiti", command=root.destroy)
third_button.grid(column=0, row=2, sticky="NSEW")

root.mainloop()
