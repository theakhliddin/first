"""
#original
a = 5
b = 11

print("Original values: a = ", a, " b = ", b)

#swap
temp = a
a = b
b = temp

print("Swapped values: a = ", a, " b = ", b)
"""

#another version

a = 5
b = 11

print("original values: a = ", a, " b = ", b)

a, b = b, a
print("swapped values: a = ", a, " b = ", b)