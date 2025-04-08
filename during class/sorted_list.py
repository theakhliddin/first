a_set = set([123, 456, 123, 789])
for number in a_set:
    print(number, end=" ")

a_list = sorted(list(a_set))
print(a_list)