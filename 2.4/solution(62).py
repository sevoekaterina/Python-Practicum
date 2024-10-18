n = int(input())
num = 1
ll = 1
while num <= n:
    for i in range(ll):
        if num > n:
            break
        print(num, end=' ')
        num += 1
    print()
    ll += 1
