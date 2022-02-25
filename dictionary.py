#           item
# -----------------------
#    key          value
# dictionary example
cars = {
    "brand":"lada",
    "model":"granta",
    "power": 87,
    "body" :"sedan",
    "year" : "2013"

     }
print(cars)
print(cars.get('power')) # output 87
cars["fuel"] = "petrol" # add item to dict 
#{'brand': 'lada', 'model': 'granta', 'power': 87, 'body': 'sedan', 'year': '2013', 'fuel': 'petrol'}
del cars ['model'] # delete item from dict 
print(cars) #{'brand': 'lada', 'power': 87, 'body': 'sedan', 'year': '2013', 'fuel': 'petrol'}
cars_v1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(cars_v1.get('brand')) # output Ford
# change value in dict
cars_v1["year"] = "1970" # output {'brand': 'Ford', 'model': 'Mustang', 'year': '1970'}
print(cars_v1)
# output only keys or values
print(cars.keys()) # dict_keys(['brand', 'power', 'body', 'year', 'fuel'])
print(cars.values()) # dict_values(['lada', 87, 'sedan', '2013', 'petrol'])