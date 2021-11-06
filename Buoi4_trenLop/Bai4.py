def Nhap():
    """
    :return:
        List that entered
    """
    global n
    n = int(input())
    List = list(map(int, input().split()))
    return List


def Dem(List):
    """
    :param List:
        a List
    :return:
        a Dictionary that has quantity of each number
    """
    Set = set(List)
    Dict = dict()
    for valSet in Set:
        cnt = 0
        for valList in List:
            if valSet == valList:
                cnt += 1
        Dict[valSet] = cnt
    return Dict


def In(a, b):
    """
    print according to the format "a : b"
    :param a:
    :param b:
    :return:
        nothing
    """
    print(a, ":", b)


n: int

Dict = Dem(Nhap())

for key in Dict:
    In(key, Dict[key])

