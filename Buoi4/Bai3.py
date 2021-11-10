List = list(map(int, input().split('+')))

List.sort()

print('+'.join(map(str, List)))
