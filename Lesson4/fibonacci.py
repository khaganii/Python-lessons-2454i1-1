import time
#recursiv ---------------------------------
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)


# start_time = time.time()
# print(fibonacci(40))
# print("--- %s seconds ---" % (time.time() - start_time))

#20 -> 0.0012209415435791016
#30 -> 0.14534521102905273
#33 -> 0.623478889465332
#35 -> 1.6477136611938477
#38 -> 7.110353708267212
#40 -> 15.194514513015747
#40 -> 4.267692565917969


#memoization ---------------------------------
level = {}
def fibonacci(n):
    if n in level:
        return level[n]
    if n == 1 or n == 2:
        return 1

    s1 = fibonacci(n-1)
    s2 = fibonacci(n-2)
    level[n] = s1 + s2
    return level[n]

start_time = time.time()
print(fibonacci(100))
print("--- %s seconds ---" % (time.time() - start_time))


#iterativ ----------------------------------------------
# def fib(n):
#     f = 1
#     s = 1
#     current = 2
#     for i in range(3, n+1):
#         current = f+s
#         s = f
#         f = current
#     return current
# print(fib(100))
