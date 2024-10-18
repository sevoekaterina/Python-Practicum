a = int(input())
b = int(input())
c = a
d = b
while b > 0:
    a, b = b, a % b
print((c * d) // a)