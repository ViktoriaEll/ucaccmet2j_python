# WEATHER ASSIGNMENT

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
total_precipitation = 0

# Calculating total monthly precipitation for each station
for station in station_data:
    station_data[station]['total_monthly_precipitation'] = []
    for month in range(1,13):
        monthly_precipitation = 0
        for precipitation in precipitation_data:
            if station_data[station]['Station'] == precipitation['station']:
                if precipitation['date'][1] == month:
                    monthly_precipitation += precipitation['value']
        station_data[station]['total_monthly_precipitation'].append(monthly_precipitation)
        
    # Calculating yearly precipitation
    total_yearly_precipitation = sum(station_data[station]['total_monthly_precipitation'])
    station_data[station]['total_yearly_precipitation'] = total_yearly_precipitation
    
    # Calculating relative monthly
    station_data[station]['relative_monthly_precipitation'] = []    
    for value in station_data[station]['total_monthly_precipitation']:
        station_data[station]['relative_monthly_precipitation'].append(value/(station_data[station]['total_yearly_precipitation']))

    # total precipitation
    total_precipitation += station_data[station]['total_yearly_precipitation']

# relative yearly precipitation for each station
for station in station_data:
    station_data[station]['relative_yearly_precipitation'] = ((station_data[station]['total_yearly_precipitation'])/total_precipitation)

print(station_data)

with open('results.json', 'w', encoding='utf-8') as file:
   json.dump(station_data, file, indent=4)