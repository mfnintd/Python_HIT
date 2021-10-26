s = list(map(lambda x: int(x[1:-1]), input().split(",")))

print(tuple([i for i in s if i % 2 == 0] + [i for i in s if i % 2 == 1]))
