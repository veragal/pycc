
#  Copyright (c) Vera Galstyan Jan 25,2018
people = ['jen', 'vera','phil','ofa','sarah']

languages = {
	'jen': 'c',
	'sarah':'python',
	'edward':'ruby',
	'phil':'python'
}
 

for name in people:
	if name in languages.keys():
		print(name + " , thank you for your particiaption")
	else:
		print(name + " , you should take a poll")
