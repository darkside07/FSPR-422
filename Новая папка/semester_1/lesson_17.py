
"""
1 вопрос
Роль PVM заключается в преобразовании инструкций байт-кода 
в машинный код, чтобы компьютер мог выполнять эти инструкции машинного кода и отображать результат
"""


"""

2 вопрос 
int- целые число
str -строка 
float - дробное число
операторы - (+,//,/,%,*,**)
bool -True/False

"""


"""

3 вопрос
не изменяемые
int
float
str
tuple


изменяемые 

list
dict

"""
""""
4 вопрос

# name='Xumo'
# surname='Otadjonov'
# age=18
# a='меня зовут {},моя фамилия {},и мне {} '.format(name,surname,age) 
# print(a)
# a='меня зовут {1},моя фамилия {0},и мне {2} '.format(name,surname,age) 
# print(a)
# a=f'меня зовут {name},моя фамилия {surname},и мне {age} '
# print(a)
# a=f'меня зовут {name:<10},моя фамилия {surname:<10},и мне {age:<10} '
# print(a)


5 вопрос
IS
in и not in — операторы принадлежности в Python. Они проверяют, есть ли значение или переменная в последовательности (строке, списке, кортеже, множестве или словаре). Иначе говоря, проверяют вхождение элемента в коллекцию.

IN
in и not in — операторы принадлежности в Python. Они проверяют, есть ли значение или переменная в последовательности (строке, списке, кортеже, множестве или словаре). Иначе говоря, проверяют вхождение элемента в коллекцию.

6 вопрос
Python содержит три разных типа области видимости: 
Локальная область видимости Глобальная область видимости Нелокальная область видимости
"""
""""
7 
None возвращает
"""
#     1 
def resheniye(arr):
    checkNum = len(arr[0])
    checkSym = ""
    for i in arr:
        if (len(i) <= checkNum):
            checkNum = len(i)
            checkSym = i
    print(checkSym, " - ", checkNum)
    return checkNum
            
arr = ["hi", "hello", "say"]
print(resheniye(arr))

#           3


string1= "You've got that fire (fire). The flavor, the style (style)"

list1=list(string1.split(". "))
print(list1)



# 4

names = [] 
for i in range(10): 
    names.append(i+4) 
    if i == 7: 
        names.pop(0) 
print(names)


# 6
obj = {
    "race": "orge",
    "age": "100", 
    "skill": ["Roar"],
}
if "race" in obj and "age" in obj and isinstance(obj["age"], int):
    print(obj["race"], obj["age"])
else:
    print("human")