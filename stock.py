price_str = 1
print(type(price_str))
if isinstance(price_str, str):
    price_str = str(price_str)
elif isinstance(price_str, float):
    price_str += 1.0
else:
    try:
        raise TypeError('price_str is other type')
    except TypeError as ex:
        print(ex.args)
        print("catch error TypeError")
    except MemoryError:
        print("catch error MemoryError")
    finally:
        print('finally')
    
    
print(type(price_str))

price_array = [30.14,31.14,33.14,35.14,36.14,7.14]
date_array = []
date_base = 20231019
for _ in range(0, len(price_array)):
    date_array.append(str(date_base))
    date_base += 1
print(date_array)

date_array = []
date_base = 20231019
price_cnt = len(price_array)
while price_cnt > 0:
    date_array.append(str(date_base))
    date_base += 1
    price_cnt -= 1
print(date_array)

date_base = 20231019
date_array = [str(date_base + ind) for ind, _ in enumerate(price_array)]
print(date_array)

# 元组
stock_tuple_list = [(date, price) for date, price in zip(date_array, price_array)]
print('第一条{}'.format(stock_tuple_list[1][1]))
print(stock_tuple_list)

# 可命名元组
from collections import namedtuple
stock_namedtuple = namedtuple('stock', ('date', 'price'))
stock_namedtuple_list = [stock_namedtuple(date, price) for date, price in zip(date_array, price_array)]
print('第一条{}'.format(stock_namedtuple_list[1].price))
print(stock_namedtuple_list)

# 字典推导式
stock_dict = {date:price for date,price in zip(date_array, price_array)}
print('第一条{}'.format(stock_dict['20231019']))
print(stock_dict)
print(stock_dict.keys())
print(stock_dict.values())

# 有序字典
from collections import OrderedDict
stock_dict = OrderedDict((date, price) for date, price in zip(date_array, price_array))
print(stock_dict.keys())

# 函数
print(min(stock_dict))
print(min(zip(stock_dict.values(), stock_dict.keys())))

def find_second_max(dict_array):
    stock_prices_sorted = sorted(zip(dict_array.values(), dict_array.keys()))
    return stock_prices_sorted[-2] #倒数第二个
if callable(find_second_max):
    print(find_second_max(stock_dict))


# lambda函数
find_second_max_lambda = lambda dict_array : sorted(zip(dict_array.values(), dict_array.keys()))[-2]
print(find_second_max_lambda(stock_dict))

def find_max_and_min(dic_array):
    stock_prices_sorted = sorted(zip(dic_array.values(), dic_array.keys()))
    return stock_prices_sorted[0], stock_prices_sorted[-1]
print(find_max_and_min(stock_dict))


from functools import reduce
pp_array = [(price1, price2) for price1, price2 in zip(price_array[:-1], price_array[1:])]
print(pp_array)
change_array = list(map(
    lambda pp: reduce(lambda a,b : round((b-a)/a, 3), pp),
    pp_array
))
change_array.insert(0, 0)
print(change_array)

stock_namedtuple = namedtuple('stock', ('date', 'price', 'change'))
stock_dict = OrderedDict((date, stock_namedtuple(date, price, change)) for date, price, change in zip(date_array, price_array, change_array))
print(stock_dict)

# filter
up_days = filter(lambda day : day.change > 0, stock_dict.values())
print(list(up_days))

def filter_stock(stock_array_dict, want_up=True, want_calc_sum=False):
    if not isinstance(stock_array_dict, OrderedDict):
        raise TypeError('stock_array_dict must be OrderedDict')
    filter_func = (lambda day:day.change>0) if want_up else (lambda day:day.change<0)
    # 使用filter_func作为筛选函数
    want_days = filter(filter_func, stock_array_dict.values())

    if not want_calc_sum:
        return list(want_days)
    
    change_sum = 0.0
    for day in want_days:
        change_sum += day.change
    return change_sum

print("all up days:{}".format(filter_stock(stock_dict)))
print("all down days:{}".format(filter_stock(stock_dict, want_up=False)))
print("all up sum:{}".format(filter_stock(stock_dict, want_calc_sum=True)))
print("all down sum:{}".format(filter_stock(stock_dict, want_up=False, want_calc_sum=True)))

# 偏函数
from functools import partial

filter_stock_up_days = partial(filter_stock, want_up=True, want_calc_sum=False)
filter_stock_down_days = partial(filter_stock, want_up=False, want_calc_sum=False)
filter_stock_up_sum = partial(filter_stock, want_up=True, want_calc_sum=True)
filter_stock_down_sum = partial(filter_stock, want_up=False, want_calc_sum=True)

print("all up days:{}".format(filter_stock_up_days(stock_dict)))
print("all down days:{}".format(filter_stock_down_days(stock_dict)))
print("all up sum:{}".format(filter_stock_up_sum(stock_dict)))
print("all down sum:{}".format(filter_stock_down_sum(stock_dict)))


# 面向对象
# 类
from collections import namedtuple
from collections import OrderedDict
class StockTradeDays(object):
    def __init__(self, price_array, start_date, date_array=None):
        #私有价格序列
        self.__price_array = price_array
        #私有日期序列
        self.__date_array = date_array
        #私有涨幅序列
        self.__date_change = self.__init_change()
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
            date_array = [str(start_date + ind) for ind in enumerate(self.__price_array)]
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

