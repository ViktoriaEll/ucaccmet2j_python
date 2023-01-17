# WEATHER ASSIGNMENT
# Q 1.1
import json
with open('precipitation.json', encoding='utf-8') as file:
  precipitation_data = json.load(file)

from csv import DictReader
with open('stations.csv') as file:
  reader = DictReader(file)
  stations = list(reader)

station_data = {}

# Creating station dictionary
for station in stations:
   station_data[station['Location']] = station

# Making the data a list of integers [year, month, day]
for precipitation in precipitation_data:
    precipitation['date'] = (precipitation['date'].split('-'))
    for i in range(3):
        precipitation['date'][i] = int(precipitation['date'][i])

total_monthly_precipitation = []

# Calculating total monthly precipitation for Seattle
for month in range(1,13):
    monthly_precipitation = 0
    for precipitation in precipitation_data:
        if precipitation['station'] == 'GHCND:US1WAKG0038':
                if precipitation['date'][1] == month:
                    monthly_precipitation += precipitation['value']
    total_monthly_precipitation.append(monthly_precipitation)

print(total_monthly_precipitation)
station_data['Seattle']['total_monthly_precipitation'] = total_monthly_precipitation

print(station_data)

with open('results.json', 'w', encoding='utf-8') as file:
   json.dump(station_data, file, indent=4)

# results.json also includes some information for the other stations which in order to make the graph using plot_results.py has to be removed