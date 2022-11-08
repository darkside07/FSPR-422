# dictionary - словарь
# ключем словаря могут быть только не изменямые типы переменных

from os import remove


user_data = {
    "ключь": "значение",
    1: None,
    2: 21,
    3: 6.7,
    4: [2,3,4],
    5: {"key": "другой словарь"}
}   
# print(user_data[1],user_data[2],user_data[3],user_data[4],user_data[5], sep='\n')

user_data = {
    "username": "Gobby",
    "password": "392i55",
    "age": "15"
}
print(user_data["age"])


user_data = [
    { 
    "username": "Gobby",
    "password": "392i55",
    "age": "15"
    },
    {
    "username": "Gobby",
    "password": "392i55",
    "age": "13"
    
    },
]

user_data = [
    {
            "username" : "gobby",
            "password" : "asjdasjdw",
            "age": 14,
    },

        {
            "username" : "abbos",
            "password" : "wioqdjssjdw",
            "age": 17,
    }
]


print(user_data[0]["age"],user_data[1]["age"]) 
user_data = {
    "username": "abbos",
    "password": "djs;aldj",
    "age": 12

}
user_data["age"] = 18
print(user_data.keys(), user_data.values(), user_data.items(), sep= '\n')

user_list= list(user_data.values())
print(user_list)

print("get:",user_data.get('age'),user_data.get("name"))

# # set - множество
# numbers = {2, 3, 4, "hello", 2, 4}
# print(numbers)
# numbers = {}
# print = (type(numbers))
# numbers = set()
# print (type(numbers))

remove_duplicates = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, "aa", "bb", "aa"]
print( remove_duplicates, set(remove_duplicates), sep="\n")

print(list(set(remove_duplicates)))