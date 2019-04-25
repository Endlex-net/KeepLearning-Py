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
    # TODO 2.3.5 作为不可变列表的元组


if __name__ == "__main__":
    main()
