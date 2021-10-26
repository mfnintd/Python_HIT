aList = list(map(int, input().split()))
k = int(input())

cnt = 0
for i in range(len(aList)):
    cnt += aList[i + 1:].count(k - aList[i])

print(cnt)
