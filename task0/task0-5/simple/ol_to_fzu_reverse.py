# 判断输入的字符串中是否含有 "ol" ，若有把所有的 "ol" 替换为 "fzu"，最后把字符串倒序输出
print("输入一个字符串")
text = input()
s = "ol"
if s in text:
    new_text = text.replace(s, "fzu")
    print(new_text[::-1])
else:
    print(text[::-1])
