vvod = input()
N_sep, M_sep = vvod.split(",")
N = int(N_sep)
M = int(M_sep)
arr = [[-1] * N for _ in range(M)]
direction = [(0, 1),(1, 0),(0, -1),(-1, 0)]
curr_x, curr_y = 0, 0
index = 0
for i in range(N * M):
    arr[curr_x][curr_y] = i % 10
    next_x = curr_x + direction[index][0]
    next_y = curr_y + direction[index][1]
    if 0 <= next_x < M and 0 <= next_y < N and arr[next_x][next_y] == -1:
        curr_x = next_x
        curr_y = next_y
    else:
        index = (index + 1) % 4
        curr_x += direction[index][0]
        curr_y += direction[index][1]
for num in arr:
    print(*num)


