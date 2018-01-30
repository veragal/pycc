#  Copyright (c) Vera Galstyan Jan 25,2018
sandwich_orders = ['armenian','italian','french','american','italien','russian','armenian']
print("We are sorry, we are run out of armenian sandwiches")

while 'armenian' in sandwich_orders:
	sandwich_orders.remove('armenian')

print(sandwich_orders)