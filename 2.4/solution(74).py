n = int(input())
m = int(input())
matrix = [[0] * m for _ in range(n)]

number = 1
for j in range(m):
    if j % 2 == 0:
        for i in range(n):
            matrix[i][j] = number
            number += 1
    else:
        for i in range(n - 1, -1, -1):
            matrix[i][j] = number
            number += 1

max_len = len(str(n * m))
for row in matrix:
    print(' '.join(str(x).rjust(max_len) for x in row))
