# -*- coding: utf-8 -*-

from Stack import Stack

from copy import copy
import operator
import sys

TRUE = -1
FALSE = 0

Data = Stack()


def add():
    """ This is a custom `add` implementation. """
    Data.push(Data.pop() + Data.pop())


def subtract():
    """ This is a custom `subtract` implementation. """
    a, b = Data.pop(), Data.pop()
    Data.push(b - a)


def multiply():
    """ This is a custom `multiply` implementation. """
    Data.push(Data.pop() * Data.pop())


def divide():
    """ This is a custom `divide` implementation. """
    a, b = Data.pop(), Data.pop()
    Data.push(int(b / (a*1.0)))


def drop():
    Data.pop()


def swap():
    a, b = Data.pop(), Data.pop()
    Data.push(a)
    Data.push(b)


def dup():
    Data.push(copy(Data.peek()))


def dot():
    """ Pop 'n print! """
    print(Data.pop())


def dot_s():
    """ Print stack and stack height. """
    print("<{}> {}".format(Data.height(), ' '.join([str(i) for i in Data.contents])))


def mod():
    """ Custom mod. """
    a, b = Data.pop(), Data.pop()
    Data.push(operator.mod(b,a))


def words():
    """ List the known words. """
    word_list = ''
    for word in Words:
        word_list += word + ' '
    print(word_list)
