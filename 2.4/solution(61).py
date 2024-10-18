n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        k = i * j

        print(f'{j} * {i} = {k}')
