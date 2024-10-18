n = int(input())

res = int(input())


def efk(x, y):
    while y > 0:
        x, y = y, x % y
    return x


for i in range(n - 1):
    num = int(input())
    res = efk(res, num)

print(res)