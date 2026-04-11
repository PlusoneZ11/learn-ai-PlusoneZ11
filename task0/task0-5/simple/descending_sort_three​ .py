# 从大到小输出三个数

print("输入三个数")
x, y, z = map(int, input().split())

# 方法1 条件分支
if x > y > z:
    print(x, y, z)
elif x > z > y:
    print(x, z, y)
elif y > x > z:
    print(y, x, z)
elif y > z > x:
    print(y, z, x)
elif z > y > x:
    print(z, y, x)
elif z > x > y:
    print(z, x, y)

# 方法2 列表
nums = [x, y, z]
nums.sort(reverse=True)
print(nums[0], nums[1], nums[2])

# 方法3 排序交换
if y > x:
    x, y = y, x
if z > x:
    x, z = z, x
if z > y:
    y, z = z, y
print(x, y, z)

# 方法4 max min函数
max_ = max(x, y, z)
min_ = min(x, y, z)
mid_ = (x + y + z) - max_ - min_
print(max_, mid_, min_)
