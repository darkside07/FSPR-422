# 1 union
A = {7, 3, 5}
B = {1, 4, 3}
print('A U B = ', A.union(B))

# 2 update

A = {1, 7, 3, 4}
B = {7, 3, 4, 5}
A.intersection_update(B)
print('A =', A)


A = {2, 3, 5}
B = {5, 7, 9, 11, 13}
C = {5, 15, 17, 19, 21}
A.intersection_update(B, C)
print('A =', A)
print('B =', B)
print('C =', C)

# 3 add

numbers = {5, 7, 8, 9}
numbers.add(11)
print(numbers)


vowels = {'h', 'o', 'm', 'e'}
vowels.add('s')
print('Vowels are:', vowels)
vowels.add('h')
print('Vowels are:', vowels)



vowels = {'a', 'b', 'c'}
tup = ('i', 'o')
vowels.add(tup)
print('Vowels are:', vowels)
vowels.add(tup)
print('Vowels are:', vowels)

# 4 pop

A = {'xumo', 'phone', 'home', 'car'}
removed_item = A.pop()
print(removed_item)


A = {'car', 'Tee', '1000', 'Hundred'}
print('Pop() removes:', A.pop())
print('Updated set A:', A)

# 5 remove

names = {'abbos', 'Javaxir', 'Xumo'}
names.remove('Xumo')
print(names)

# 6 copy

numbers = {"22", "33", "44"}
new_numbers = numbers.copy()

print('Original Names: ', numbers)
print('Copied Names: ', new_numbers)

# 7 clear

names = {5, 7, 8, 9}
names.clear()
print(names)

# 8

A = {2, 5, 7, 9, 11}
B = {2, 13, 5, 11, 9}
print(A.difference(B)) 

A = {'k', 'o', 't', 'd'}
B = {'a', 'b', 'c'}
print(A - B)
print(B - A)


# 2 задание


