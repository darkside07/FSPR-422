for val in [1, 2, 3, 4, 5, [6, "Hello",7, 8, 5, 6], (4, 5, 6)]:  
    if isinstance(val, (list, set, tuple)): 
        for i in val: 
            print(i)
    else:
        print(val)
       


firstNumbers = [1, 2, 3, 4, 5, 6 , 7]
secondNumbers = []
for num in firstNumbers:
    secondNumbers.append(num * 4)
print(secondNumbers)



