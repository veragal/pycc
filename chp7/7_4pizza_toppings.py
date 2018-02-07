# Copyright (c) Vera Galstyan Feb 2018

prompt = " Tell me your pizza topping: "
prompt += "Enter 'quit' to end the program"

message = ""
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print("We will add " + message + " to your pizza")