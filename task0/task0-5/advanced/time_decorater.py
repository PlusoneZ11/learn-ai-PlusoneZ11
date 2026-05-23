# 实现一个装饰器，在开始执行函数时输出该函数名称
# 在结束时输出函数的开始时间和结束时间以及运行时间
import time
from functools import wraps
from datetime import datetime


def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"执行函数: {func.__name__}")

        result = func(*args, **kwargs)

        end_time = time.time()
        end_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elapsed_time = end_time - start_time

        print(f"[结束] 函数: {func.__name__}")
        print(f"  开始时间: {start_time_str}")
        print(f"  结束时间: {end_time_str}")
        print(f"  运行时间: {elapsed_time:.6f}秒")

        return result

    return wrapper


@time_decorator
def factorial(n):
    """计算n的阶乘"""
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


if __name__ == "__main__":
    result1 = factorial(1000)
    result2 = factorial(10000)
    result3 = factorial(100000)
