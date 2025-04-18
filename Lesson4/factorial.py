def factorial(n): # 4
    if n == 1 or n == 0:
        return 1
    return factorial(n-1) * n



# //2 ---- 1! * 2
# //3 ---- 2! * 3 = 6
# //4 ---- 3! * 4 = 24
# //5 ---- 4! * 5 = 120

print(factorial(5))

# mul = 1
# for i in range(1, 1000):
#     mul *= i
# print(mul)