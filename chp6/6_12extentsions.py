# Copyright (c) Vera Galstyan Jan 2018
favorite_languages ={
'jen':['python','c','java'],
'sarah':['c'],
'david':['ruby','go']
	
}

for name,languages in favorite_languages.items():
	if len(languages) == 1:
		print(name + "'s favorite language is: "),
	else:
		print(name + "'s favorite languages are :")
	for language in languages:
		print("\t" + language.title())