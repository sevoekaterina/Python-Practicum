N = int(input())
M = int(input())
T = int(input())
hours = (N + (M + T) // 60) % 24
minutes = (M + T) % 60
print(f'{hours // 10}{hours % 10}:{minutes // 10}{minutes % 10}')
