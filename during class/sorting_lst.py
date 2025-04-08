a_list = [1, 4, 3, 5, 2]
b_list = sorted(a_list)
a_list.sort()

c_list = [1, 4, 3, 5, 2]
c_list.sort(reverse=True)
d_list = sorted(c_list, reverse=True)

print(b_list)  # [1, 2, 3, 4, 5]
print(c_list)  # [1, 2, 3, 4, 5]
print(d_list)  # [5, 4, 3, 2, 1]


print([n for n in range(1, 10)])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([n for n in range(1, 10, 2)])  # [1, 3, 5, 7, 9]
print([char for char in 'hello'])  # ['h', 'e', 'l', 'l', 'o']
print(['x' for _ in range(10)])  # ['x', 'x', 'x', 'x', 'x']
print([0 for _ in "Toothpaste Pop"])  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lst = [num for num in range(2, 11, 2)]
print(lst)  # [2, 4, 6, 8, 10]

print([5 for _ in range(100)])

data = [1, 2, 3, 4, 5]
print([x for x in data if x % 2 == 0])  # [2, 4]