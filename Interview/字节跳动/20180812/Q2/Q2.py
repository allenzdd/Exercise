def combine_interval(inte_list):
    res = []
    # print(111)
    inte_list = sorted(inte_list, key=lambda l: l[0])
    for inte in inte_list:
        if not res or inte[0] > res[-1][1]:
            res.append(inte)
        else:  # elif inte[0] < res[-1][1]
            res[-1][1] = max(res[-1][1], inte[1])
    return res


inte_list = [[1, 10], [32, 45], [78, 94], [
    5, 16], [80, 100], [200, 220], [16, 32]]


n = int(input())
inte_list = []
for i in range(n):
    line = list(map(str, input().split(';')))
    [inte_list.append(list(map(int, x.split(',')))) for x in line]

print(combine_interval(inte_list))
