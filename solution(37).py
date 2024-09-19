a = int(input())
b = int(input())
c = int(input())
ma = max(a, b, c)
ni = min(a, b, c)
sr = a + b + c - ma - ni
if ma ** 2 == (sr ** 2 + ni ** 2):
    print('100%')
elif ma ** 2 > (sr ** 2 + ni ** 2):
    print('велика')
else:
    print('крайне мала')

