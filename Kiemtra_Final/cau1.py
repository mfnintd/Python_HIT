a, b, n = map(int, input().split())

d = {i: i**2 for i in range(a, b+1) if i % n == 0}

print(d)