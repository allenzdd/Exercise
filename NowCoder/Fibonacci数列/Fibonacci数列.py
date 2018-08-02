# N = int(input())

N = 15


def func(N):
    pre, cur = 0, 1

    while N > cur:
        cur_ = cur
        cur = pre + cur
        pre = cur_

    return min((cur - N), (N - pre))


print(func(N))
