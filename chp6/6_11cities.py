# Copyright (c) Vera Galstyan Jan 2018
cities = {
	'paris':{ 'country': 'france', 'population': 8, 'famous_place':'eiffel tower' },
	'yerevan':{'country': 'armenia','population': 1 , 'famous_place':'cascade'},
	'new york': {'country':'usa', 'population': 9, 'famous_place':'times sqaure'}
}

for city, info in cities.items():
	print(city)

	city_country = info['country']
	city_population = info['population']
	city_places = info['famous_place']

	print("\ncountry: " + city_country)
	print("population: "+ str(city_population))
	print("famous places: " + city_places)