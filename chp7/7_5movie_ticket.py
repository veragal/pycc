# Copyright (c) Vera Galstyan Feb 2018

prompt = input("Please tell me your age: ")
age = int(prompt)

active = True
while active:
	message = input(prompt)
	if message =='quit':
		active = False
	else:
		print(message)
		if age <= 3:
			print("You can enter for free,because you are " + prompt)
		elif age > 3 and age < 12:
			print("your ticket is 10$, because you are "+ prompt)
		else:
			print("your ticket is 15$, because you are " + prompt)