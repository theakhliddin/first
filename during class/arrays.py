import arrays

array_a = arrays.Array(5)
print(array_a)
print(array_a.[3])

length = len(array_a)
for index in range(length):
    array_a[index] = index * 5

array_b = arrays.Array(5, "abc")