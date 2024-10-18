x, y = 0, 0
while (d := input()) != "СТОП":
    n = int(input())
    if d == 'ВОСТОК':
        x += n
    if d == 'ЗАПАД':
        x -= n
    if d == 'ЮГ':
        y -= n
    if d == 'СЕВЕР':
        y += n
print(y)
print(x)