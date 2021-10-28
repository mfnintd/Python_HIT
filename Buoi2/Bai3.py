s = input("a, Nhập chuỗi: ")
while len(s) < 10:
    s = input("Nhập lại: ")

print(len(s))
print(s[2:7])

s = input("b, Nhập chuỗi: ")
print(s.upper())
print(s.lower())
print(s.replace("b", "g"))

print("c, ", end="")
s = "hElLo-mY-NAMe-iS-SuZIe"

# print(“Hello My Name Is Suzie”)

print(s.replace("-", " ").title())
