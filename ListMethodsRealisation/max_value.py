def max_value(data):
    min_val = data[0]
    i = 0
    while i < len(data):
        if data[i] > min_val:
            min_val = data[i]
        i += 1
    return min_val

# Example
list1 = [100, 45, 125, 12, 124, 14, 45]
print(max_value(list1))
