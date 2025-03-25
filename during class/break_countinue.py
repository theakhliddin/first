count = 0
while True:
    count = count + 1
    if count % 5 == 0:
        continue
    elif count >= 1000:
        break
    print(count)

print("The loop has ended.")