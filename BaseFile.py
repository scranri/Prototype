from tkinter import messagebox, ttk
import tkinter as tk
from SignIn import SignInFrame


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(background='#c4f7c1')
        self.menu = MainFrame(self)
        # self.menu.pack(side='left', anchor='n')
        self.menu.pack(side='top', anchor='w')

        self.current_frame = SignInFrame(self)
        # self.current_frame.pack(side='top', anchor='w', fill='y')
        self.current_frame.pack(anchor='nw', side='top')

    def change_frame(self, new_frame):
        self.current_frame.destroy()

        self.current_frame = new_frame(self)
        # self.current_frame.pack(side='top', anchor='w', fill='y')
        self.current_frame.pack(anchor='nw', side='top')


class MainFrame(tk.Frame):
    def __init__(self, root):
        self.root = root
        root.geometry("1800x800")
        super().__init__(root, bg='#706f6c')
        self.root.title("Prototype")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        menu_frame = tk.Frame(root)
        menu_frame.configure(width=100, height=5)
        menu_frame.pack(side='top', anchor='nw', padx=5, pady=5)

        self.membership_menu = tk.Menubutton(
            menu_frame,
            height=2,
            width=12,
            text='Memberships',
            underline=0,
            direction='below')
        self.membership_menu.grid(row=0, column=0)

        self.competitions_menu = tk.Menubutton(
            menu_frame,
            height=2,
            width=12,
            text='Competitions',
            underline=0,
            direction='below')
        self.competitions_menu.grid(row=0, column=1)

        self.graphsreports_menu = tk.Menubutton(
            menu_frame,
            height=2,
            width=16,
            text='Graphs and Reports',
            underline=0,
            direction='below')
        self.graphsreports_menu.grid(row=0, column=2)

        self.settings_menu = tk.Menubutton(
            menu_frame,
            height=2,
            width=10,
            text='Settings',
            underline=0,
            direction='below')
        self.settings_menu.grid(row=0, column=3)

        self.signout_button = tk.Button(
            menu_frame,
            height=2,
            width=6,
            text='Sign-Out',
            underline=0)
        self.signout_button.grid(row=0, column=4)


app = Application()
app.mainloop()
