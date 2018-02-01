# Copyright (c) Vera Galstyan Feb 2018
def make_album(artist_name,albom_title,number_of_track = ''):
	artist = {'name':artist_name,'albom title': albom_title}
	if number_of_track:
		artist['number_of_track']=number_of_track
	return artist

musician_1 = make_album('system of a down','hysteria')
musician_2 = make_album('sia','hello')
musician_3 = make_album('adele','bye')
musician_4 = make_album('mia','barev',17)
print(musician_3)
print(musician_2)
print(musician_1)
print(musician_4)