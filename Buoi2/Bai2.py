aList = list(map(int, input().split(" ")))

result = [sum(aList[:i+1]) for i in range(len(aList))]

print(result)
