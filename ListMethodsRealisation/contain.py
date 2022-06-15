""" Function for checking value exsisting in data"""
def contain(data, val):
    for i in data:
        if i == val:
            return True
    return False


list1 = [1, 2, 5]
# True example
print(contain(list1, 1))
# False example
print(contain(list1, 12))
