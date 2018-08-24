def get_same_max(n, pai_list):
    x = []
    y = []
    [[x.append(ele[0]), y.append(ele[1])] for ele in pai_list]
    sum_x = sum(x)
    opt = [[0] * (sum_x + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        mxi = sum(x[:i])
        if i == 1:
            sub_i = [x[0]]
        else:
            temp_sub = sub_i.copy()
            [[sub_i.append(ele + x[i - 1]), sub_i.append(ele - x[i - 1])]
             for ele in temp_sub]
        # print(sub_i)
        for j in range(sum_x + 1):
            if j <= mxi:
                temp1, temp2 = 0, 0
                if j == x[i - 1] or (j - x[i - 1]) in sub_i:
                    # print(j)
                    temp1 = opt[i - 1][j - x[i - 1]] + y[i - 1]
                if j == x[i - 1] or (j + x[i - 1]) in sub_i:
                    temp2 = opt[i - 1][j + x[i - 1]] + y[i - 1]

                opt[i][j] = max(opt[i - 1][j], temp1, temp2)

                if i == 1 and j == 0:
                    opt[i][j] = 0
                    # print(11111111)
                    # print(opt[1][0])
    print(opt)
    return opt[-1][0]


def get_same_max_2(n, pai_list):
    x = []
    y = []
    [[x.append(ele[0]), y.append(ele[1])] for ele in pai_list]
    sum_x = sum(x)
    opt = [[0] * (2 * sum_x + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        mxi = sum(x[:i])
        if i == 1:
            sub_i = [x[0]]
        else:
            temp_sub = sub_i.copy()
            [[sub_i.append(ele + x[i - 1]), sub_i.append(ele - x[i - 1])]
             for ele in temp_sub]

        for j_i in range(2 * sum_x + 1):
            j = j_i - sum_x
            if abs(j) <= mxi:
                temp1, temp2 = 0, 0
                if abs(j) == x[i - 1] or (j - x[i - 1]) in sub_i:
                    temp1 = opt[i - 1][j_i - x[i - 1]] + y[i - 1]
                if abs(j) == x[i - 1] or (j + x[i - 1]) in sub_i:
                    temp2 = opt[i - 1][j_i + x[i - 1]] + y[i - 1]

                opt[i][j_i] = max(opt[i - 1][j_i], temp1, temp2)

                if i == 1 and j == 0:
                    opt[i][j_i] = 0
    return opt[-1][sum_x]


if __name__ == '__main__':
    n = 4
    # Inp = [[3, 1], [2, 2], [1, 4], [1, 4]]
    Inp = [[2, 2], [1, 4], [1, 4], [3, 1], ]
    print(get_same_max_2(n, Inp))
