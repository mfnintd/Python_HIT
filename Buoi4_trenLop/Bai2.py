String = input()

ans = ""
if len(String) < 2:
    pass
else:
    ans = String[:2] + String[-2:]

print(ans)
