# xp=int(input('Wxp: '))
# damage=int(input("damage: ")) 
# mp=int(input("mp: "))
 
# if xp<=100 and  damage<=10 and mp<=50:
#     print("Уровень 1")
# elif xp<=300 and damage<=20 and mp<=100:
#     print("Уровень 10")
# elif  xp<=500 and damage<=100 and mp<=200:
#     print("Уровень 15")
# else:
#     print("Вы герой")


print (type("qwerty"))

val = input('введите что то:')
if type(val) == int or type(val) == str:
    print(True)
else:
    print(False)


a= [1, 2, 3, 4, 5, 6, 7]
for i in range(len(a)):
  a[i] *=4
print(a)

a=[1, 2, "hello", 4, 5, 6, 7]
del a[2]
del a[5]
for i in range(len(a)):
     a[i] *=4
     print(a)