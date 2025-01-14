import json
import csv

with open('precipitation.json') as file:
    precipitation_data = json.load(file)


# Question 1   
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

# Question 2 (started without realising that it was only meant to be only Seattle, so this is part of question 3 also)
yearly_prec_cincinnati = 0
yearly_prec_maui = 0
yearly_prec_san_diego = 0
yearly_prec_seattle = 0

for measurement in precipitation_data:
    if measurement["station"] == "GHCND:USW00093814":
        yearly_prec_cincinnati += measurement['value']
    elif measurement['station'] == "GHCND:USC00513317":
        yearly_prec_maui += measurement['value']
    elif measurement['station'] == "GHCND:US1CASD0032":
        yearly_prec_san_diego += measurement['value']
    else:
        yearly_prec_seattle += measurement['value']

#   seattle Question 2
relative_monthly_prec = {}
key = 1
for measurement in total_monthly_precipitation:
    relative_monthly_prec[key] = total_monthly_precipitation[key]/yearly_prec_seattle
    key += 1

with open('seattle_relative_precipitation.json', 'w', encoding='utf-8') as file:        
    json.dump(relative_monthly_prec, file)