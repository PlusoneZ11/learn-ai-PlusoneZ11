# 设计⼀个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量。
# 具有的公有成员函数是：初始化商品信息的构造函数 init，显示商品信息的函数display，
# 计算已售出 商品价值 income，修改商品信息的函数 setdata
class Products(object):
    def __init__(self, number, name, price, total):
        self.__number = number
        self.__name = name
        self.__price = price
        self.__total = total
        self.__remaining_quantity = total

    def display(self):
        print(f"商品序号: {self.__number}")
        print(f"商品名: {self.__name}")
        print(f"单价: {self.__price}")
        print(f"总数量: {self.__total}")
        print(f"剩余数量: {self.__remaining_quantity}")
        print(f"已售出数量: {self.__total - self.__remaining_quantity}")
        print(f"已售出价值: {self.income()}")

    def income(self):
        sold_quantity = self.__total - self.__remaining_quantity
        return sold_quantity * self.__price

    def setdata(
        self, number=None, name=None, price=None, total=None, remaining_quantity=None
    ):
        if number is not None:
            self.__number = number
        if name is not None:
            self.__name = name
        if price is not None:
            self.__price = price
        if total is not None:
            self.__total = total
        if remaining_quantity is not None:
            self.__remaining_quantity = remaining_quantity
