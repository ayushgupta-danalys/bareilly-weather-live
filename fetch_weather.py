import requests
import csv
from datetime import datetime
import os

url = "https://wttr.in/Bareilly?format=j1"
response = requests.get(url)
data = response.json()

current = data["current_condition"][0]

row = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "temp_C": current["temp_C"],
    "feelslike_C": current["FeelsLikeC"],
    "humidity": current["humidity"],
    "pressure": current["pressure"],
    "windspeedKmph": current["windspeedKmph"],
    "winddir16Point": current["winddir16Point"],
    "uvIndex": current["uvIndex"],
    "cloudcover": current["cloudcover"],
    "precipMM": current["precipMM"],
    "weatherDesc": current["weatherDesc"][0]["value"]
}

file_exists = os.path.isfile("bareilly_weather.csv")

with open("bareilly_weather.csv", "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=row.keys())
    if not file_exists:
        writer.writeheader()
    writer.writerow(row)

print("Data saved successfully:")
print(row)