a_set = {1, 2, 3}
print(a_set)

a_set.add(4)
print(a_set)

if 3 in a_set:
    print("3 is in the set")
else:
    a_set.add(3)

    a_set.add(5)

if 5 in a_set:
    print("5 is in the set")
else:
    a_set.add(30)

print(a_set)