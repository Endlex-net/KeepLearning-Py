"""
    这个demo中模拟了一个二维的变量
"""
from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # def __str__(self):
    # """
    #     str只会在print() 和 str()中被调用
    # """
    #     return "111"

    def __repr__(self):
        """
            repry用在命令行的字符串标示上(应该以无歧义的形式表现)
        """
        # repr 在没有实现 str的时候，会在 str 或 print 中被调用
        return 'Vector(%r, %r)' % (self.x, self.y)  # 这里用%r 可以体现变量原来的类型

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        """
            返回布尔值
        """
        # 当没有__bool__函数的时候，会自动尝试调用__len__
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """
            乘法实现(忽略了乘法交换律)
        """
        return Vector(self.x * scalar, self.y * scalar)


def main():
    print(Vector())
    print(bool(Vector()))
    print(bool(Vector(1, 3)))

    print(Vector(1, 3) * 3)
    # print(3 * Vector(4, 6))
    # TypeError unsupported operand type(s) for *: 'int' and 'Vector'

    # print(Vector(1, 3) * Vector(2, 4))
    # TypeError: unsupported operand type(s) for *: 'int' and 'Vector'


if __name__ == '__main__':
    main()
