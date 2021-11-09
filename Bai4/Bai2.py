Str = input()

if len(Str) > 10:
    Str = Str[0] + str(len(Str)-2) + Str[-1]

print(Str)