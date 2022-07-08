import tkinter as tk

import WeatherForecast

class MeteoModule(tk.Frame):
    
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.font = ("Arial", 20)

        self.create_test_label()
    
    def create_test_label(self):
        self.test_label = tk.Label(self, text="Meteo", font=self.font, background= "black", foreground="white")
        self.test_label.grid(row=0, column=0)
    
    def create_location_label(self):
        self.test_label = tk.Label(self, text="", font=self.font, background= "black", foreground="white")
        self.test_label.grid(row=1, column=0)

    def create_temp_label(self):
        self.test_label = tk.Label(self, text="", font=self.font, background= "black", foreground="white")
        self.test_label.grid(row=2, column=0)
    
    def create_hum_label(self):
        self.test_label = tk.Label(self, text="", font=self.font, background= "black", foreground="white")
        self.test_label.grid(row=3, column=0)

    def create_press_label(self):
        self.test_label = tk.Label(self, text="", font=self.font, background= "black", foreground="white")
        self.test_label.grid(row=3, column=0)    

    def create_refresh_label(self):
            self.test_label = tk.Label(self, text="", font=self.font, background= "black", foreground="white")
            self.test_label.grid(row=4, column=0) 
            
    def refresh_temperature():
        
        weather = WeatherForecast()
        temperatue_data = weather.get_formated_weather_data()
        location_label.configure(text=temperatue_data['location'])
        temp_label.configure(text=f"{temperatue_data['current_temperature']} °C")
        hum_label.configure(text=temperatue_data['humidity'])
        press_label.configure(text=temperatue_data['humidity'])
        last_refresh_label.configure(text=temperatue_data['last_refrersh'])
        location_label.after(1000 * 10, refresh_temperature)
    
    refresh_temperature()


