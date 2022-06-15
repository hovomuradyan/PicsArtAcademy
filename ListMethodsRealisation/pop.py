def pop(data, i=-1):
    if i != -1:
        data1 = data[:i] + data[i + 1:-1]
        data1.append(data[-1])
    else:
        data1 = data[:i]
    # print(data1)   // for testing
    removed_index = data[i]
    data = data1
    return removed_index


list1 = [1, 45, 125, 12, 124, 14]
print(pop(list1, 3))
