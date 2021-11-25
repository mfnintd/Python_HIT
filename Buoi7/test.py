import pandas as pd
import numpy as np

"""
s1 = pd.Series([1, 2, 3, 4])  # Tạo Series (Không truyền index)
print(s1)

s2 = pd.Series((1, 2, 3, 4), index=(1, 2, 3, 4))  # Tạo Series (Truyền index)
print(s2)
# print(s2[5])

s3 = pd.Series([1, 2, 3, 4], index=["as", 2, "as", "xlll"])  # Tạo Series (Truyền index trùng nhau)
print(s3)
print(s3["as"])  # in ra nhiều phần tử có index giống nhau

data = {"as": 1, 2: 2, "as": 3, "xlll": 4}
ser = pd.Series(data, index=["as", 2, "as", "bphone", "xlll"])  #tạo Series từ dist
# Note: Không tạo 2 phần tử có index giống nhau có giá trị khác nhau được do tính chất của dict
# index bphone có giá trị NaN do không có :/
#
print(data)
print(ser)

s4 = pd.Series("aa", index=['a', 1, 'ca', 3])  # Tạo Series từ Scalar (Một đại lượng)
print(s4)
print(s4['a'])

"""
"""

print(s3[1:3])

ar = np.asarray(s3)
print(ar)
ar = np.asarray(ser)
print(ar)
"""
"""

print("\n", s3.index)
print("\n", s3.array)
print("\n", s3.values)
print("\n", s3.size)
"""
"""
    DataFrame
"""
# print("\n")
"""
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series((1, 2, 3, 4), index=(1, 2, 3, 4))
s1 = {"một": s1, "hai": s2}
df1 = pd.DataFrame(s1)

# Thêm cột "giống một", "ba", "check" với giá trị theo công thức
df1["giống một"] = df1["một"]
df1["ba"] = df1["một"] - df1["hai"]
df1["check"] = df1["ba"] == df1["một"]
# Thêm cột "bốn" với giá trị vô hướng
df1["bốn"] = "Hello"
# Thêm cột không cùng số lượng index
df1["khác"] = df1["một"][1:4]
# insert
df1.insert(2, "hai rưỡi", df1["một"])

del df1["hai"]
df1.pop("ba")

print(df1["giống một"])

print(df1.loc[0])


# df2 = pd.DataFrame(s, index=[1, 2, 3])
# print(df2)
"""
"""
s = {"một": pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     "hai": pd.Series([2, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df3 = pd.DataFrame(s)

# Chọn các dòng có df["hai] > 2
print(df3[df3["hai"] > 2])
"""

df = pd.read_csv('a.csv', index_col=0)
print(df["táo"]["duy"])
