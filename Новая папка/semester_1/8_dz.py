# from glob import iglob


# square_line = 4 
# star = "*" 
# star_width = star * square_line  

# for i in range(square_line):
#     # prinnt("I", i)
#     if i > 0 and i < (square_line - 1): # i < 0 and i < 5; i = 1 2 3 4
#         empty_space = " " * (square_line - 2) # 4 "  "
#         print(f"{star}{empty_space}{star}")
#     else:
#         print(star * square_line)

# treeWidth = 19
# treeHeight = 10
# tree = []
# for i in range(treeHeight):
#     if  (i < (treeHeight - treeHeight/3)):
#         for y in range(treeWidth):
#             if ((y < (i+1) + int(treeWidth/2)) and (y > int(treeWidth/2) - (i+1))):
#                 tree.append('*')
#             else:
#                 tree.append(" ")
#     else:
#         for y in range(treeWidth):
#             if ((y < 1 + int(treeWidth/2)) and (y > int(treeWidth/2) - 1)):
#                 tree.append('*')
#             else:
#                 tree.append(" ")

#     print(*tree, sep='')
#     tree = []
        
# number_of_lines = 4
# for line_number in range(1,number_of_lines+1):
#        print("1" * line_number+"*"* ((number_of_lines-line_number)*2) + "1"*line_number)

# for i in range(0,4):
#     for j in range(0,7-i):
#         print(" ",end="")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print("")

n = 7
treeHeight = int(n / 2) + 1 
trunkHeight = int(treeHeight/2)
for i in range(treeHeight):
    print(' ' * int(n / 2 - i), '*' * (1 + i * 2), ' ' * int(n / 2 - i))
for y in range(trunkHeight):
    print(' ' * int(n / 2), '*', ' ' * int(n / 2))


n = 7
for i in range(4):
    print(' ' * int(n / 2 - i), '*' * (1 + i * 2), ' ' * int(n / 2 - i))
for y in range(2):
    print(' ' * int(n / 2), '*', ' ' * int(n / 2))


numbers = [2, 3, 4, 5, 6]
# superNumbers = []
# lenth = int(input("Введите количество цифр: "))
# for y in range(lenth):
#     superNumbers.append(int(input("Введите цифру: ")))
even = []
uneven = []
for i in numbers:
    residue = (i % 2) 
    if (residue == 0):
        even.append(i)
    else: 
        uneven.append(i)
print("четные - ",  *even, sep=' ')
print("нечетные - ",  *uneven, sep=' ')

faranheitsList = [20, 19, 24, 45] 
celsiusList = []
i = 0
while i < len(faranheitsList):
    celsius = ((faranheitsList[i] - 32) * 5 / 9)
    celsiusList.append(celsius)
    i += 1
    if celsius > 50:
        print("Слишком горячо")
        break
    elif celsius < 5:
        print("Жить можно")
        continue
    print(f"На улице {celsius} по цельсию")


square_line = 4 
star = "*" 
star_width = star * square_line  
i = 0
while i < square_line:
    if i > 0 and i < (square_line - 1): # i < 0 and i < 5; i = 1 2 3 4
        empty_space = " " * (square_line - 2) # 4 "  "
        print(f"{star}{empty_space}{star}")
    else:
        print(star * square_line)
    i += 1
