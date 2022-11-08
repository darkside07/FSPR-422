# x = []
# y = int(input("Введите число:"))

# for i in range(y):
#     x.append(i+1)
# print(x)

# x = [1, 2, 3, 4]
# y = 1
# for i in x:
#   y *= i
# print(y)

x = ["home", "car", "boy"]
y = x[0]
x[0] = x[2]
x[2] = y
# y = [1,5,8,9]
# y[0] = 9
print(x)
