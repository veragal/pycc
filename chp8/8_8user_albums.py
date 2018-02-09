# Copyright (c) Vera Galstyan Feb 2018

def make_album(artist_name,album_title):
	artist = {'name':artist_name, 'title':album_title}
	return artist

while True:
	print("\Please enter your favorite artist's name")
	print("(enter 'q' to quit")

	a_name = input("Artist name: ")
	if a_name == 'q':
		break

	a_title = input("Album title: ")
	if a_title == 'q':
		break

album = make_album(a_name,a_title)
print("Hello" + artist )