n = str(input())
list = [int(n[0]), int(n[1]), int(n[2])]
mi = min(list)
ma = max(list)
sr = sum(list) - mi - ma
if mi + ma == sr * 2:
    print('YES')
else:
    print('NO')