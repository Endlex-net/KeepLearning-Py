import collections
from random import choice

"""
    这个demo 快速创建了一套卡牌对象
"""

# namedtuple 可以快速创建一个没有方法的对象
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 牌号
    suits = 'spades diamonds clubs hearts'.split()  # 花色

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    # 当同时实现__len__ 和 __getitem__ 两个特殊方法，则实现了大多数python 有序序列的执行前提
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position: int) -> Card:
        """
            __getitem__ 实现了将对象变为可迭代对象, 可以通过 obj[key]进行快速调用
        """
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card: Card) -> int:
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def main():
    # 创建一张牌
    beer_card = Card("7", "diamonds")
    print(beer_card)
    print(type(beer_card))

    # 创建一套卡牌
    deck = FrenchDeck()
    print(len(deck))

    # random.choice 可以实现对可迭代对象的随机选择, 通过len(obj) 取出随机范围，然后随机抽取, 可对列表对象进行使用
    print(choice(deck))
    print(choice(deck))

    # 实现了__getitem__的可迭代对象，可以使用for 循环进行遍历
    print([card for card in deck])

    # reversed(list) 可以快速构造一个反向的生成器
    print(reversed(deck))
    print([card for card in reversed(deck)])

    # __contains__ 方法被隐式实现了，因为FrenchDeck是可迭代的对象
    print(Card('Q', 'hearts') in deck)

    # 实现了spades_high 则实现了排序的顺序比对
    print([card for card in sorted(deck, key=spades_high)])

    """
        FrenchDeck 实现了object类， 我们可以通过实现一些特殊函数，来实现Python语言的核心特性(迭代,切片)
        同时可以使用标准库中的 random.choice, reversed, sorted 等功能.
        另外，同时__len__ 和 __getitem__ 的实现 可以代理给 自身的list 对象(self._cards)
    """


if __name__ == "__main__":
    main()
