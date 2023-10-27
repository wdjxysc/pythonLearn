# 面向对象
# 类
from functools import reduce
from collections import namedtuple
from collections import OrderedDict
class StockTradeDays(object):
    def __init__(self, price_array, start_date, date_array=None):
        #私有价格序列
        self.__price_array = price_array
        #私有日期序列
        self.__date_array = self._init_days(start_date, date_array)
        #私有涨幅序列
        self.__change_array = self.__init_change()
        #进行OrderDict的组装
        self.stock_dict = self._init_stock_dict()
    def __init_change(self):
        """
        从price_array生成change_array
        :return:
        """
        price_float_array = [float(price_str) for price_str in self.__price_array]
        pp_array = [(price1, price2) for price1, price2 in zip(price_float_array[:-1], price_float_array[1:])]
        change_array = list(map(
            lambda pp: reduce(lambda a, b: round((b-a)/a, 3), pp),
            pp_array
        ))
        # list insert()插入数据 将第一天的涨跌幅设为0
        change_array.insert(0, 0)
        return change_array
    def _init_days(self, start_date, date_array):
        """
        protect 方法,
        :param start_date: 初始日期
        :param date_array: 给定日期序列
        :return:
        """
        if date_array is None:
            # 由start_date和self.__price_array来确定日期序列
            date_array = [str(start_date + ind) for ind, _ in enumerate(self.__price_array)]
        else:
            # 稍后的内容会使用外部直接设置的方式
            # 如果外面设置了date_array,就直接转换str类型组成新的date_array
            date_array = [str(date) for date in date_array]
        return date_array
    def _init_stock_dict(self):
        """
        使用namedtuple, OrderedDict将结果合并
        :return:
        """
        stock_namedtuple = namedtuple('stock', ('date', 'price', 'change'))
        # 使用已被赋值的__date_array等进行OrderedDict的组装
        stock_dict = OrderedDict(
            (date, stock_namedtuple(date, price, change)) 
            for date, price, change in
            zip(self.__date_array, self.__price_array, self.__change_array)
        )
        return stock_dict
    def filter_stock(self, want_up=True, want_calc_sum=False):
        """
        筛选结果子集
        :param want_up: 是否刷选上涨
        :param want_calc_sum: 是否计算涨跌幅和
        :return:
        """
        # Python中的三目表达式的写法
        filter_func = (lambda day:day.change > 0) if want_up else (lambda day:day.change < 0)
        # 使用filter_func作为筛选函数
        want_days = list(filter(filter_func, self.stock_dict.values()))
        if not want_calc_sum:
            return want_days
        # 需要计算涨跌幅和
        change_sum = 0.0
        for day in want_days:
            change_sum += day.change
        return change_sum
        """
        下面的
        """
    def __str__(self):
        return str(self.stock_dict)
    __repr__ = __str__
    def __iter__(self):
        """
        通过代理stock_dict的迭代,yield元素
        :return:
        """
        for key in self.stock_dict:
            yield self.stock_dict[key]
    def __getitem__(self, ind):
        date_key = self.__date_array[ind]
        return self.stock_dict[date_key]
    def __len__(self):
        return len(self.stock_dict)

        

price_array = '30.14,29.58,26.36,32.56,32.82'.split(',')
date_base = 20170118
# 从StockTradeDays类初始化一个实例对象trade_days,内部会调用__init__
trade_days = StockTradeDays(price_array, date_base)
print(trade_days)
print(len(trade_days))


from collections.abc import Iterable
# 如果trade_days是可迭代的对象,依次打印出
if isinstance(trade_days, Iterable):
    for day in trade_days:
        print(day)

filter_days = trade_days.filter_stock()
print(filter_days)
