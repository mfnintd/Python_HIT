s = input("a, Nhập chuỗi: ")
while (len(s) < 10):
    s = input("Nhập lại: ")

print(len(s))
print(s[2:7])

s = input("b, Nhập chuỗi: ")
for c in s:
    if "A" <= c <= "Z":
        print(c, end="")
print()
for c in s:
    if "a" <= c <= "z":
        print(c, end="")
print()
print(s.replace("b", "g"))

print("c, ", end="")
s = "hElLo-mY-NAMe-iS-SuZIe"

# print(“Hello My Name Is Suzie”)

print(s.replace("-", " ").title())
