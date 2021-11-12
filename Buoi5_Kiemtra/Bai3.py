import math


def checkPrime(Num: int):
    """
    Kiểm tra tính nguyên tố theo toán học
    :param Num: Số nguyên
    :return: True nếu Num là số nguyên tố
    """
    for i in range(2, int(math.sqrt(Num))+1):
        if Num % i == 0:
            return False
    return Num >= 2


def checkPrimeOfHung(Num: int):
    """
    Kiểm tra căn một số có phải là số nguyên tố của Hùng
    :param Num: Số nguyên
    :return:
    True khi Num có đúng 3 ước (Num là số chính phương và căn của Num là số nguyên tố đúng)
    """
    canNum = int(math.sqrt(Num))
    return canNum ** 2 == Num and checkPrime(canNum)


n = int(input())
Arr = list(map(int, input().split()))
Res = [num for num in Arr if checkPrimeOfHung(num)]
if len(Res) == 0:
    print("KHôNG")
else:
    print(len(Res))
