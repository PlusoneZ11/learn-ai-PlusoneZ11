## 基础容器##
### <font color="#ffc000">列表：list</font>###
**定义**：有序集合，可随时增删元素，元素类型可不同，可嵌套列表
**索引与切片**：
	- **索引**：访问list中每一个位置的元素
		- 从0开始；-1获取最后一个元素
		- 正向索引：0~len(x)-1 , 反向索引：-len(x)~-1
		- 当索引超出了范围时，会报IndexError错误
	- **切片**：等同于字符串索引  
		- 字符串[开始的索引:结束的索引:步长]
		- 切片赋值是改变原列表的排列，不会生成新列表；
		- 对于<u>步长为1</u>的切片赋值，完成的功能是连续替换，等号左右总数可以不等；
		- 对于<u>步长大于1</u>的切片赋值，完成的是逐一替换，故等号左右数要一致；
		- 切片被字符赋值时，字符串会被拆开，字符串长度要和切片长度一致
**运算**：
	+号用于拼接列表，
	\*号用于生成重复的列表，
	比较运算是对对应位置上的元素进行的，需要保持类型一致
**常用属性方法**:
	*增*
		L.append(x)                在列表尾部添加单个元素
		L.extend(list)              向列表追加另一个列表
		L.insert(index,obj)      将obj插到列表中的指定位置index
	*删*
		L.remove(x)      从列表中删除第一次出现在列表中的值 
		L.pop([index])   删除并返回指定位置的元素；若不加索引，默认删除最后元素，同时返回移除元素；会修改原列表
		L.clear()            清空列表，同于L[ : ]=[ ] 
	*查*
		list.index(element[, start[, end]])    返回（第一个）对应元素的索引，不存在抛出 `ValueError`
		L.count(x)         返回列表中元素的个数
	*排序*
		L.reverse()           列表反转
		L.sort(reverse=False)   将列表的顺序按值的小到大顺序进行排列（升序）reserve=True 降序
		L.copy()            浅拷贝
**列表推导式**：用可迭代对象，依次生成列表内元素
	[表达式 for变量 in可迭代对象 ]
	[表达式 for变量 in可迭代对象 if条件表达式]
### <font color="#ffc000">字典：dict</font>###
**定义**：以键-值（key-value）存储的集合，可以存储任意类型，存储是无序的
	键必须是不可变对象，键不能重复
	一个key只能对应一个value，多次对一个key放入value，后面的值会把前面的值冲掉
**创建与访问**：
- 创建
	空字典：d={ }           
	d =  dict(name="Bob", age=30)
	d = {“name”:”xiaoming”,”age”:35}
- 访问
	- value = d["name"]  # xiaoming
	- value = d.get("gender", "unknown")   # 不存在时返回默认值
**生成函数**：
	dict()创建空字典                         d1=dict()
	dict(iterable)用可迭代对象创建    d1=dict([(‘name’,’amy’),(‘age’,15)])
	dict(\*\*kwargs)关键字参数创建   d1=dict(name=’amy’,age=17)
**核心方法**：
	增删改查
		D["d"] = value          添加/修改键值对
		D.clear()                   清空字典	
		D.pop(key)               移除键，同时返回键对应的值    
		del D[键]                   删除键
		D.copy()                    返回字典D的副本		
		D.update(D2)            将字典D2合并到D中，若键相同则取代
		D.get(key.default)     返回键key对应的值，没有则返回default或None
	视图
		D.keys()                     返回可迭代的dict_keys集合对象
		D.values()                  返回可迭代的dict_values集合对象
		D.items()                   返回可迭代的dict_items集合对象
	遍历：                               for k,v in d.items ():
	通过in判断key是否存在返回True/False			'Thomas' in d
**字典推导式**：
	{键表达式 : 值表达式 for 变量 in 可迭代对象(if 条件表达式) }
## 函数##
### <font color="#d99694">匿名函数（lambda）</font>###
 **特点**：简洁，无需函数名，创建后即用
 **语法**：**lambda[参数1，参数2，…]：表达式**		
	  [ ]内的部分可省略。
	  创建一个匿名函数对象，同def类似但不提供函数名
 不必担心函数名冲突，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
### <font color="#d99694">装饰器</font>###
**定义**：接受函数为参数，返回新函数的闭包函数，在代码运行期间动态增加功能
**语法**：**def 装饰器函数名（参数）:**
		**函数块**
	   **return 函数**
	- 用@语法把decorator置于函数的定义处：**@装饰器**  
	- 在被装饰函数定义完成后立即执行
	- 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
**基本结构**：
```python
def metric(text):
	def decorator(func):
	    def wrapper(*args, **kwargs):
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
  三层结构：
	最外层 metric(text)：接受一个参数（比如要显示的文字）
	中间层 decorator(func)：接受要被装饰的函数
	最内层 wrapper：实际执行函数的地方
## 面向对象##
### <font color="#92d050">Class（类）</font>
#### 定义
类是创建对象的模板，定义了一组属性和方法。
对象是类的实例，具有具体的属性值。
#### 创建和访问
**创建**:
	**class关键字+类名**(通常是大写开头)**+(object)**(表示该类是从哪个类继承下来的，如果没有合适的继承类，就使用object类)
	**`__init__`方法**：可以在创建实例时把必须绑定的属性强制填写进去。
		第一个参数永远是`self`，表示创建的实例本身。
		不能传入空的参数，需要传入与`__init__`方法匹配的参数
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
**实例**
	创建 ：类名+()      
	调用：实例.变量名        
	模块中调用：模块名.实例.变量名
**实例属性和类属性**
	**对象的属性管理**：
		**getattr(obj,name[,default]：**
		  从一个对象得到对象的属性，getattr(x,’y’)等同于x.y
		  当属性不存在时，若给出default参数，则返回default，否则产生AttributeError错误
		**hasattr(obj,name)** 用给定的name返回对象obj是否有此属性，可避免getattr()引发错误
		**setattr(obj,name,value)** 给对象obj的名为name的属性设置相应的值，set(x,’y’,v)等同x.y=v
		**delattr(obj,name)** 删除对象obj的name属性，delattr(x,’y’)等同del x.y
	**实例属性**
		通过实例变量，或者通过self变量
	**类属性**
		在class中定义，归类所有，但类的所有实例都可以访问到。
	实例属性优先级比类属性高，因此它会屏蔽掉类的属性。
	不要对实例属性和类属性使用相同的名字，相同名称的实例属性将屏蔽掉类属性
	删除实例属性后，再使用相同的名称，访问到的将是类属性。
**访问变量的方法**
 - **实例方法**：
	定义在类内的函数，第一个参数为self
	可访问类变量和实例属性，若无return则返回None
	实例.实例方法名（调用参数）
	类名.实例方法名（实例，调用参数）
 - **类方法@classmethod**
	只能访问类变量，第一个参数是类的实例
	 类名.方法名() 或 实例.方法名
 - **静态方法@staticmethod**：
	定义在类的内部，只能凭借该类和实例调用。
	 与普通函数定义相同。
	 不能访问类变量和实例属性，类实例和对象实例可以调用
 - 总结：
	不想访问类变量和实例变量，用静态方法
	只想访问类内变量，不想访问实例属性用类方法
	既想访问类内变量，又想访问实例属性用实例方法
**获取对象信息**
	**type()函数**：判断对象类型：基本类型、指向函数或者类的变量。返回对应的Class类型。
	**isinstance()函数**：判断class的类型是否是该类型本身，或者位于该类型的父继承链上。能用`type()`判断的基本类型也可以用`isinstance()`判断
	**dir()函数**：获得一个对象的所有属性和方法，返回一个包含字符串的list
	**hasattr(object, name)**：检查对象是否拥有指定属性
	**getattr(object, name[, default])**：获取对象的属性值，若不存在返回默认值default
	**setattr(object, name, value)**：设置对象的属性值（新增或修改）
### <font color="#92d050">Magic Methods（魔法方法）</font>
#### 初始化
`__new__(cls, ...)​ `   创建实例时调用的第一个方法，负责创建并返回实例对象
`__init__(self, ...)`​ 在实例创建后被调用,初始化实例的属性
`__del__(self)`            实例被销毁时调用
#### 字符串表示
`__str__(self)`    返回对象的字符串表示。调用`str()`和`print()`时使用
`__repr__(self)`  返回对象的正式字符串表示。调用`repr()`时使用
`__format__(self, format_spec)`  控制对象的格式化输出。调用`format()`时使用
`__bytes__(self)` 返回对象的字节表示。调用`bytes()`时使用。
#### 比较
`__eq__(self, other)`  相等比较，对应 ==
`__ne__(self, other)`  不等比较，对应`!=`
`__lt__(self, other)`  小于比较，对应`<`
`__gt__(self, other)`  大于比较，对应`>`
`__le__(self, other)`   小于等于比较，对应`<=`
`__ge__(self, other)`  大于等于比较，对应`>=`
#### 算术运算
`__add__(self, other)`  加法
`__sub__(self, other)`  减法
`__mul__(self, other)`  乘法
`__truediv__(self, other) `       除法
`__floordiv__(self, other)`      整数除法  //
`__mod__(self, other) `             取模        %
`__pow__(self, other)`               幂运算
#### 类型转换
`__int__(self) ` 转换为整数，调用int()时使用。
`__float__(self)`  转换为浮点数，调用float()时使用。
`__complex__(self)`  转换为复数，调用complex()时使用。
`__bool__(self)`  转换为布尔值，调用bool()时使用。
`__index__(self)`   转换为整数索引，用于切片和bin()、hex()、oct()函数。
#### 容器类
`__len__(self) ` 返回容器长度，调用`len()`时使用。
`__getitem__(self, key)` 获取容器中指定元素，对应`self[key]`操作。
`__setitem__(self, key, value)`设置容器中指定元素，对应`self[key] = value`操作。
`__delitem__(self, key)` 删除容器中指定元素，对应`del self[key]`操作。
`__iter__(self)`返回迭代器对象，用于迭代容器。
`__next__(self)` 迭代器的下一个值，调用`next()`时使用。
`__reversed__(self)`​  返回反向迭代器，调用`reversed()`时使用。
`__contains__(self, item)`  成员测试，对应`item in self`操作。
#### 属性访问
`__getattr__(self, name)` 当访问不存在的属性时调用。
`__getattribute__(self, name)` 访问任何属性时都会调用，优先级高于`__getattr__`。
`__setattr__(self, name, value)`设置属性值时调用。
`__delattr__(self, name)` 删除属性时调用。
`__dir__(self)` 返回属性列表，调用`dir()`时使用。
#### 描述符
`__get__(self, instance, owner)` 获取描述符的值。
`__set__(self, instance, value)` 设置描述符的值。
`__delete__(self, instance)` 删除描述符。
#### 哈希
`__hash__(self)`返回对象的哈希值，用于字典键和集合元素。
`__eq__(self, other)`实现对象的相等比较。
注意：`__hash__`和`__eq__`需要一起实现，如果类定义了`__eq__`但没有定义`__hash__`，则实例不可哈希。
#### 复制
`__copy__(self)`浅拷贝实现，调用`copy.copy()`时使用。
`__deepcopy__(self, memo)` 深拷贝实现，调用`copy.deepcopy()`时使用。
#### 类
`__init_subclass__(cls)`子类初始化时调用，用于自定义子类创建。
`__set_name__(self, owner, name)`描述符在所属类创建时调用。
`__class_getitem__(cls, item)` 支持泛型类，对应`Class[item]`操作。
#### 异步
`__aiter__(self)` 返回异步迭代器。
`__anext__(self) 返回异步迭代器的下一个值。
`__aenter__(self)` 异步上下文管理器的进入方法。
`__aexit__(self, exc_type, exc_val, exc_tb) 异步上下文管理器的退出方法。
`__await__(self)` 返回迭代器，用于await表达式。
#### 总结
1. 魔法方法名称以双下划线开头和结尾
2. 大多数方法都有特定的调用时机
3. 实现运算符重载时，应保持数学语义
4. 避免在`__getattribute__`中访问实例属性，否则会无限递归
### <font color="#92d050">OOP（面向对象编程）</font>
#### 封装
##### 访问限制
- **定义**：将数据和操作数据的方法绑定在一起，对外隐藏实现细节
- 要让内部属性不被外部访问，把属性的名称前加上两个下划线`__`
- 如果外部代码要获取name，可以给Student类增加get_name的方法：
```python
class Student(object):
    ...
    def get_name(self):
        return self.__name
```
- 如果要允许外部代码修改score，可以再给Student类增加`set_score`方法：
```python
class Student(object):
    ...
    def set_score(self, score):
        self.__score = score
```
#### 继承###
 - 定义一个class时，可以从某个现有的class继承
	新的class称为子类（Subclass）被继承的class称为基类、父类或超类（Base class、Super class）
	子类获得父类的全部功能，在代码运行的时候，总是会调用子类
 - 单继承： **class 子类名（超类名）**：
	任何类都直接或间接的继承自object类，object类是一切类的超类
	\_\_base__属性   用来记录此类的基类（类实例）
	**super(type,obj)** 返回绑定的超类的实例，要求obj必须为type类型的实例
    用于类的函数：**issubclass(cls,类或类元组)**  判断类是否继承自其他的类，若cls是类(class)或元组中的一个派生子类，则返回True，
 - 多继承： **class 子类名（超类名1，超类名2，…）**：	
	当多个父类中拥有相同属性时，子类中使用时按照“广度优先”顺序搜索
- 相关函数
	`issubclass(cls, 类或类元组)`：判断继承关系
	`super(type, obj)`：返回绑定的超类实
	`__base__`属性：记录此类的基类
	`__mro__`属性：方法解析顺序
#### 多态
 - 在有继承关系的类中，调用基类对象的方法，实际能调用子类的覆盖方法现象
 - 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。
 - 对于一个变量，我们只需要知道它是`Animal`类型，无需确切地知道它的子类型，就可以放心地调用`run()`方法，而具体调用的`run()`方法是作用在`Animal`、`Dog`还是`Cat`对象上，由运行时该对象的确切类型决定
 - 调用方只管调用，不管细节，而当我们新增一种`Animal`的子类时，只要确保`run()`方法编写正确，不用管原来的代码是如何调用的。
	对扩展开放：允许新增`Animal`子类；
	对修改封闭：不需要修改依赖`Animal`类型的`run_twice()`等函数。
 - **覆盖/重写 overwrite**：在有继承关系的类中，子类中实现了与基类同名的方法，在子类实例调用该方法时，实际调用的时子类中的覆盖版本
## 文本处理
### <font color="#7030a0">re正则表达式</font>###
**定义**：一种用于匹配、查找、替换文本的工具。它通过定义一种模式来描述要查找的文本。
**应用**：
	 **验证**：检查字符串是否符合特定格式
	 **提取**：从文本中提取特定信息
	 **替换**：批量修改文本内容
**元字符**:具有特殊的含义的字符
  位置：
	. 匹配任意单个字符（除换行符）					如：r.t 匹配rat，rot等
	$ 匹配字符串结尾						                    如：boy$ 匹配以boy为行尾的字符串
	^ 匹配字符串开头							                如：^boy 匹配以boy为首行的字符串
	\b 匹配单词边界                                           如： 'er\b' 可匹配"never" 中的 'er'，但不能匹                                                                               配 "verb" 中的 'er'。
	\B匹配非单词边界
  字符集合：
	[  ]  匹配括号中的任何一个字符			         	如：r[aou]t 匹配rat,rot,rut
	[^] 匹配不在括号内的任意字符                      如：[\^269A-C]匹配除2,6,9,A,B,C以外的任字符
	[c1-c2]括号中可使用连字符-来指定字符的区间	如：[0-9]→ 任意数字，[a-zA-Z]→ 任意字母
  转义字符：
	\ 转义特殊字符	                                            如：\\.匹配字符.
	\w 匹配字母数字及下划线
	\W 匹配非字母数字非下划线
	\s 匹配任意空白字符，等价于 [\t\n\r\f].
	\S 匹配任意非空字符
	\d 匹配任意数字，等价于 [0-9].
	\D 匹配任意非数字
    -->**小写字母表示"匹配"，大写字母表示"不匹配"**
    \1..\9 匹配第n个分组的内容。
	\10 匹配第n个分组的内容，如果它经匹配；否则指的是八进制字符码的表达式
	\< 和 \> 匹配词（word）的开始和结束	    	如：<the 匹配 them，但不匹配other
										如：>the匹配breathe，但不匹配other 	
  量词（重复匹配）
	 \*匹配0个或多个在它之前的那个字符			    如：r\*t 匹配 t，rt，rrt等 
	+匹配1或多个正好在它之前的那个字符		    如：r+t匹配rt、rrt等，但不匹配t
	? 匹配0或1个在它之前的那个字符			        如：r?t 只匹配 t和rt
	{n} 恰好n次，匹配指定数目的字符                如：A[0-9]{3}匹配"A"后面跟正好3个数字字符串
	{n,} 至少n次
	{n,m} n到m次                                        如：[0-9]\{4,6\} 匹配连续的任意4、5或6个数字字符
**分组与捕获**
	**分组**：用圆括号把部分正则括起来，将匹配表达式的字符保存到一个临时区域
		一个正则表达式中最多可以保存9个字符，
		它们可以用\1到\9的符号来引用。如：%s/99/\1aa/g 将99替换成99aa
	**捕获分组：**
		`text = "2024-01-15"
		`pattern = r'(\d{4})-(\d{2})-(\d{2})'`
		`match = re.search(pattern, text)`
	**命名分组：**
		`pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
		`match = re.search(pattern, text)
**贪婪与非贪婪模式**
	贪婪模式（默认）：尽可能多地匹配    符号：`*`、`+`、`?`、`{n,m}`
	非贪婪模式：          尽可能少地匹配    符号：`*?`、`+?`、`??`、`{n,m}?`
	**贪婪模式：匹配整个字符串**
	**非贪婪模式：每个`<div>`标签单独匹配**
	在量词后加?变为非贪婪
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
#### re模块详解
1. 函数：
	<u>re.match函数</u> 从字符串**开头**匹配
		**re.match(pattern, string, flags=0)**
		pattern 匹配的正则表达式；string 要匹配的字符串；flags 用于控制匹配方式
		匹配成功返回匹配的对象，否则返回None。
	<u>re.search函数 </u>在整个字符串中**搜索**匹配
		**re.search(pattern, string, flags=0)**
		匹配成功返回匹配的对象，否则返回None。
	re.match与re.search的区别:
		re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败,函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
	<u>re.sub函数</u> 用于替换字符串中的匹配项 
		**re.sub(pattern, repl, string, count=0, flags=0)**
		pattern：正则中的模式字符串；repl：替换的字符串，也可为一个函数。
		string：要被查找替换的原始字符串；
		count：模式匹配后替换的最大次数，默认0表示替换所有的匹配。
		返回替换后的字符串
	<u>group(num)或groups()</u>匹配对象函数来获取匹配表达式。
		group(0) 匹配的整个表达式的字符串
		group()可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组
		返回一个包含所有小组字符串的元组，从1到所含的小组号
	<u>re.findall()</u>      查找所有匹配                  返回列表 
	<u>re.finditer()</u>     查找所有匹配（迭代器）返回匹配对象迭代器
	<u>re.split(）</u>        按模式分割字符串          返回列表
	<u>re.compile() </u>    预编译正则表达式         返回正则表达式对象
2. 正则表达式标志：
	re.I   忽略大小写
	re.L   做本地化识别匹配
	re.M  多行匹配，影响 ^ 和 $
	re.S   使 . 匹配包括换行在内的所有字符
	re.U  根据Unicode字符集解析字符。影响 \w, \W, \b, \B。
	re.A  ascll模式，使\w、\W、\b、\B等只匹配ASCII字符
3. 语法：
	(re)​   捕获分组，匹配括号内的表达式，并将匹配内容保存到编号分组中。
	(?:re)​ - 非捕获分组，匹配括号内的表达式，类似 (...), 但不保存匹配内容，不占用分组编号。
	(?i)​ - 忽略大小写
	(?m)​ - 多行模式
	(?s)​ - 点匹配所有
	(?x)​ - 详细模式
	(?imx: re) 在括号中使用i, m, 或 x 可选标志
	(?-imx: re) 在括号中不使用i, m, 或 x 可选标志
	(?#....) 注释
	(?= re) 正向前向断言。匹配一个位置，后面必须跟着指定的模式，匹配后，匹配位置不变
	(?! re) 负向先行断言。匹配一个位置，后面不能跟着指定的模式
	(?> re) 匹配的独立模式，一旦匹配不会回溯。
## 代码格式##
### <font color="#fac08f">列表推导式</font>
**定义**：用**一行代码**生成列表的简洁方法。
	可节省内存，如果推导式超过2行，考虑使用普通循环
**语法结构**：[expression for item in iterable if condition]
**多重循环**
```python
colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]
combinations = [(color, size) for color in colors for size in sizes]
# [('red', 'S'), ('red', 'M'), ('red', 'L'), ('green', 'S'), ...]
```
 **条件表达式**： 跟在for后面的if是一个筛选条件，不能带else；把if写在for前面必须加else
 ```python
 # 在for循环前使用if-else（三元表达式）
numbers = [1, 2, 3, 4, 5, 6]
result = [x if x % 2 == 0 else "奇数" for x in numbers]
# ['奇数', 2, '奇数', 4, '奇数', 6]

# 在for循环后使用if（过滤条件）
result = [x for x in numbers if x % 2 == 0]
# [2, 4, 6]
 ```
**嵌套推导式**
```python
# 矩阵转置
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 展平二维列表
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
**字典推导式**
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
**生成器表达式**
```python
# 使用圆括号，惰性求值
gen = (x**2 for x in range(1000000) if x % 2 == 0)
# 不会立即生成所有值，只在需要时计算
first_three = [next(gen) for _ in range(3)]
# [0, 4, 16]
```
### <font color="#fac08f">Type Hint（类型注释）</font>
**核心要点**：
	1. **基本语法**：`变量: 类型 = 值`  或  `def 函数(参数: 类型) -> 返回类型:`
	2. **从简单开始**：先从公共API（即其他模块会调用的函数、类等）开始添加类型注释，然后逐步扩展到内部实现。
	3. **细化**：从简单类型（`int`, `str`）到复杂类型（`list[int]`, `dict[str, int]`）
**基本类型注释**
```python
#变量
name: str = "张三"
age: int = 20
is_student: bool = True
height: float = 1.75
```
**容器类型注释**
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
**函数类型注释**
```python
# 参数类型
def greet(name: str, times: int = 1) -> str:
	return (f"Hello, {name}! " * times).strip()

# 无返回值
def print_hello(name: str) -> None:
	print(f"Hello, {name}"
```
**可选类型**（可能为None）
```python
from typing import Optional

# 表示 name 可能是 str 或 None
def greet(name: Optional[str] = None) -> str:
	if name is None:
		return "Hello, World!"
	return f"Hello, {name}!"
```
**联合类型**
```python
from typing import Union

# 返回值可能是 int 或 float
def divide(a: float, b: float) -> Union[int, float]:
	result = a / b
	if result.is_integer():
		return int(result)
	return result
```
**任意类型**和**任意多个参数**
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
**类型别名**
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
## 进阶技巧##
### <font color="#00b050">generator 生成器</font>
**定义**：特殊的迭代器，一边循环一边计算的机制，只在需要时生成值，不一次性存储所有结果
**创建**：
	**法一：把一个列表生成式的[]改成()**
	(表达式 for 变量 in 可迭代对象 [if 真值表达式]）
	```
	squares = (x**2 for x in range(5))
	print(list(squares))  # [0, 1, 4, 9, 16]
	```
	法二：**yield关键字**
	在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
	```
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
	调用generator函数时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值,没有更多元素时，抛出StopIteration的错误，返回值包含在StopIteration的value中
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

