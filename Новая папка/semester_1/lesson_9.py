# is и ==
from copy import copy
from re import A


a = (2, 3, 4)
b = (2, 3, 4)
print (a is b, a ==b)

b = [2, 3, 4]
b.append(23)
a = [2, 3, 4]
print (a is b, a == b)

# a это б. Б ЭТО А
a = [2, 3, 4]
b = a 
b.append(43)
print("a =", a, "b =", b)

# c копированием
a = [2, 3, 4, [2, 3]]
b = a.copy()
b[2] = 400
b[3][1] = 12
print ("a =", a, "b", b)

# модуль для глубоко копирования
import copy
a = [2, 3, 4, [2, 3]]
b = copy.deepcopy(a)
b[2] = 400
b[3][1] = 12
print ("a =", a, "b", b)




print("list")
numbers = [1, 2, 3, 4, 5, 6 , 7]
for num in numbers:
    print(num + 2)


print("tuple")
numbers = [1, 2, 3, 4, 5, 6 , 7]
for num in numbers:
    print(num + 2)


print("set")
numbers = [1, 2, 3, 4, 5, 6 , 7]
for num in numbers:
    print(num + 2)


print("dict")
user = {
    "name": "Xumo",
    "age": 18,
    "skill": "swim",
}
for key in user:
    print(key)

print("dict vals")
for val in user.values():
    print(val)

print("\ndict items")
for key, val in user.items():
    print("key =", key, "val =", val)

print (user.items())
a, b = [2, 4]
print(a, b)

