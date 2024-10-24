import time
sum = 0
begin = time.perf_counter()

for i in range(1000000):
    sum = sum + i

end = time.perf_counter()

elapsed_time = end - begin

print(elapsed_time)
#6.2.2
