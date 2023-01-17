# WEATHER ASSIGNMENT
# Q 1.1

import json
with open('precipitation.json', encoding='utf-8') as file:
  precipitation_data = json.load(file)



for precipitation in precipitation_data:
    precipitation['date'] = (precipitation['date'].split('-'))
    for i in range(3):
        precipitation['date'][i] = int(precipitation['date'][i])
#print(precipitation_data)

total_monthly_precipitation = []

for month in range(1,13):
    monthly_precipitation = 0
    for precipitation in precipitation_data:
        if precipitation['station'] == 'GHCND:US1WAKG0038':
                if precipitation['date'][1] == month:
                    monthly_precipitation += precipitation['value']
    total_monthly_precipitation.append(monthly_precipitation)

print(total_monthly_precipitation)

#with open('results.json', 'w', encoding='utf-8') as file:
 #   json.dump(total_monthly_precipitation, file, indent=4)

