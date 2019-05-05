"""
    列表推导和生成器表达式
"""


def main():
    symbols = '%^&$*('
    symbol = 'time'
    codes = [ord(symbol) for symbol in symbols]
    print(codes)
    # 在 python3 中 推导式不再会有变量泄漏的问题
    print(symbol)  # time

    # 推导式与filter，map比较
    print([ord(symbol) for symbol in symbols if ord(symbol) > 40])
    print(list(filter(lambda c: c > 40, map(ord, symbols))))

    # 笛卡尔乘积
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    # 这里需要注意生成后的顺序：是优先排列 前一个循环条件
    t_shirts = [(color, size) for color in colors for size in sizes]
    print(t_shirts)

    # 生成器表达式
    # 生成器可以避免内存占用，其原理使用了协程, 并不会将数据一次性取到内存中
    # 具体的详情在后续协程中会详细说明
    generator_obj = ('%r,%r' % (color, size) for color in colors for size in sizes)
    print(type(generator_obj))
    print(generator_obj)
    print(next(generator_obj))  # next(generator_obj)
    print(list(generator_obj))

    # 元组不仅仅是不可变的列表
    # 元组的更多用途在于记录，有点像DDD中的值对象的概念, 将多组数据捆绑成一个标示一个信息
    lax_coordinates = (33.9425, -118.408056)
    latitude, longitude = lax_coordinates
    print(latitude, longitude)
    # * 运算符可以标示一个可迭代对象
    print(divmod(1, 3))
    a_tuple = (1, 3)
    print(divmod(*a_tuple))
    # * 也可以做一个强大的占位符
    a, b, *c, d = [1, 2, 3, 4, 5, 6]
    print(a, b, c, d, )  # 1 2 [3, 4, 5] 6

    # 命名元组
    # namedtuple构建的类所消耗的内存与元组是一样的，比对象实例要小一点，没有__dict__存放属性
    import collections
    Card = collections.namedtuple('Card', 'rank, suit')
    # Card = collections.namedtuple('Card', ['rank', 'suit'])
    card = Card(2, 'hearts')
    print(card)
    # 命名元祖属性创建后不可再次更改
    # card.rank = 3 AttributeError: can't set attribute
    print(card._fields)  # 打印名字元祖中的属性
    # 通过元祖来创建名字元组
    card_tuple = (3, 'hearts')
    print(Card._make(card_tuple))
    print(card._asdict())  # 通过 OrderedDict的形式返回元组, OrderedDict: 有顺序的dict

    # 切片
    l = [10, 20, 30, 40, 50, 60]
    print(l[:2])
    print(l[2:])

    s = 'bicycle'
    print(s[::3])
    print(s[::-1])
    print(s[::-2])

    print(l)
    l[2:5] = [100]
    print(l)

    a = [1, 2, 3]
    print(a * 5)
    print(5 * 'abcd')

    board = [['_'] * 3 for i in range(3)]
    print(board)
    board[1][2] = 'x'
    print(board)

    l = [1, 2, 3]
    print(l)
    print(id(l))
    l *= 2  # 本地乘
    print(l)
    print(id(l))

    t = (1, 2, [30, 40])
    try:
        t[2] += [50, 60]  # TypeError: 'tuple' object does not support item assignment
    except BaseException as e:
        print(e)

    print(t)

    # 这个问题很神奇，我本来以为 答案会是 (1, 2, [30, 40, 50, 60]), 因为[30, 40]是个可变变量，其实就是一个内存的指针
    # 但是结果却是发生了异常，并且 t的结果发生了改变
    # 引发异常的原因，是因为增量赋值并不是一个原子操作。
    # 所以在元组之内，我们应该尽量避免出现填入可变对象

    # list.sort 与 sorted
    a = [3, 5, 1, 5, 7, 4]
    print(sorted(a))  # sorted 会返回一个排序后的新列表(浅复制)
    print(a)

    print(a.sort())  # .sort() 没有返回值，会直接在原来的数组之上进行排序
    print(a)

    # 这两个函数都存在一个共有的参数， key(制定排序规则), reverse(控制正反序列)
    a = ['time', 'nihao', 'me', 'python']
    print(sorted(a, reverse=True, key=lambda x: x[-1]))

    # 排序是一个十分耗时的工作，对于已经排好的序列，我们应该妥善管理
    # 使用bisect管理已经排序的序列(通过二分查找实现)
    # bisect 的实现只是通过 大小(<) 比较, 没有实现，排序规则的指定(key), 但是有指定排序范围的工具
    import bisect
    a = [1, 4, 6, 7, 9, 10]
    a.sort()
    print(a)
    print(bisect.bisect(a, 8))  # 返回应该插入的位置
    # 更多的排序功能实现 应该看下 cookie book
    # https://docs.python.org/3/howto/sorting.html 这篇官方文档有一些排序的妙用

    # list 虽然是一个不错的工具，但是我们有时候需要使用更加专业的工具

    # 队列
    # 利用.append 和 .pop 我们可以把list当作队列(栈)使用, 但是在删除第一个元素或者增加第一个元素是个很耗时的过程
    # collections.deque 双向队列，是个线程安全，可以快速从两端添加或者删除元素的数据类型
    from collections import deque
    dq = deque(range(15), maxlen=10)  # 开头的5个被弹出了
    print(dq)
    dq.rotate(3)  # 旋转操作
    print(dq)
    dq.appendleft(-1)
    print(dq)
    dq.extend([1, 2, 3])
    print(dq)
    # deque 实现了几乎所有的list 方法, 但是并不推荐操作中间部分，因为实现方式是双向链表
    print(dq[3])

    # 其他队列:
    # queue
    # multiprocessing
    # asyncio
    # heapq

    # array 数组, array 在对数组处理上更加高效，并且拥有一个序列化工具
    # 感觉如果需要用到 array 那一定是一个非常非常大的数组了
    from array import array
    from random import random
    fs = array('d', (random() for i in range(10 ** 6)))
    # print(fs)  # 我为什么要想不开
    print(fs[-1])

    # memeoryview 与 NumPy, SciPy
    # memv = memoryview([1, 3, 4, 5, 6, 7, -1])  # TypeError: memoryview: a bytes-like object is required, not 'list'
    memv = memoryview(array('d', [1, 4, 5, 67, 9, 7, 5, 45, 3]))
    print(memv)
    print(len(memv))


if __name__ == "__main__":
    main()
