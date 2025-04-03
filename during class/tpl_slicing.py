a_string = "Buttercup FTW"
doggo = list(a_string)
slice = doggo[2:6] # ['t', 't', 'e', 'r']
print(slice)

slice = doggo[:6] # ['B', 'u', 't', 't', 'e', 'r']
print(slice)

slice = doggo[4:] # ['e', 'r', 'c', 'u', 'p', ' ', 'F', 'T', 'W']
print(slice)

slice = doggo[:] # ['B', 'u', 't', 't', 'e', 'r', 'c', 'u', 'p', ' ', 'F', 'T', 'W']
print(slice)

slice = doggo[2:10:2] # ['t', 'e', 'c', 'p']
print(slice)

slice = doggo[::-1] # ['W', 'T', ' ', 'p', 'u', 'c', 'r', 'e', 't', 't', 'u', 'B']
print(slice)

slice = doggo[:-4:-1] # ['W', 'T', 'F']
print(slice)