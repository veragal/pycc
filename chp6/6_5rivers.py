#Copyright (c) Vera Galstyan Jan 25,2018

rivers = {
	'seine':'paris',
	'rone':'lyon',
	'hudson':'new york',
	'moscow': 'moscow',
	}

for key,value in rivers.items():
	print("The "+ key + " runs through "  + value)
	
for key in sorted(rivers.keys()):
	print(key)

for value in set(rivers.values()):
	print(value)