s = input()
num = s.count("1")

if num % 2:
    print("NO")
else:
    cnt = 0
    for c in s:
        print(c, end="")
        if c == "1":
            cnt += 1
        if cnt == num / 2:
            cnt = num
            print(" ", end="")

