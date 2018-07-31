def func(N, nums):
    mindp = [0]
    [mindp.append(1e+10) for i in range(N)]
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if nums[i - j] == 0:
                continue
            elif (i - j) + nums[i - j] >= i:
                mindp[i] = min(mindp[i], mindp[i - j] + 1)
    if mindp[N] == 1e+10:
        return -1
    else:
        return mindp[N]


N = 5
nums = [2, 0, 1, 1, 1]

print(func(N, nums))
