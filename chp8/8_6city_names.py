# Copyright (c) Vera Galstyan Feb 2018

def city_country(city_name,city_country):
	message = city_name + ", " + city_country
	return(message)
first_city = city_country('paris', 'france')
second_city = city_country('london','uk')
third_city = city_country('las vegas','usa')

print(first_city)
print(second_city)
print(third_city)