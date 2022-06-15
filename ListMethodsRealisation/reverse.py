def reverse(data):
    i = len(data) - 1
    data1 = []
    while i >= 0:
        data1.append(data[i])
        i -= 1
    return data1


list1 = [1, 45, 125, 12, 124, 14, 45]
print(reverse(list1))
