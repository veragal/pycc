
# Copyright (c) Vera Galstyan Jan 2018

favorite_places ={
	'vera': ['lyon','paris','london'],
	'ofa':['berlin','madrid','milan'],
	'karen':['dubai','barcelona']
}

for name,places in favorite_places.items():
	print("\n" + name + "'s favorite places are:")
	for place in places:
		print(place)