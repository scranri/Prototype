from tkinter import ttk, messagebox
import tkinter as tk


class SignInFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        signin_frame = tk.Frame(root)
        signin_frame.pack(anchor='center', fill='both')

        self.username_label = tk.Label(signin_frame, text='Username: ')
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(signin_frame, width=15)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(signin_frame, text='Password: ')
        self.password_label.grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(signin_frame, width=15)
        self.password_entry.grid(row=1, column=1)
