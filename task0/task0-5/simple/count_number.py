# 创建一个函数，可以统计一个只有数字的列表中各个数字出现的次数，通过字典方式返回
def count_num(l):
    result = {}
    for num in l:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result
