def greet():
    print("Hello")

# вызов функции
print("вызов функции", greet())

def greet():
    return "Hello" # return - вернуть

result = greet()
print(result)

# ---------------

def greet(name):
    print(F"Hello {name}")

greet("Xumo")
s = "Xumo"
greet(s)
greet( input("input name: "))

def greet(name):
    return F"Hello {name}"

print(greet("Abbos"))
result = greet("Oybek")
print(result)





square_line = 4
star = "*" 
star_width = star * square_line  

def fars_to_cels(square_line, star):
    if fars_to_cels > 0 and fars_to_cels < (square_line - 1): 
        empty_space = " " * (square_line - 2) # 4 "  "
        print(f"{star}{empty_space}{star}")
    else:
        print (star * square_line)
    
square_line = 4 
star = "*" 
def draw_square(square_line, star):
    for i in range(square_line):
        if i > 0 and i < (square_line - 1): # i < 0 and i < 5; i = 1 2 3 4
            empty_space = " " * (square_line - 2) # 4 "  "
            print(f"{star}{empty_space}{star}")
        else:
            print(star * square_line)
draw_square(10, "2")
