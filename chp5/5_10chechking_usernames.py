#  Copyright (c) Vera Galstyan Jan 2018
current_users = ['anna','ani','lia','ofa','vera','karen']
new_users = ['Karen','ani','vova','papa','vera']

new_current_users = [name.lower() for name in current_users]
print(new_new_users)

for user in new_users:
	small_user = user.lower()
	if small_user in new_current_users:
		print("You have to choose a new username " + small_user)
	else:
		print("your username is available " + small_user)