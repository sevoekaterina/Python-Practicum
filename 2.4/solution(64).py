n = int(input())
res = 0
a = [0] * n
for i in range(n):
    while (s := input()) != 'ВСЁ':
        if s == 'зайка':
            a[i] += 1
for i in range(n):
    if a[i] != 0:
        res += 1

print(res)