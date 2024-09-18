a = int(input())
b = int(input())
c = int(input())
if max(a, b, c) == a:
    print('Петя')
elif max(a, b, c) == b:
    print('Вася')
else:
    print('Толя')