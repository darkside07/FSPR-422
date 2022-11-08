a, b, *args = (2, 4, 4, 7, 8, 9, 0)
print(a, b, args)

for i in range (10): 
    print(i)

print("Next range")
for i in range (4, 10):
    print (i)

print("Next range")
for i in range (4, 10, 2):
    print (i)

# continue

numbers = [1, 2, 3, 5, 4, 5, 6, 7]
for val in numbers:
    if val == 5 or val == 7:
        print(f"пропустить {val}")
        continue
    print("vaal  =", val)
    

# break

numbers = [1, 2, 3, 5, 4, 5, 6, 7]
for val in numbers:
    if val == 5 or val == 7:
        print("выйти из цикла")
        break
    print("vaal  =", val)       


if 1 == 1:
    pass