info = []
for i in range (10): 
    age = input('введите возраст:')
    name = input('введите имя:')
    info.append( 
        { 
            "age": age, 
            "name": name, 
        } 
    )
print(info)

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
