List = list(map(int, input().split()))

Index = [index for index in range(len(List)) if List[index] % 2 == 1]

print(" ".join(map(str, Index)))

for val in reversed(Index):
    List.pop(val)
print(List)

