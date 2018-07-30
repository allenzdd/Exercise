# # time exceed
# def func(n, m, table, cust):
#     table.sort()
#     cust = sorted(cust, key=lambda l: l[0])
#     money = 0
#     for i in range(n):
#         temp_money_list = []
#         for j in range(len(cust)):
#             if cust[j][0] > table[i]:
#                 break
#             else:
#                 temp_money_list.append(cust[j])
#         temp_money_list = sorted(
#             temp_money_list, key=lambda l: l[1], reverse=True)

#         if temp_money_list:
#             table_i_money = temp_money_list[0]
#             money += table_i_money[1]
#             cust.remove(table_i_money)

#     return money


# bisection
# nums is sorted by asc
def search(nums, target):
    if target <= nums[0]:
        return 0
    elif target > nums[-1]:
        return -1
    else:
        l = 0
        r = len(nums) - 1
        while l + 1 != r:
            m = (l + r) // 2  # only select left num
            if target <= nums[m]:
                r = m
            else:
                l = m
    return r


def func(n, m, table, cust):
    table.sort()
    cust = sorted(cust, key=lambda l: l[1], reverse=True)  # sorted by price
    money = 0
    count = 0
    for j in range(m):
        i = search(table, cust[j][0])
        if i >= 0:
            count += 1
            money += cust[j][1]
            # table.remove(table[i]) # time exceed
            del table[i]
            if count == n:
                break
    return money


# n, m = 3, 5
# table = [2, 4, 2]
# cust = [
#     [1, 3],
#     [3, 5],
#     [3, 7],
#     [5, 9],
#     [1, 10]
# ]

n, m = 4, 6
table = [12, 1, 4, 7]
cust = [
    [11, 3],
    [3, 10],
    [35, 10],
    [5, 9],
    [12, 10],
    [6, 7],
]

print(func(n, m, table, cust))
