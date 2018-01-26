#  Copyright (c) Vera Galstyan Jan 25,2018
my_pizzas = ['napoli','margarita','calzone']
friends_pizzas = my_pizzas[:]
my_pizzas.append('arugula')
friends_pizzas.append('peperoni')
print("My favorite pizzas are")
for pizza in my_pizzas:
	print(pizza)
print("My friends favorite pizzas are")
for food in friends_pizzas:
	print(food)

