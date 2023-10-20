#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'wdjxysc'

import sys
import numpy
from enum import Enum,unique



def test():
    a = numpy.arange(15).reshape(3, 5)
    print(a)
    args = sys.argv
    if len(args)==1:
        print('Hello World!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')




class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

@unique #装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__=='__main__':
    test()
    bart = Student('bob', 99)
    print(bart)
    bart.print_score()
    str = 'sdf'
    print(type(123))
    print(type('123'))
    print(type(bart))
    print(type(test))
    print(dir(test))
    print(dir(bart))
    print(dir(str))
    Month = Enum('Month', ('Jan'))
    print(Month.Jan)
    day1 = Weekday.Sun
    print(day1)
    print(day1.value)