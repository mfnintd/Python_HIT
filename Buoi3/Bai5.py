from functools import reduce


def MyMathAdd(x, y):
    """
    :param x:
    :param y:
    :return:
        Sum of x and y
    """
    return x + y


def MyMathMutilple(x, y):
    """
    :param x:
    :param y:
    :return:
        Mutilple of x and y
    """
    return x * y


def MyMathShower(*args):
    """
    :param args:
        :argument:
    :return:
        Print Sum, Product, Different
    """
    print(
        reduce(MyMathAdd, args),
        args[0] - reduce(MyMathAdd, args[1:]),
        reduce(MyMathMutilple, args)
    )


MyMathShower(10, 4, 1, 1)
