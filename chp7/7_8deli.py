# Copyright (c) Vera Galstyan Jan 2018

sandwich_orders= ['french','italian','armenian']
finished_sandwiches= []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print("I made your " + sandwich + " sandwich")
	finished_sandwiches.append(sandwich)

