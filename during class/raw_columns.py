def create_2d_list(rows, cols, value = 0):
    return [[value for _ in range(cols)] for _ in range(rows)]

rows = 3
cols = 4
value = 1

print("2D List:")
for rows in create_2d_list(rows, cols, value):
    print(rows)