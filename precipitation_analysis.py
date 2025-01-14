import json

with open('precipitation.json') as file:
    precipitation_data = json.load(file)

precipitation_seattle = []
total_monthly_precipitation = {}
total_prec = 0

for measurement in precipitation_data:
    if measurement["station"] == "GHCND:US1WAKG0038":
        precipitation_seattle.append(measurement)

for measurement in precipitation_seattle: 
    months = int(measurement['date'].split('-')[1])
    precipitation_value = measurement['value']
    if months in total_monthly_precipitation:
        total_monthly_precipitation[months] += precipitation_value
    else:
        total_monthly_precipitation[months] = precipitation_value  

with open('total_monthly_precipitation.json', 'w', encoding='utf-8') as file:        
    json.dump(total_monthly_precipitation, file)

 