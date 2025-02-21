import requests
from dotenv import load_dotenv
import os
from pprint import pprint   

load_dotenv()

def get_current_weather():

    print("\n*** Get Current Weather")

    city = input("\nEnter city name: ")

    request_url =f'https://api.openweathermap.org/data/2.5/weather?&q={city}&appid={os.getenv("API_KEY")}&units=metric'

    # print(request_url)

    weather_data =  requests.get(request_url).json()
    # pprint(weather_data)

    print(f"\n Current weather for {weather_data['name']}: ")
    print(f"\n The Temprature is {weather_data["main"]["temp"]:.2f}")

get_current_weather()