def bag(v_list, w_list, total_weight):
    # m = total_length
    m = len(v_list) - 1
    n = total_weight
    opt = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if w_list[i] > j:
                opt[i][j] = opt[i - 1][j]
            else:
                opt[i][j] = max(opt[i - 1][j], opt[i - 1]
                                [j - w_list[i]] + v_list[i])

    return opt[-1][-1]


v_list = [0, 60, 100, 120]
w_list = [0, 10, 20, 30]
total_weight = 50
# n = 4

print(bag(v_list, w_list, total_weight))

