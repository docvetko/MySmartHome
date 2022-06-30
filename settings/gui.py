import tkinter as tk


class SettingsModule(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.font = ("Arial", 20)

        self.create_test_label()
    
    def create_test_label(self):
        self.test_label = tk.Label(self, text="Settings", font=self.font, background= "black", foreground="white")
        self.test_label.grid(row=0, column=0)