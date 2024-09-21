a = int(input())
b = int(input())
c = int(input())
ma = max(a, b, c)
mi = min(a, b, c)
sr = a + b + c - ma - mi
if sr + mi > ma:
    print('YES')
else:
    print('NO')