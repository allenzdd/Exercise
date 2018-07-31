def splitNum(n):
    a = int(n / 100)
    b = int((n - a * 100) / 10)
    c = n - a * 100 - b * 10
    return a, b, c


def func(inp):
    # m, n = list[map(int, inp)]
    m, n = inp
    res = []
    for i in range(m, n):
        a, b, c = splitNum(i)
        temp = a ** 3 + b ** 3 + c ** 3
        if temp == i:
            res.append(str(i))
    if len(res) == 0:
        print("no")
    else:
        print(' '.join(res))


inp = [300, 800]
func(inp)
