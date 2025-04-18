def calculate_sub(a, b):
    if a > b:
        a = a-b
        return calculate_sub(a, b)
    print("ended -> ", a)
    return None

print(calculate_sub(90, 10))

# ls = [1,4,5,5,6,4,2,34,3434,543,23]
# def check(n):
#     if n % 2 == 0:
#         print("cut")
#     else:
#         print("tek")
#
# def rec(i): #2
#     if i < len(ls) :
#         check(ls[i])
#         i = i + 1  # 2
#         rec(i)
#     return None

#rekursiv
# print(rec(0))

#iterativ
# for num in ls:
#     check(num)

