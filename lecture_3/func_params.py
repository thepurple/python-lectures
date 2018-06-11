"""
Function parameters test
"""


# pylint: disable=invalid-name
def test_params(x1, y1, x2, y2):
    """
    Test

    :param x1: ddd
    :param y1: ddd
    :param x2:
    :param y2:
    :return:
    """
    print(f"({x1}, {y1}) - ({x2}, {y2})")


def test_args(*args):
    print(f"({args[0]}, {args[1]}) - ({args[2]}, {args[3]})")


def test_kwargs(**kwargs):
    print("({}, {}) - ({}, {})"
          .format(kwargs['x1'], kwargs['y1'], kwargs['x2'], kwargs['y2']))


test_params(x1=1, y1=1, x2=2, y2=3)
test_args(*(1, 1, 2, 2))
test_kwargs(**{"x1": 1, "y1": 1, "x2": 2, "y2": 3})
