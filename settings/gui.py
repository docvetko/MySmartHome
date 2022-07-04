
import tkinter as tk
from tkinter import IntVar
from tkinter import ttk
from tkinter.colorchooser import askcolor


class SettingsModule(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.font = ("Arial", 12)

        self.create_test_label()
        self.create_color_button()
        self.create_time_check()

    
    def create_test_label(self):
        self.test_label = tk.Label(self, text="Settings", font=self.font, background= "black", foreground="white")
        self.test_label.grid(row=0, column=0)
    
    def create_color_button(self):
        self.color_label = tk.Button(self, text="Select a Color", font=self.font, background= "black", foreground="white", command=self.change_color)
        self.color_label.grid(row=1, column=0)
    
    def create_time_check(self):
        CheckVar1 = IntVar()
        self.test_label = tk.Checkbutton(self, text="Show current time", font=self.font, background= "black", foreground="white",variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
        self.test_label.grid(row=2, column=0)

    def change_color(self):
        self.colors = askcolor(title="Background Color Chooser")
        self.configure(bg=self.colors[1])
