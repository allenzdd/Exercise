# n = int(input())
# stud = list(map(int, input().split()))
# k, d = list(map(int, input().split()))
n = 3
stud = [7,4,7]
k,d = 2, 50

def max_energy(n, stud, k, d):
    opt = [[1] * (len(stud) + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, len(stud) + 1):
            # diagonal
            temp_diagonal = opt[i - 1][j - 1] * stud[j - 1]
            # judge
            opt[i][j] = max(opt[i][j-1], temp_diagonal)
    return opt[-1][-1]

print(max_energy(n, stud, k, d))