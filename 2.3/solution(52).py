n = int(input())
res = 'ЯЯЯЯЯЯЯЯЯЯ'
for i in range(n):
    k = input()
    res = min(k, res)

print(res)
