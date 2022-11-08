# # 1 задание
# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
 
 
# print(fibonacci(4))

# # 2 задание
# # Names = []
# # namesDictionary = {}

# # namesCount = int(input("Введите количетсво имен: "))
# # for i in range(namesCount):
# #     Names.append(input("Введите имя: "))

# # def toDictionary(names):
# #     for i in range(namesCount):
# #         namesDictionary.update({names[i]: None})
# #     return namesDictionary

# # print(toDictionary(Names))
# # a = toDictionary(Names)
# # print(a)

# # # 4 задание
# def shades_of_grey(n):
#     shades = []
#     firstHex ="0123456789abcdef"
#     secondHex = "0123456789abcdef"
#     secondCounter = 0 
#     firstCounter = 0
#     for i in range(n):
#         if i == 0:
#             secondCounter = 1
#         if secondCounter >= 16:
#             firstCounter += 1
#             secondCounter = 0
#         if firstCounter >= 16:
#             firstCounter = 0
#         gray = f"#{firstHex[firstCounter]}{secondHex[secondCounter]}{firstHex[firstCounter]}{secondHex[secondCounter]}{firstHex[firstCounter]}{secondHex[secondCounter]}"
#         shades.append(gray)
#         secondCounter += 1
    
#     return shades
# print(shades_of_grey(55))

# # 5 задание

import numpy as np 

def matrix(number):
    array = np.arange(number).reshape(int(number/3), 3)
    return(array)
        
print(matrix(12))
