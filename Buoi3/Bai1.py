def xd10(x):
    """
    :param x:
        A string
    :return:
        True if that string has character 0 or 1
        False if it doesn't
    """
    if "0" in x or "1" in x:
        return True
    else:
        return False


def convertIndex01(x):
    """
    :param x:
        A string
    :return:
        A string that have same length
            1 replace for character '0' and '1'
            0 replace for the rest
    """
    x = x.replace("0", "1")
    otherChars = "23456789"
    for otherChar in otherChars:
        x = x.replace(otherChar, "0")
    return x


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
    if xd10(Point):
        listConvert.add(convertIndex01(Point))

print(len(listConvert))


