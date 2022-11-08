# область видимости - scope
# LEGB - LOcal Enclosed Global Built-in
# ЛВГВ - Локальный Вложенный Глобальный Встроенный

# print(print) # builtin.

# #
# name = "Xumo" # global

# def get():
#     name = "xumo"
#     print(name)

# get()

# #######

# name = "xumo"

# def spam():
#     global name
#     name = "abbos"

# print(name)

# ##########

# def foo(items):
#     items.append(42)

# a = (1, 2, 3, 4, 5, 6, 7)

# foo(a)
# print(a)

# ##

# def bar (items):
#     items = [4, 5, 6]

# b = [1, 2, 3]
# bar(b)
# print(b)

from re import A


def parent():
    a = 5
    return a
print("не вложенный", parent()) # 5

def parent():
    a = 5
    def answer():
        return a
    return answer()
print("вложенный", parent()) # 5

#########

def outer():
  # enclossed
    x = "local"

    def inner():
        # local
        nonlocal x
        x = "non local"
        print("inner:", x)

    inner()
    print("outer:", x)
outer()

##########

# global
a = 20
def parent():
    # enclosed
    a = 5
    def answer():
        # local
        a = 10
        def get():
            return a      
        return get()
    return answer()