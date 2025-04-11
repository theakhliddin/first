def max_value_pair(d):
    if not d:
        return None
    
    max_key = max(d, key=d.get)
    return (max_key, d[max_key])

sample_dict = {'a': 10, 'b':25, 'c':7, 'd':250}

result = max_value_pair(sample_dict)
print("Key wiht max value:", result)


# ASCII value of the key
# 48 -0
# 49 -1
# 50 -2

# 65 -A
# 66 -B
# 67 -C

# 97 -a
# 98 -b
# 99 -c
# 100 -d