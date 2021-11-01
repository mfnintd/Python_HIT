def xd10(x):
    """
    :param x:
        A string
    :return:
        True if that string has character 0 or 1
        False if it doesn't
    """
    if '0' in x or '1' in x:
        return True
    else:
        return False


def convertIndex01(x):
    """
    :param x:
        String
    :return:
        Tuple: Indexes of 0, 1 in x
    """
    return tuple([i for i in range(len(x)) if x[i] in ['0', '1']])


def ss10(x, y):
    """
    :param x:
        String 1
    :param y:
        String 2
    :return:
        True if Indexes of 0, 1 in x and y are the same
        False if they aren't
    Note: No need to use
    """
    if convertIndex01(x) == convertIndex01(y):
        return True
    else:
        return False


List = input().split()
listConvert = set()

for Point in List:
    listConvert.add(convertIndex01(Point))

print(len(listConvert))


