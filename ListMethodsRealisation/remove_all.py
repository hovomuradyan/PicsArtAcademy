def remove_all(data, value):
    i = 0
    data1 = []
    while i < len(data):
        if data[i] != value:
            data1.append(data[i])
        i += 1
    return data1


list1 = [1, 45, 125, 12, 124, 14, 45]
print(remove_all(list1, 135))
