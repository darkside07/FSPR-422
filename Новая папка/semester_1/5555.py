faranheitsList = [20, 19, 24, 45] 
celsiusList = []
for i in faranheitsList:
    celsius = ((i - 32) * 5 / 9)
    celsiusList.append(celsius)
    if celsius > 50:
        print("Слишком горячо")
        break
    elif celsius < 5:
        print("Жить можно")
        continue
    print(f"На улице {celsius} по цельсию")




faranheits = [20, 19, 24, 45]

for faran in faranheits:
    celsius = (faran - 32) * 5 / 9
    if celsius >= 50:
        print("ЖАРААА")
        continue
    elif celsius <= 5:
        print('очень холодно')
    else:
        print("жить можно")
    print("celsius =", celsius, "faranheit =", faran)