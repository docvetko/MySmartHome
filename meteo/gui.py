import tkinter as tk
from meteo.get_meteo import Prognoza



class MeteoModule(tk.Frame):


    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.font = ("Arial", 20)

        self.create_test_label()
        self.create_location_label()
        self.create_temp_label()
        self.create_hum_label()
        self.create_press_label()
        self.create_refresh_label()
    
   
    def create_test_label(self):
        
        self.test_label = tk.Label(self, text="Meteo", font=self.font, background= "black", foreground="white")
        self.test_label.grid(row=0, column=0)
    
    def create_location_label(self):
        weather = Prognoza()
        temperatue_data = weather.get_formated_weather_data()
        self.location_label = tk.Label(self, text="", font=self.font, background= "black", foreground="white")
        self.location_label.grid(row=1, column=0)
        self.location_label.configure(text=temperatue_data['location'])
        
    def create_temp_label(self):
        weather = Prognoza()
        temperatue_data = weather.get_formated_weather_data()
        self.temp_label = tk.Label(self, text="", font=self.font, background= "black", foreground="white")
        self.temp_label.grid(row=2, column=0)
        self.temp_label.configure(text=f"{temperatue_data['current_temperature']} °C")
    
    def create_hum_label(self):
        weather = Prognoza()
        temperatue_data = weather.get_formated_weather_data()
        self.hum_label = tk.Label(self, text="", font=self.font, background= "black", foreground="white")
        self.hum_label.grid(row=3, column=0)
        self.hum_label.configure(text=f" Vlažnost: {temperatue_data['humidity']}")

    def create_press_label(self):
        weather = Prognoza()
        temperatue_data = weather.get_formated_weather_data()
        self.press_label = tk.Label(self, text="", font=self.font, background= "black", foreground="white")
        self.press_label.grid(row=4, column=0)
        self.press_label.configure(text=f" Tlak: {temperatue_data['pressure']}")   

    def create_refresh_label(self):
        weather = Prognoza()
        temperatue_data = weather.get_formated_weather_data()
        self.refresh_label = tk.Label(self, text="", font=self.font, background= "black", foreground="white")
        self.refresh_label.grid(row=5, column=0)
        self.refresh_label.configure(text=temperatue_data['last_refrersh'])
            

