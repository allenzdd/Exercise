def LCS(str1, str2):
    m = len(str1)
    n = len(str2)
    opt = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                opt[i][j] = opt[i - 1][j - 1] + 1
            else:
                opt[i][j] = max(opt[i - 1][j], opt[i][j - 1])
    return opt[-1][-1]


s1 = '1A2C3D4B56'
s2 = 'B1D23CA45B6A'
print(LCS(s1, s2))
