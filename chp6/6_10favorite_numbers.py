# Copyright (c) Vera Galstyan Jan 2018

favorite_numbers = {
	'eva': [7,12,13],
	'ofa': [1,28,12],
	'karen':[21,32,8],
	'lia':[2,11,9]
}

for name,numbers in favorite_numbers.items():
	print(name + "'s favoprite numbers are :")
	for number in numbers:
		print(number)