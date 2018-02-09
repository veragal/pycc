# Copyright (c) Vera Galstyan Feb 2018
message = input("Tell me your name: ")
active = True
while active:
	phrase = input(message)

	if message == 'quit':
		active = False
	else:
		print(phrase)

prompt = "please enter your favorite city name: "
prompt += "\Enter 'quit' when you are done"

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print(" I would love to go to "+ city)
