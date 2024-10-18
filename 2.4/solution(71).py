n = int(input())
m = int(input())
s = len(str(m * n))
for i in range(1, n + 1):
    for j in range(m * (i - 1) + 1, m * i + 1):
        if j == m * i:
            print(str(j).rjust(s, ' '))
        else:
            print(str(j).rjust(s, ' '), end=' ')
