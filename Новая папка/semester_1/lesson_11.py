# **** 
# *  * 
# *  * 
# **** 
# square_line = 4 
# star = "*" 
# star_width = star * square_line 
# print(star_width) 
# print(f"{star}  {star}") 
# print(f"{star}  {star}") 
# print(star_width) 

square_line = 4 
star = "*" 
star_width = star * square_line  

for i in range(square_line):
    # prinnt("I", i)
    if i > 0 and i < (square_line - 1): # i < 0 and i < 5; i = 1 2 3 4
        empty_space = " " * (square_line - 2) # 4 "  "
        print(f"{star}{empty_space}{star}")
    else:
        print(star * square_line)


i = 0
while i < 10: # true - будет работать
    print("i =", i) # 9
    i += 1 # 9 + 1 = 10
i = 0
while True:
    i += 1
    print("i", i)
    if i == 100:
        break

names = [1, 2, 3, 4, 5, 6]
i = 0
while i < len(names):
    print(names[i])
    i += 1


#############

for val in enumerate("ABDHJD"):
    print(val)

for i, val in enumerate("ABDHJD"):
    print(i, val)

list = [1, 2, 4, 4, 2, 5, 6]
print ("Оригинальный список : " + str(list))
list = []
for i in list:
  if i not in list:
    list.append(i)
print ("список после удаления дубликатов : " + str(list))