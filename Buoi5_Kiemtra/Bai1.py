a, b = input().split()
cnt = 0
for i in range(0, len(b)-len(a)+1):
    if a == b[i:i+len(a)]:
        cnt = cnt + 1
print(cnt)