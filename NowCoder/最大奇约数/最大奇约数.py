# N = int(input())
N = 7


# def func(n):
#     if n == 1:
#         return 1
#     elif n % 2 == 0:
#         res = n**2 / 4 + func(n / 2)
#     else:
#         res = n + func(n - 1)
#     return int(res)

def func(n):
    res = 0
    while n > 0:
        res += ((n + 1) // 2) * ((n + 1) // 2)
        n = n // 2
    return res


print(func(N))
