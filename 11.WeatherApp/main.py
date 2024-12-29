import tkinter as tk
import requests
from tkinter import messagebox

API_KEY = "API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


class WeatherApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x300")

        self.label = tk.Label(self.root, text="Weather App", font=("Arial", 26))
        self.label.pack(pady=10)

        self.city_entry = tk.Entry(self.root, font=("Arial", 14))
        self.city_entry.pack(pady=10)

        self.get_weather_button = tk.Button(self.root, text="Get Weather", font=("Arial", 16), command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        self.weather_info_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.weather_info_label.pack(pady=20)

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city name")
            return
        url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
        response = requests.get(url)
        data = response.json()

        print(response.ok)
        if response.ok:
            main_data = data["main"]
            weather_data = data["weather"][0]
            temperature = main_data["temp"]
            weather_description = weather_data["description"]
            humidity = main_data["humidity"]
            pressure = main_data["pressure"]

            self.weather_info_label.configure(
                text=f"Temperature: {temperature}°C\n"
                     f"Weather: {weather_description.capitalize()}\n"
                     f"Humidity: {humidity}%\n"
                     f"Pressure: {pressure} hPa"
            )
        else:
            messagebox.showerror("Error", "City not found, please try again!")



if __name__ == '__main__':
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
