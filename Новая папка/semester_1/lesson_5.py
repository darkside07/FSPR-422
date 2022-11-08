"""
Можете сами почитать про: 
    complex 
    Decimal 
    Fraction 
 
Изменяемые 
    set - множество 
    dict - словарь 
    list - список 
 
Неизменяемые 
    bin 
    frozenset - множество 
    tuple - кортеж 
    int 
    float 
    str 
    bool 
    None

"""

from turtle import home


names = []
print(names)
names = list()
print(names)

# 
names = [1.2,3,4,5,6,12.5,'Abcd', True, None]
print (names)
names[0] = False
# names[7] = "None"
print(names[6][0]) #ABSD - A
#
names = [[2, 3, 4], [4.5, 5.6, 6.6,], ['go','go1','g02']] # вывести на экран строку go2

print(names[2][2])

# нарезка - slice
# интерировать - проходиться по элементам интерируемых переменных (это такие переменные которые могут хранить больше одного значения)

numbers = [4, 5, 6, 10, 22, 55, 500]

# начало:конец
print ( numbers[1:5] ) # 5 не включительно
print ( numbers[:], numbers )
print ( numbers[1:] )
print ( numbers[:5] )

# начало конец шаг
print ("Шаг", numbers[:6:2]) 
print ("Шаг", numbers[:6]) 
print ("Шаг", numbers[::2]) 
print ("Шаг", numbers[::10]) 

print(numbers[-1])

print('home'[::-1])

s = "homework"
home = s[::-1]
print(home)