import json

with open('precipitation.json') as file:
    precipitation_data = json.load(file)

precipitation_seattle = {}
total_monthly_precipitation = []
list_index = 0

for measurement in precipitation_data:
    if measurement["station"] == "GHCND:US1WAKG0038":
        precipitation_seattle.update(precipitation_data(list_index))
        # precipitation_seattle.update(measurement) 
        list_index = list_index + 1

with open('precipitation_seattle.json', 'w', encoding='utf-8') as file:        
    json.dump(precipitation_seattle, file)

# since the json file is a list of directories (might be worth asking about this), I was trying to get it to add the item of the list to a new list?


