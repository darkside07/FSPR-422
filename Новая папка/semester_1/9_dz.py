Number = int(input("Введите число: "))
Degree = int(input("Введите степень: "))

def logic(number, degree):
    return number ** degree
    
print(logic(Number, Degree))

def logic(n, num):
    numbers = []
    for i in range(n):
        numbers.append(i * num)
    return numbers

print(logic(20, 3))