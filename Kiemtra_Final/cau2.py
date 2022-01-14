ARR = list(map(int, input().split()))

S = set(ARR)

ans = []

for i in S:
    ans.append([i] * ARR.count(i))
    
print(ans)