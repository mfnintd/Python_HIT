Str = input()
Answer = 0

for i in range(len(Str)):
    for j in range(i+1, len(Str)+1):
        if Str.count(Str[i:j]) >= 2:
            Answer = max(Answer, j-i+1)

print(Answer)
