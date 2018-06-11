class A(object):
    """Test class A"""

    def __init__(self, x=0):
        self._x = x

    @property
    def x(self):
        """
        Getter

        :return: private variable "x"
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Setter with validation
        Note: Is not available without getter!

        :param x: new value for a private variable "x"
        """
        if x < 0:
            self._x = 0
        elif x > 1000:
            self._x = 1000
        else:
            self._x = x


a = A()
a.x = 50
print(a.x)
