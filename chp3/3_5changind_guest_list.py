#  Copyright (c) Vera Galstyan Jan 25,2018
guests = ['ofa', 'karen', 'mama', 'papa']
message = "Please,be my guest "
print(message + guests[0].title())
print(message + guests[1])
print(message + guests[2])
print(message + guests[3])
print("Karen cannot come today")

del guests[1]
guests.append('samvel')
print(message + guests[0].title())
print(message + guests[1])
print(message + guests[2])
print(message + guests[3])