#  Copyright (c) Vera Galstyan Jan 25,2018
guests = ['ofa', 'karen', 'mama', 'papa','ani']
message = "Please,be my guest "
print("Now I can invite only 2 people")
sorry_message = "Sorry, I cannot invite you"

print(sorry_message + guests.pop(0))
print(sorry_message + guests.pop(1))
print(sorry_message + guests.pop())
print(guests)

print("You are still invited " + guests[0])
print("You are still invited " + guests[1])

del guests[-1]
del guests[0]

print guests