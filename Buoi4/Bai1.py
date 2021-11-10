Str = input()

a, b = Str[Str.index('(')+1:Str.index(')')].split(',')

print(a, b)
