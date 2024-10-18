n = int(input())
m = int(input())
s = len(str(m * n))
for i in range(1, n + 1):
    for j in range(i, i + n * (m - 1) + 1, n):
        if j == i + n * (m - 1):
            print(str(j).rjust(s, ' '))
        else:
            print(str(j).rjust(s, ' '), end=' ')