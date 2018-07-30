def func(num, elem):
    max_sum = int(elem[0])
    current_sum = int(elem[0])
    for i in range(1, num):
        temp = int(elem[i])
        if current_sum < 0:
            current_sum = temp
        else:
            current_sum += temp
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


num = 10

elem = [-1, -2, -3, -4, -5, 0, -6, -7, -8, -9]


print(func(num, elem))
