import os
from dotenv import find_dotenv, load_dotenv
import datetime as dt
import requests

#find the .env file
dotenv_path  = find_dotenv()

load_dotenv(dotenv_path)
api_key = os.getenv("API_KEY")
url = f"https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": 52.5200,  # Latitude for Berlin
    "lon": 13.4050,  # Longitude for Berlin
    "appid": api_key,
    "units": "metric"  # For Celsius
}

# Make the API request
response = requests.get(url, params=params)
data = response.json()
timestamp = data['dt']
timezone_offset = data['timezone']

local_time = dt.datetime.utcfromtimestamp(timestamp + timezone_offset)
print(local_time)

temperature = data['main']['temp']
print(temperature)

cloud_cover = data['weather'][0]['description']
print (cloud_cover)



