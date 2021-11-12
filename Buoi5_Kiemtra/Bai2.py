def luckyNumber(Num: int):
    """
    :param Num: Số nguyên
    :return: True nếu tổng các ước khác Num lớn hơn Num
    """
    return sum([num for num in range(1, Num // 2 + 1) if Num % num == 0]) > Num


n = int(input())
Arr = list(map(int, input().split()))

Ans = [num for num in Arr if luckyNumber(num)]
print(len(Ans))
print(" ".join(map(str, sorted(Ans))))
