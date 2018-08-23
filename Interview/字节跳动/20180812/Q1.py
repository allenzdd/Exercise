def sum_group(i, j, m, n, maps):
    queue = [[i, j]]
    people_sum = 1
    maps[i][j] = 0
    # 8 direction
    direction = [[1, 0], [1, -1], [0, -1],
                 [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
    while queue:
        x = queue[0][0]
        y = queue[0][1]
        for dire_i in direction:
            x_dir = x + dire_i[0]
            y_dir = y + dire_i[1]
            if 0 <= x_dir < m and 0 <= y_dir < n and maps[x_dir][y_dir] == 1:
                queue.append([x_dir, y_dir])
                people_sum += 1
                maps[x_dir][y_dir] = 0
        del queue[0]

    return people_sum


def main(m, n, maps):
    team = []
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 1:
                team.append(sum_group(i, j, m, n, maps))
    return team


maps = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
m = 10
n = 10

team = main(m, n, maps)

print(team)

print(len(team), '----', max(team))
