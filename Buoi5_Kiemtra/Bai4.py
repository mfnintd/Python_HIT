def convertBeSangDoc(Num: str):
    """
    Chuyển dãy số Num về cách bé Sang đọc
    :param Num: xâu gồm các chữ số
    :return: xâu là cách bé Sang đọc
    """
    res = ""
    cnt = 1
    for index in range(1, len(Num)):
        if Num[index] != Num[index - 1]:
            res += str(cnt) + str(Num[index-1])
            cnt = 1
        else:
            cnt = cnt + 1
    res += str(cnt) + str(Num[-1])
    return res


Str, n = input().split()
for i in range(int(n)):
    Str = convertBeSangDoc(Str)
    print(Str)
