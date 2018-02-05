# Copyright (c) Vera Galstyan Feb 2018
restaurant = input("How many people are in your group: ")
if int(restaurant)>=8:
	print("You have to wait for a table, because you are " + restaurant)
else:
	print("Your table is ready, because you are " + restaurant)