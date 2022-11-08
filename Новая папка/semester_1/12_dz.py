# def fibonacci(i):
#     if i in (1, 2):
#         return 1
#     return fibonacci(i - 1) + fibonacci(i - 2)
 
 
# print(fibonacci(10))

# [(4, True), (5, False), (3, True)]) -> [6, 30, 125] 
# i = 0 
# while i < 4 + 1: # 6 
#     i += 1 
#     j = 0 # 5 
#     while j < 5: # 5 
#         j += 1 
#         z = 0 # 4 
#         while z < 3: # 4 
#             z += 1 
#             pass # 3 
 
 
# for(int i = 0; i <= 7; i++) { # 0 1 2 3 4 5 6 7 8 = 9 
#     # 0 1 2 3 4 5 6 7 = 8 


def count_loop_iterations(arr):
    res = []
    x = 1
    for n, b in arr:
        res.append(x * (n + b + 1))
        x *= n + b
    return res

arr = [(3, False), (4, True), (6, False)]
print(count_loop_iterations(arr))

