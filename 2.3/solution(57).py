n = int(input())


def pr(x):
    for i in range(2, int(x * 0.5) + 1):
        if x % i == 0:
            return 0
    return x > 1


dd = [0] * n
for i in range(2, n):
    c = 0
    if n % i == 0 and pr(i):
        while n % i == 0:
            c += 1
            n //= i
    dd[i] = c
res = ''
for i in range(len(dd)):
    if dd[i] != 0:
        res += f'{i} * ' * dd[i]
print(res[:-2])
