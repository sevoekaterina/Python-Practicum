n = int(input())

for i in range(n):
    for j in range(n):
        d = min(i, j, n - i - 1, n - j - 1) + 1
        print(str(d).rjust(len(str((n + 1) // 2))), end=' ')
    print()
