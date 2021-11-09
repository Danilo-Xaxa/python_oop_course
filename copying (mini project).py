from copy import copy
 
 
a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c
 
def remove_elem(data, target):
    for item in (d := copy(data)):
        if item == target:
            d.remove(target)
    return d
 
def get_product(data):
    total = 1
    for _ in range(len((d := copy(data)))):
        total *= d.pop()
    return total
 
remove_elem(c, 3)
print(get_product(b))
print(a)
