## 基础容器

### 列表：list

**定义**：有序、可变、元素类型可不同，可嵌套。

**索引**：访问 list 中每一个位置的元素。

- 从 0 开始；-1 获取最后一个元素。
- 正向索引：`0~len(x)-1`，反向索引：`-len(x)~-1`。
- 当索引超出范围时，会报 IndexError 错误。
  
**切片**：等同于字符串索引。

- `[start:end:step]`。
- 切片赋值是改变原列表的排列，不会生成新列表。
- 对于**步长为 1**的切片赋值，完成的功能是连续替换，等号左右总数可以不等。
- 对于**步长大于 1**的切片赋值，完成的是逐一替换，故等号左右数要一致。
- 切片被字符赋值时，字符串会被拆开，字符串长度要和切片长度一致。

**运算**：

- `+`号用于拼接列表。
- `*`号用于生成重复的列表。
- 比较运算是对对应位置上的元素进行的，需要保持类型一致。

**常用属性方法**：

- 增：`append(x)`，`extend(list)`，`insert(index,obj)`。

- 删：`remove(x)`：删除第一次出现。
`pop([index])`：删除并返回指定位置的元素；默认末尾，同时返回移除元素；会修改原列表。
`clear()`：清空列表，同于`L[ : ]=[ ]`。

- 查：`index(element[, start[, end]])`：返回（第一个）对应元素的索引。
`count(x)`：返回元素的个数。

- 排序：`reverse()` ：列表反转。
`sort(reverse=False)`：升序排列，（reverse=True 降序）。

- 复制：`L.copy()`：浅拷贝。

**列表推导式**：用可迭代对象，依次生成列表内元素

- `[表达式 for变量 in可迭代对象 if条件表达式]`

### 字典：dict

**定义**：以键-值存储的集合，一一对应，可存储任意类型，无序，键必须不可变且唯一。

**创建**：

- 空字典：`d={ }`。
- `d = dict(name="Bob", age=30)`。
- `d = {"name":"xiaoming","age":35}`。

**访问**：`d[key]`，`d.get(key, default)`。

**常用操作**：

- 增/改：`d[key] = value`.

- 删：`pop(key)`移除键，同时返回键对应的值，`del d[key]`，`clear()`

- 合并：`d1.update(d2)`:将字典d2合并到d1中，若键相同则取代

- 复制：`copy()`。

**视图**

- `D.keys()`                     返回可迭代的dict_keys集合对象。
- `D.values()`                  返回可迭代的dict_values集合对象。
- `D.items()`                   返回可迭代的dict_items集合对象。
  
**遍历**：`for k,v in d.items():`。

**成员判断**：`key in d`。

**生成函数**：

- `dict()`创建空字典                         `d1=dict()`。
- `dict(iterable)`用可迭代对象创建    `d1=dict([('name','amy'),('age',15)])`。
- `dict(**kwargs)`关键字参数创建   `d1=dict(name='amy',age=17)`。

**字典推导式**：`{键表达式 : 值表达式 for 变量 in 可迭代对象(if 条件表达式) }`

---

## 函数

### 匿名函数（lambda）

**特点**：简洁，无需函数名，创建后即用。

**语法**：`lambda [参数1，参数2，…] : 表达式`

- [ ]内的部分可省略。
- 创建一个匿名函数对象，同def类似但不提供函数名
- 不必担心函数名冲突，匿名函数也是一个函数对象

**使用**：可赋值给变量调用，或直接作为参数传递。

### 装饰器

**定义**：接受函数为参数，返回新函数的闭包函数，在代码运行期间动态增加功能。

**语法**：`@装饰器名` 放在函数定义前。

- 在被装饰函数定义完成后立即执行。
- 把 `@log` 放到 `now()` 函数的定义处，相当于执行了语句：`now = log(now)`。
- 本质：`func = decorator(func)`

**基本结构**：

```python
def metric(text):    #接受一个参数（比如要显示的文字）
 def decorator(func):    #接受要被装饰的函数
     def wrapper(*args, **kwargs):    #实际执行函数的地方
         # 前置处理
         result = func(*args, **kwargs)
         # 后置处理
         return result
     return wrapper
 return decorator

@decorator
def target_function():
    pass
```

---

## 面向对象

### Class（类）

#### 定义与创建

- **类**：创建对象的模板，包含属性和方法。

- **对象**：类的实例，拥有具体属性值。

- **创建**:
 **class关键字+类名**（通常是大写开头）**+(object)**（表示该类是从哪个类继承下来的，如果没有合适的继承类，就使用object类）。

**`__init__`方法**：可以在创建实例时把必须绑定的属性强制填写进去。
第一个参数永远是`self`，表示创建的实例本身。
不能传入空的参数，需要传入与`__init__`方法匹配的参数。

```python
  class Student(object):
     # 类属性
      school = "福州大学"
       def __init__(self, name, score):
        # 实例属性
           self.name = name
           self.score = score
  # 创建实例
  stu1 = Student("xiaomig", "90")

  # 访问属性
  print(stu1.name)  # xiaomig
  # 类属性是所有实例共享的
  print(stu1.school)  # 福州大学
```

- **实例**：
创建 ：`实例 = 类名(参数)`
调用：`实例.变量名`
模块中调用：`模块名.实例.变量名`

#### 属性

- **实例属性**：属于具体实例，通过 `self.属性` 或 `实例.属性` 访问。

- **类属性**：在class中定义，归类所有，所有实例共享。

- **关系**：
实例属性优先级比类属性高，因此它会屏蔽掉类的属性。
不要对实例属性和类属性使用相同的名字，相同名称的实例属性将屏蔽掉类属性。
删除实例属性后，再使用相同的名称，访问到的将是类属性。

- **属性操作函数**：
`hasattr(obj, name)`：检查对象obj是否拥有指定属性name，可避免getattr()引发错误。
`getattr(obj, name, default)`：获取对象的属性值，getattr(x,'y')等同于x.y，当属性不存在时返回default。
`setattr(obj, name, value)`：给对象obj的name属性设置相应的值，set(x,'y',v)等同x.y=v。
`delattr(obj, name)`：删除对象obj的name属性，delattr(x,'y')等同del x.y。

- **访问变量的方法**

1. **实例方法**：
  定义在类内的函数，第一个参数为self，
  可访问类变量和实例属性，若无return则返回None，
  实例.实例方法名（调用参数），
  类名.实例方法名（实例，调用参数）。
  
2. **类方法@classmethod**
  只能访问类变量，第一个参数是类的实例，
  类名.方法名() 或 实例.方法名。
  
3. **静态方法@staticmethod**
  定义在类的内部，只能凭借该类和实例调用。
  与普通函数定义相同。
  不能访问类变量和实例属性，类实例和对象实例可以调用。
  
4. 总结：
  不想访问类变量和实例变量，用静态方法，
  只想访问类内变量，不想访问实例属性用类方法，
  既想访问类内变量，又想访问实例属性用实例方法。

- **获取对象信息**
  **type()函数**：判断对象类型：基本类型、指向函数或者类的变量。返回对应的Class类型。

  **isinstance()函数**：判断class的类型是否是该类型本身，或者位于该类型的父继承链上。能用`type()`判断的基本类型也可以用`isinstance()`判断
  
  **dir()函数**：获得一个对象的所有属性和方法，返回一个包含字符串的list

---

### Magic Methods（魔法方法)

#### 特点

双下划线包围，在特定操作时自动调用。

#### 常用魔法方法

- 初始化
`__init__(self, ...)`​ 在实例创建后被调用,初始化实例的属性。

- 字符串
`__str__(self)`    返回对象的字符串表示。调用`str()`和`print()`时使用。
`__repr__(self)`  返回对象的正式字符串表示。调用`repr()`时使用。

- 比较
`__eq__(self, other)`  相等比较，对应 == ，
`__ne__(self, other)`  不等比较，对应`!=`，
`__lt__(self, other)`  小于比较，对应`<`，
`__gt__(self, other)`  大于比较，对应`>`，
`__le__(self, other)`   小于等于比较，对应`<=`，
`__ge__(self, other)`  大于等于比较，对应`>=`，

- 算术运算
`__add__(self, other)`  加，
`__sub__(self, other)`  减，
`__mul__(self, other)`  乘，
`__truediv__(self, other)`除，
`__floordiv__(self, other)`  整数除法 //，
`__mod__(self, other)`取模 %，
`__pow__(self, other)`  幂运算。

- 类型转换
`__int__(self)` 转换为整数，调用int()时使用。
`__float__(self)`  转换为浮点数，调用float()时使用。
`__complex__(self)`  转换为复数，调用complex()时使用。
`__bool__(self)`  转换为布尔值，调用bool()时使用。
`__index__(self)`   转换为整数索引，用于切片和bin()、hex()、oct()函数。

- 容器类
`__len__(self)` 返回容器长度，调用`len()`时使用。
`__getitem__(self, key)` 获取容器中指定元素，对应`self[key]`操作。
`__setitem__(self, key, value)`设置容器中指定元素，对应`self[key] = value`操作。
`__delitem__(self, key)` 删除容器中指定元素，对应`del self[key]`操作。
`__iter__(self)`返回迭代器对象，用于迭代容器。
`__next__(self)` 迭代器的下一个值，调用`next()`时使用。
`__reversed__(self)`​  返回反向迭代器，调用`reversed()`时使用。
`__contains__(self, item)`  成员测试，对应`item in self`操作。

- 属性访问
`__getattr__(self, name)` 当访问不存在的属性时调用。
`__getattribute__(self, name)` 访问任何属性时都会调用，优先级高于`__getattr__`。
`__setattr__(self, name, value)`设置属性值时调用。
`__delattr__(self, name)` 删除属性时调用。
`__dir__(self)` 返回属性列表，调用`dir()`时使用。

- 描述符
`__get__(self, instance, owner)` 获取描述符的值。
`__set__(self, instance, value)` 设置描述符的值。
`__delete__(self, instance)` 删除描述符。

- 哈希
`__hash__(self)`返回对象的哈希值，用于字典键和集合元素。
`__eq__(self, other)`实现对象的相等比较。
注意：`__hash__`和`__eq__`需要一起实现，如果类定义了`__eq__`但没有定义`__hash__`，则实例不可哈希。

- 复制
`__copy__(self)`浅拷贝实现，调用`copy.copy()`时使用。
`__deepcopy__(self, memo)` 深拷贝实现，调用`copy.deepcopy()`时使用。

- 异步
`__aiter__(self)` 返回异步迭代器。
`__anext__(self)` 返回异步迭代器的下一个值。
`__aenter__(self)` 异步上下文管理器的进入方法。
`__aexit__(self, exc_type, exc_val, exc_tb)`异步上下文管理器的退出方法。
`__await__(self)` 返回迭代器，用于await表达式。

- **总结**

1. 魔法方法名称以双下划线开头和结尾。
2. 大多数方法都有特定的调用时机。
3. 实现运算符重载时，应保持数学语义。
4. 避免在`__getattribute__`中访问实例属性，否则会无限递归  。

### OOP（面向对象编程）

#### 封装

- 隐藏内部实现，通过方法访问数据。
- **访问限制**：属性名前加双下划线 `__name` 变成私有属性。
- 如果外部代码通过 `get_xxx()` 和 `set_xxx()` 方法安全访问和修改。

```python
class Student(object):
    ...
    def get_name(self):
        return self.__name
```

#### 继承

- 子类获得父类的全部功能，在代码运行的时候，总是会调用子类。

- 单继承： `class 子类名（超类名）：`
任何类都直接或间接的继承自object类，object类是一切类的超类。

- 多继承： `class 子类名（超类名1，超类名2，…）:`
当多个父类中拥有相同属性时，子类中使用时按照“广度优先”顺序搜索。

- 相关函数/属性：
`__base__属性`：用来记录此类的基类（类实例）。
`__mro__`属性：方法解析顺序。
`super(type,obj)`： 返回绑定的超类的实例，要求obj必须为type类型的实例。
`issubclass(子类, 父类)`判断继承关系。

#### 多态

- **定义**：父类变量可以指向子类对象，调用方法时执行子类的覆盖版本。

- 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。

- 调用方只需知道父类类型，无需关心具体子类；新增子类不影响已有代码。

- 对扩展开放，对修改封闭。

- **覆盖/重写 overwrite**：子类定义与父类同名的方法，调用时优先使用子类方法。

---

## 文本处理

### re正则表达式

**定义**：用于匹配、查找、替换文本。通过定义一种模式来描述要查找的文本。

**应用**：验证格式、提取信息、批量替换。

### 元字符：具有特殊含义的字符

**位置匹配**：

- `.` 匹配任意单个字符（除换行符） 如：`r.t` 匹配 `rat`，`rot` 等。
- `$` 匹配字符串结尾 如：`boy$` 匹配以 boy 为行尾的字符串。
- `^` 匹配字符串开头 如：`^boy` 匹配以 boy 为首行的字符串。
- `\b` 匹配单词边界 如：`er\b` 可匹配 "never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
- `\B` 匹配非单词边界。

**字符集合**：

- `[ ]` 匹配括号中的任何一个字符 如：`r[aou]t` 匹配 `rat`, `rot`, `rut`。
- `[^]` 匹配不在括号内的任意字符 如：`[\^269A-C]` 匹配除 2,6,9,A,B,C 以外的任字符。
- `[c1-c2]` 括号中可使用连字符 `-` 来指定字符的区间 如：`[0-9]` → 任意数字，`[a-zA-Z]` → 任意字母。

**转义字符**：

- `\` 转义特殊字符 如：`\\.` 匹配字符 `.`
- `\w` 匹配字母数字及下划线。
- `\W` 匹配非字母数字非下划线。
- `\s` 匹配任意空白字符，等价于 `[\t\n\r\f]`。
- `\S` 匹配任意非空字符。
- `\d` 匹配任意数字，等价于 `[0-9]`。
- `\D` 匹配任意非数字。
- **小写字母表示"匹配"，大写字母表示"不匹配"。**
- `\1..\9` 匹配第 n 个分组的内容。
- `\10` 匹配第 n 个分组的内容，如果它经匹配；否则指的是八进制字符码的表达式。
- `\<` 和 `\>` 匹配词（word）的开始和结束。如：`<the` 匹配 them，但不匹配 other；`>the` 匹配 breathe，但不匹配 other。

**量词（重复匹配）**：

- `*` 匹配 0 个或多个在它之前的那个字符 如：`r*t` 匹配 t，rt，rrt 等。
- `+` 匹配 1 或多个正好在它之前的那个字符 如：`r+t` 匹配 rt、rrt 等，但不匹配 t。
- `?` 匹配 0 或 1 个在它之前的那个字符 如：`r?t` 只匹配 t 和 rt。
- `{n}` 恰好 n 次，匹配指定数目的字符 如：`A[0-9]{3}` 匹配 "A" 后面跟正好 3 个数字字符串。
- `{n,}` 至少 n 次。
- `{n,m}` n 到 m 次 如：`[0-9]\{4,6\}` 匹配连续的任意 4、5 或 6 个数字字符。

### 分组与捕获

**分组**：用圆括号把部分正则括起来，将匹配表达式的字符保存到一个临时区域。一个正则表达式中最多可以保存 9 个字符，它们可以用 `\1` 到 `\9` 的符号来引用。如：`%s/99/\1aa/g` 将 99 替换成 99aa。

`(re)`：**捕获分组**，匹配并保存内容，可用 `\1`…`\9` 引用。

`(?:re)`：**非捕获分组**，只匹配不保存。

**命名分组：**
`pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'`
`match = re.search(pattern, text)`

### 贪婪与非贪婪模式

贪婪模式（默认）：尽可能多地匹配    符号：`*`、`+`、`?`、`{n,m}`

非贪婪模式：尽可能少地匹配    符号：`*?`、`+?`、`??`、`{n,m}?`

**贪婪模式**：匹配整个字符串。

**非贪婪模式**：每个`<div>`标签单独匹配，在量词后加`?`变为非贪婪。

```python
import re
# 贪婪模式（默认）
text = "<div>内容1</div><div>内容2</div>"
greedy = re.findall(r'<div>.*</div>', text)
# 匹配：'<div>内容1</div><div>内容2</div>'（整个字符串）

# 非贪婪模式
lazy = re.findall(r'<div>.*?</div>', text)
# 匹配：['<div>内容1</div>', '<div>内容2</div>']
```

### re模块详解

#### 函数

- **re.match(pattern, string, flags=0)**  从字符串**开头**匹配。
pattern 匹配的正则表达式；string 要匹配的字符串；flags 用于控制匹配方式  。
匹配成功返回匹配的对象，否则返回None。

- **re.search(pattern, string, flags=0)**  在整个字符串中**搜索**匹配。
匹配成功返回匹配的对象，否则返回None。

- re.match与re.search的区别:  
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败返回None；
re.search匹配整个字符串，直到找到一个匹配。

- **re.sub(pattern, repl, string, count=0, flags=0)**  替换字符串中的匹配项 。
pattern：正则中的模式字符串；repl：替换的字符串或函数，string：被查找替换的原始字符串；  
count：模式匹配后替换的最大次数，默认0表示替换所有的匹配。  
返回替换后的字符串。

- **re.findall()** 查找所有匹配 返回列表 。

- **re.finditer()** 查找所有匹配（迭代器）返回匹配对象迭代器 。

- **re.split()** 按模式分割字符串 返回列表 。

- **re.compile()** 预编译正则表达式 返回正则表达式对象。

#### 匹配对象的方法

- `group(0)`：整个匹配的字符串

- `group(1)`, `group(2)`：第 1、2 个捕获分组

- `groups()`：返回所有捕获分组组成的元组

#### 正则表达式标志

- re.I 忽略大小写。

- re.L 做本地化识别匹配。

- re.M 多行匹配，影响 ^ 和 $。

- re.S 使 . 匹配包括换行在内的所有字符。

- re.U 根据Unicode字符集解析字符。影响 \w, \W, \b, \B。

- re.A ascii模式，使\w、\W、\b、\B等只匹配ASCII字符。

#### 语法

- `(re)` 捕获分组，匹配括号内的表达式，并将匹配内容保存到编号分组中。
- `(?:re)` 非捕获分组，匹配括号内的表达式，类似 (...)，但不保存匹配内容，不占用分组编号。
- `(?i)` 忽略大小写。
- `(?m)` 多行模式。
- `(?s)` 点匹配所有。
- `(?x)` 详细模式。
- `(?imx: re)` 在括号中使用i, m, 或 x 可选标志。
- `(?-imx: re)` 在括号中不使用i, m, 或 x 可选标志。
- `(?#....)` 注释。
- `(?= re)` 正向前向断言。匹配一个位置，后面必须跟着指定的模式，匹配后，匹配位置不变。
- `(?! re)` 负向先行断言。匹配一个位置，后面不能跟着指定的模式。
- `(?> re)` 匹配的独立模式，一旦匹配不会回溯。。

---

## 代码格式

### 推导式

#### 列表推导式

- 定义：

```python
colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]
combinations = [(color, size) for color in colors for size in sizes]
# [('red', 'S'), ('red', 'M'), ('red', 'L'), ('green', 'S'), ...]
```

- 条件表达式

 跟在for后面的if是一个筛选条件，不能带else；把if写在for前面必须加else

 ```python
 # 在for循环前使用if-else（三元表达式）
numbers = [1, 2, 3, 4, 5, 6]
result = [x if x % 2 == 0 else "奇数" for x in numbers]
# ['奇数', 2, '奇数', 4, '奇数', 6]

# 在for循环后使用if（过滤条件）
result = [x for x in numbers if x % 2 == 0]
# [2, 4, 6]
 ```

#### 嵌套推导式

```python
# 矩阵转置
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 展平二维列表
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### 字典推导式

```python
# 反转字典
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# 过滤字典
scores = {"Alice": 85, "Bob": 60, "Charlie": 90, "David": 75}
passing = {name: score for name, score in scores.items() if score >= 70}
# {'Alice': 85, 'Charlie': 90, 'David': 75}
```

#### 生成器表达式

- 用圆括号 `()`，不立即生成所有值，适合大数据量

```python
# 使用圆括号，惰性求值
gen = (x**2 for x in range(1000000) if x % 2 == 0)
# 不会立即生成所有值，只在需要时计算
first_three = [next(gen) for _ in range(3)]
# [0, 4, 16]
```

### Type Hint（类型注释）

- **基本语法**：变量：`变量: 类型 = 值` ；函数：`def 函数(参数: 类型) -> 返回类型:`

- **从简单开始**：先从公共API开始添加类型注释，然后逐步扩展到内部实现。

- **细化**：从简单类型（`int`, `str`）到复杂类型（`list[int]`, `dict[str, int]`）

- **基本类型注释：**`str`, `int`, `float`, `bool`, `None`

```python
#变量
name: str = "张三"
age: int = 20
is_student: bool = True
height: float = 1.75
```

- **容器类型注释：** `list[int],tuple[int, str],tuple[int, ...],dict[str, int],set[float]`

```python
# 列表
scores_better: list[int] = [90, 85, 88]  # 推荐，指明元素类型

# 元组
point_better: tuple[int, int] = (10, 20)  # 固定长度
person: tuple[str, int, float] = ("张三", 20, 1.75)

# 可变长度元组
values: tuple[int, ...] = (1, 2, 3, 4, 5)  # 任意个整数

# 字典
student_best: dict[str, str | int] = {"name": "张三", "age": 20}  # 最好

# 集合
unique_numbers: set[int] = {1, 2, 3, 4, 5}

#函数类型
from typing import List, Dict, Set, Tuple
def process_students_v2(students: dict[str, int]) -> dict[str, int]:
 return {name: age + 1 for name, age in students.items()}
```

- **函数类型注释**

```python
# 参数类型
def greet(name: str, times: int = 1) -> str:
 return (f"Hello, {name}! " * times).strip()

# 无返回值
def print_hello(name: str) -> None:
 print(f"Hello, {name}")
```

- **可选类型：**（可能为None）`Optional[str]` 或 `str | None`

```python
from typing import Optional

# 表示 name 可能是 str 或 None
def greet(name: Optional[str] = None) -> str:
 if name is None:
  return "Hello, World!"
 return f"Hello, {name}!"
```

- **联合类型：`Union[int, float]` 或 `int | float`**

```python
from typing import Union

# 返回值可能是 int 或 float
def divide(a: float, b: float) -> Union[int, float]:
 result = a / b
 if result.is_integer():
  return int(result)
 return result
```

- **任意类型和任意多个参数：** `Any`

```python
from typing import Any, Callable

# Any 表示任意类型
def process_data(data: Any) -> Any:
 # 这里可以处理任何类型的数据
 return data
 
# 任意多个参数
from typing import Union

def sum_all(*args: int) -> int:
 return sum(args)

def print_info(**kwargs: Union[str, int]) -> None:
 for key, value in kwargs.items():
  print(f"{key}: {value}")
```

- **类型别名：**

```python
from typing import Dict, List, Tuple, Union

# 为复杂的类型定义别名
Student = Dict[str, Union[str, int, List[str]]]
Coordinates = Tuple[float, float]

# 使用类型别名
def process_student(student: Student) -> None:
 print(student)

def get_distance(point1: Coordinates, point2: Coordinates) -> float:
 x1, y1 = point1
 x2, y2 = point2
 return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
```

---


## 进阶技巧

### generator 生成器

**定义**：特殊的迭代器，一边循环一边计算，只在需要时生成值，不一次性存储所有结果

**创建**：

1. **生成器表达式**（圆括号）

`(表达式 for 变量 in 可迭代对象 [if 真值表达式])`

```python
squares = (x**2 for x in range(5))
print(list(squares))  # [0, 1, 4, 9, 16]
```

1. **yield 函数**

在调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

```python
def countdown(n):
"""倒计时的生成器函数"""
 print(f"开始倒计时: {n}")
 while n > 0:
  yield n
  n -= 1
 print("倒计时结束!")
# 使用生成器
for num in countdown(5):
 print(num)
```

**next()方法**

调用generator函数时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值,没有更多元素时，抛出StopIteration的错误，返回值包含在StopIteration的value中。

```python
def fib():
"""斐波那契数列生成器"""
 a, b = 0, 1
 while True:
  yield a
  a, b = b, a + b
  fib = fibonacci()
  print(next(fib))  # 0
 ```
