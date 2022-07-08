import datetime as dt
import tkinter as tk
from tkinter import ttk
from tkinter import font

from lights.gui import  LightsModule
from security.gui import SecurityModule
from temperature.gui import TemperatureModule
from tv.gui import TVModule
from meteo.gui import MeteoModule


def formatted_date():

    today = dt.datetime.now()

    return today.strftime('%A, %d %B %Y')
    
def formatted_time():

    now_time = dt.datetime.now()

    return now_time.strftime('%H : %M : %S')

class MySmartHome(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Algebra | MySmartHome")
        self.geometry("800x600")
        self.configure(background='black')

        self.apply_custom_style()
        self.create_tab_navigation()
        self.create_time_frame()
    
    def apply_custom_style(self):
        self.style = ttk.Style()
        self.style.theme_create(
            "MySmartHomeTheme", settings={
                "TNotebook": {
                    "configure": {
                        "tabmargins": [5, 5, 5, 5]
                    }
                },
                "TNotebook.Tab": {
                    "configure": {
                        "padding": [15, 15],
                        "background": "black",
                        "foreground": "white"
                        
                    },
                    "map": {
                        "background": [("selected", "#737373")],
                        "expand": [("selected", [1, 1, 1, 0])]
                    }
                }
            }
        )
        self.style.theme_use("MySmartHomeTheme")

    def create_tab_navigation(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=0 )

        self.tv_frame = TVModule(self, background='Black')
        self.tv_frame.grid(row=1, column=1)
        self.notebook.add(self.tv_frame, text="TV")

        self.lights_frame = LightsModule(self, background='Black')
        self.lights_frame.grid(row=1, column=1)
        self.notebook.add(self.lights_frame, text="Lights")

        self.security_frame = SecurityModule(self, background='Black')
        self.security_frame.grid(row=1, column=1)
        self.notebook.add(self.security_frame, text="Security")

        self.temperature_frame = TemperatureModule(self,  background='Black')
        self.temperature_frame.grid(row=1, column=1)
        self.notebook.add(self.temperature_frame, text="Temperature")

        self.meteo_frame = MeteoModule(self,  background='Black')
        self.meteo_frame.grid(row=1, column=1)
        self.notebook.add(self.meteo_frame, text="Meteo")

    def create_time_frame(self):
        #time_frame = tk.LabelFrame(self,text='', width=100, height=100, background='black', fg='#ffffff')
        #time_frame.grid(column=0, row=0, padx=0, pady=0)

        date_label = tk.Label(
            self, text=formatted_date(),
            font=('Arial', 12), background='black', fg='#ffffff'
            )
        date_label.grid(row=0, column=0, padx=5, pady=5)

        time_label = tk.Label(
            self, text=formatted_time(),
            font=('Arial', 12), background='black', fg='#ffffff'
            )
        time_label.grid(row=0, column=2,  padx=5, pady=5)

        def refresh_time():
            now_time = formatted_time()
            time_label.configure(text=now_time)
            time_label.after(1000, refresh_time)

        refresh_time() 

root = MySmartHome()

root.mainloop()
