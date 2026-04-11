# 写一个正则表达式，用于验证用户密码，长度在 6~18 之间，只能包含英文和数字
import re

pattern = r"^[a-zA-Z0-9]{6,18}$"

# 测试用例
test_passwords = [
    "abc123",  # 有效: 6个字符
    "Pass1234",  # 有效: 8个字符
    "Abc123456789012345",  # 有效: 18个字符
    "12a",  # 无效: 太短
    "abc1234567890123456",  # 无效: 太长(19个字符)
    "abc 123",  # 无效: 包含空格
    "abc_123",  # 无效: 包含下划线
]


# 测试函数
def validate_password(password):
    if re.match(pattern, password):
        return True
    else:
        return False


# 运行测试
print("密码验证测试:")
print("-" * 40)
for pwd in test_passwords:
    result = "有效" if validate_password(pwd) else "无效"
