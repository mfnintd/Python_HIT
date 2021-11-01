A = {"An", "Binh", "Nam", "Long", "Ngoc", "Tu"}
B = {"Binh", "Linh", "Nam", "Hai", "Long"}
# a
A.remove("Tu")
# b
A.add("Cuong")
# c
C = A.union(B)
# d
D = A.intersection(B)
# e
E = A.difference(B)
# f
F = A.symmetric_difference(B)
