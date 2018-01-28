#  Copyright (c) Vera Galstyan Jan 2018
users = ['anna', 'david','katya','admin','kolya']
for user in users:
	if user=='admin':
		print("hello admin jan, would you like to see a status report?")
	else:
		print("Hello " + user + " , thank you for logging in again")
print('Done')