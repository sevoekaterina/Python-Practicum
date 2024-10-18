n = int(input())


def pr(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
        
    return n > 1


if pr(n) == 1:
    print('YES')
else:
    print('NO')
