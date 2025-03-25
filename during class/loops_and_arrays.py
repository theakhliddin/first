import arrays
from arrays import array_a
lenght = len(array_a)

counter = 0
while counter < lenght:
    array_a[counter] = counter * 2
    counter += 1
for index in range(lenght):
    print(array_a[index])