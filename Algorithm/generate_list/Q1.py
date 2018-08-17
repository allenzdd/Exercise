def func(a_list):
    res = []
    for i in range(2 ** len(a_list)):
        combo = []
        for j in range(len(a_list)):
            if (i >> j) % 2 == 1:
                combo.append(a_list[j])
        res.append(combo)
    return res


def main(range_len, length):
    import random
    lists = random.sample(range(range_len), length)
    print(f'the list is {lists}')
    print(f'the subset of list are {func(lists)}')


main(30, 10)
