n = int(input())
d = []
dantoc = []
for i in range(n):
    a, b = input().split()
    d.append([a, b])
    dantoc.append(b)
d.sort(key=lambda x: dantoc.count(x[1]))

print(" ".join([i[0] for i in d if dantoc.count(i[1]) == dantoc.count(d[-1][1])]))
