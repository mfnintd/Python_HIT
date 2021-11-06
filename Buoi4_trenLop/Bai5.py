def Nhap():
    """
    :return:
        a dictionary of number and a number X that are entered
    """
    List = list(map(int, input().split()))
    x = int(input())
    return List, x


def Xuly(List, x):
    """
    Delete the first x in List
    Print the index of the first x
    :param List: List
    :param x: int
    :return: nothing
    """
    for index in range(len(List)):
        if List[index] == x:
            List.pop(index)
            print(index)
            return


def XoaX(List, x):
    """
    Delete all number X in List
    :param List:
    :param X:
    :return: nothing
    """
    while x in List:
        List.remove(x)


def Check(List, x, y):
    """
    check y and insert x in index y
    :param List:
    :param y:
    :return:
    """
    if y<0 or y >= len(List):
        print("Không chèn được")
    else:
        List.insert(y, x)


List, x = Nhap()
Xuly(List, x)
XoaX(List, x)
print(List)
y = int(input())
Check(List, x, y)
print(List)