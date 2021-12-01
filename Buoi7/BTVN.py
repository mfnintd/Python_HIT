import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


def avgCalc(nums):
    """
    avgCalc(nums):

    Calculate average of non-nan value in nums

    :param nums: array_like
    :return: Average of non-nan value in nums
    """
    res = 0
    cnt = 0
    for num in nums:
        if not np.isnan(num):
            res = res + num
            cnt = cnt + 1
    if cnt == 0:
        return None
    return res / cnt


shellInfo = pd.read_csv('categorical_data.csv')

print(shellInfo)

shellInfo2 = shellInfo.copy()

imputer = SimpleImputer(missing_values=np.NaN, strategy='mean')
"""
SimpleImputer dùng để bổ sung, thay thế các giá trị
missing_values: Tất cả các missing_values sẽ được thay thế
strategy: chiến lược dùng để thay thể, 'mean' -> thay thế bằng giá trị trung bình của các giá trị còn lại
"""

# print(shellInfo2['age'].values.reshape(shellInfo2['age'].size, 1))

shellInfo2.age = imputer.fit_transform(shellInfo2.age.values.reshape(shellInfo2.age.size, 1))

shellInfo2.salary = imputer.fit_transform(shellInfo2.salary.values.reshape(shellInfo2.salary.size, 1))
"""
fit_transform được gọi trên imputer để xác định giá trị giá trị phù hợp và thay đổi
shellInfo2.age.values.reshape(shellInfo2.age.size, 1): 
    lấy mảng giá trị của age/salary, đổi thành dạng cột, gán lại cho cột ban đầu
"""
print("Sử dụng SimpleImpute:\n", shellInfo2)

shellInfo3 = shellInfo.copy()

fill_value_age = avgCalc(shellInfo3.age)
fill_value_salary = avgCalc(shellInfo3.salary)
"""
Tính toán các giá trị trung bình cần thay thế vào missing data
"""

shellInfo3.age = shellInfo3.age.replace(np.nan, fill_value_age)
shellInfo3.salary = shellInfo3.salary.replace(np.nan, fill_value_salary)
"""
dùng replace thay thể NaN thành giá trị trung bình đã tính toán
"""

print("Tính tay:\n", shellInfo3)
