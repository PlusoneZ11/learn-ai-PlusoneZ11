# 输入⼀个列表（list），列表中含有字符串和整数，删除其中的字符串元素，然后把剩下的整数升序排序，输出列表
import re

print("请输入一个包含字符串和数字的列表")
s = input()
integers = re.findall(r"-?\d+", s)
result = sorted([int(num) for num in integers])
print(result)
