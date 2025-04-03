a_list = ["a"]
print(a_list)
b_list = ["b"]
print(b_list)
b_list = a_list + b_list
print(b_list)

b_list = b_list + [1, 2, 3]
one = ["Butt"]
one += ["ercup"]
print(one)

print(one.pop(0), end="")
print(one.pop())

lst = []
lst.insert(0, 123)
print(lst)