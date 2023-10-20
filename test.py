#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'wdjxysc'

import sys
import numpy
from enum import Enum,unique
import logging #可打印异常堆栈
from io import StringIO
from io import BytesIO
import os
import json 


def test():
    args = sys.argv
    if len(args)==1:
        print('Hello World!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def tryCatch():
    try:
        r = 10/int('0')
        print('result:', r)
    except ValueError as e:
        logging.exception(e)
    except ZeroDivisionError as e:
        logging.exception(e)
    else:
        print('no error!')
    finally:
        print('finally...')
    print('the end')

def readFile():
    f = ''
    try:
        f = open('C:\\Users\\Administrator\\Desktop\\智能检测服务列表.txt', 'r', encoding='utf-8')
        # lines = f.readlines()
        print(f.read())
        print('---------------------------------------------------------------------------')
        for line in f.readlines():
            print(line.strip()) # 把末尾的'\n'删掉
    except IOError as e:
        logging.exception(e)
    finally:
        if f:
            f.close()
    print('---------------------------------------------------------------------------')
    with open('C:\\Users\\Administrator\\Desktop\\智能检测服务列表.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    print('readFile end')


class Student(object):

    def __init__(self):
        self.name = ''
        self.score = ''

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    def cash(self, money):
        print('cash: %s' % (money))

def student2dict(std): #转json用
    return {
        'name': std.name,
        'score': std.score
    }

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
    bart.cash(1000)
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
    tryCatch()
    readFile()
    print('name:%s, environ:%s' % (os.name, os.environ))

    s = Student('ada wong', 100)
    print(json.dumps(s, default=student2dict))
    print(json.dumps(s, default=lambda obj: obj.__dict__))

    json_str = '{"name": "Bob", "score": 88}'
    r = json.loads(json_str)
    print(type(r))
    
    rebuild = json.loads(json_str, object_hook=lambda d: Student(d['name'], d['score']))
    print(type(rebuild))
    print(rebuild.name)
