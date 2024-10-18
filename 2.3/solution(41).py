k = 0
while (s := input()) != 'Приехали!':
    k += s.count('зайка')
print(k)