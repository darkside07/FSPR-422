# bool 
# true \ false
# любое число что не ноль - это правда (труе)
# если переменная пустая - то она ложь (фалсе)

# true = 1 false = 0

# print (false * 3)
x = 10
y = 20
if x > y:
    print(True)
else:
    print(False)

"name surname".split() # {"name", 'surname'}
# a if condition else b
print (True if x > y else False)




# == != > >= < <= is  is not in  not in  not and  or
# [] {} () "" 0 false

if []: # true
    print(True)
if 19: # true
    print(True)

name = "Xumo"
skill = "D2"
age = 18
surname = "Atadjanov"

if name == "Abbos" and skill == "D2": # and - и
    print(name, skill)
else:   
    print("AND")

if name == "Abbos" or skill == "D2": # or - или
    print(name, skill)
else:
    print("OR")

# not - ne
if not age: # not - false - true
    print(age)
else:
    print("Age is False")


if (name == "Xumo" and age > 18) or skill == "D2":
    print(name, age, skill)
else:
    print("Invalid name, age, skill")

if name == "Xumo" or age > 22 and skill == "d2": 
    print(name, age, skill, "second output")
else:
    print("Age is False")

# is, == 
# is - сравнивает id двух знначений 
# == - сравнивает значения 
# id ()

a= 1
b= 1
print(id(a), id(b))

t_1 =()
t_2 =()
print(t_1 is  t_2)
print( id(t_1), id(t_2))
print("1==1", 1==1,1 is 1)


l_1 = [1]
l_2 = [1]
print(id(l_1), id(l_2)) # id разное так как список можно изменить


a_1 = [1,2,3]
a_2 = [1,2,3]
print(a_1 == a_2)
print(a_1 is a_2)



d_1 = {1: 1}
d_2 = {1: 1}
print( "dict" , d_1 == d_2) # сравнивает значения 
print( "dict" , d_1 is d_2) # сравнивает idы