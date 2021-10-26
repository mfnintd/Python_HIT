n = int(input())

while n >= 10:
    n = sum([int(c) for c in str(n)])

print(n)
