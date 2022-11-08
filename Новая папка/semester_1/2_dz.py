s = "phew"
home = s[::-1]
print(home)

# 2 задание

# 1
a = ["car", "home", "boy"]
b = ["sleep", "girl", "pen"]
a.append(b)
print(a)

#2
fruits = ['виноград', 'яблоко', 'апельсин']

x = fruits.count("апельсин")

print(x)

#3
fruits = ['grape', 'apple', 'pear', 'orange']

x = fruits.copy()

print(x)

#4
s = ['car', 'boy', 'home']

s.insert(2, "orange")
print(s)

#5
fruits = ['grape', 'apple', 'pear']

fruits.sort(reverse=True)
print(fruits)

#6
phonemodels = ['apple', 'samsung', 'LG']

cars = ['chevrolet', 'BMW', 'gelik']

phonemodels.extend(cars)

print(phonemodels)

#7
cars = ['chevrolet', 'BMW', 'gelik']

cars.pop(0)

print(cars)

#8
numbers = [4, 45, 68, 24, 16, 32]

x = numbers.index(45)
print(x)