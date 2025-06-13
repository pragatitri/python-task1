import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# 1. CONFIGURATION
API_KEY = '78c27fe22ce0e75827452a6003550d45'  # Replace with your real API key
CITY = 'Delhi'  # City for which to fetch the weather
UNITS = 'metric'  # Use 'metric' for Celsius
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}'

# 2. FETCH DATA
response = requests.get(URL)  
data = response.json() 

# 3. PROCESS DATA
temperatures = []
humidities = []
timestamps = []

# Loop through the next 12 forecast entries (3-hour intervals)
for forecast in data['list'][:12]:
    timestamps.append(datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S'))
    temperatures.append(forecast['main']['temp'])  
    humidities.append(forecast['main']['humidity'])  

# 4. PLOT TEMPERATURE TREND
plt.figure(figsize=(12, 6))  
sns.lineplot(x=timestamps, y=temperatures, marker='o', color='tomato', label="Temperature (°C)")
plt.title(f"12-Point Temperature Forecast for {CITY}")  
plt.xlabel("Time")  
plt.ylabel("Temperature (°C)")  
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.legend()  
plt.grid(True) 
plt.show()  

# 5. PLOT HUMIDITY TREND
plt.figure(figsize=(12, 6))  
sns.barplot(x=timestamps, y=humidities, palette="coolwarm")  
plt.title(f"12-Point Humidity Forecast for {CITY}")  
plt.xlabel("Time")  
plt.ylabel("Humidity (%)")  
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()  

# 6. PRINT WEATHER CONDITIONS
print("\nWeather Condition Forecast:")
for time in timestamps:
    print(f"{time.strftime('%Y-%m-%d %H:%M')} - Forecast available")