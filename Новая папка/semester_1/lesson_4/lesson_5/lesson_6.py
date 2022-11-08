# матрица
[2,3,4,5,6] # error
matrix = [[2,3,4], [5,6,7]] # матрица 3 столбца и 2 строки 
print (matrix[1][1]) # 01 \ 11 \
# random = list(1) # error
# random = list(true) # error
rendom = list("Random  !%#&%$!=") # error
splitted_string = "Split me ! random".split("me ! ")
print(rendom, splitted_string, ''.join(rendom),sep="\n")

# tuple
numbers = (2,3,4,5,6)
print(numbers, numbers[3])

numbers = ((4,5), 4.5, "fafa", [5,6,7])
print (numbers, numbers[3])

# numbers[1] = "changed"

numbers = (2, 4, 5, [4, 5])
numbers[3][0] = 24
print (numbers[3], numbers[3][0])
