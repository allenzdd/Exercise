import time


def quicksort(lists):
    if len(lists) <= 1:
        return lists
    else:
        left = []
        right = []
        pivot = lists.pop()

        for x in lists:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
                print(left + [pivot] + right)
        return quicksort(left) + [pivot] + quicksort(right)

# def QuickSort(myList, start, end):
#     # 判断low是否小于high,如果为false,直接返回
#     if start < end:
#         i, j = start, end
#         # 设置基准数
#         base = myList[i]

#         while i < j:
#             # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
#             while (i < j) and (myList[j] >= base):
#                 j = j - 1

#             # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
#             myList[i] = myList[j]

#             # 同样的方式比较前半区
#             while (i < j) and (myList[i] <= base):
#                 i = i + 1
#             myList[j] = myList[i]
#         # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
#         myList[i] = base

#         # 递归前后半区
#         QuickSort(myList, start, i - 1)
#         QuickSort(myList, j + 1, end)
#     return myList


def time_it(func):
    def wrapper(*args, **kwargs):
        t_start = time.time()
        res = func(*args, **kwargs)
        t_end = time.time()
        print(t_end - t_start)
        return res
    return wrapper


# @time_it
# def Main(range_length, length):
#     import random
#     lists = random.sample(range(range_length), length)
#     print(f"The random list is {lists}")
#     QuickSort(lists, 0, length - 1)
#     print(f"The sorted lists is {lists}")


# Main(3000000, 100000)

@time_it
def main(range_length, length):
    import random
    lists = random.sample(range(range_length), length)
    print(f"The random list is {lists}")
    res = quicksort(lists)
    print(f"The sorted lists is {res}")


main(30, 5)

# @time_it
# def main_2(range_length, length):
#     import random
#     lists = random.sample(range(range_length), length)
#     print(f"The random list is {lists}")
#     res = sorted(lists)
#     print(f"The sorted lists is {res}")


# main_2(3000000, 100000)
