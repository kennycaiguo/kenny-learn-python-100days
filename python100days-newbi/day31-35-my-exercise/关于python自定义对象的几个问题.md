# 1.python自定义的对象能不能使用运算符做运算？

可以。Python 允许通过**运算符重载**，让自定义的对象支持算术运算、比较运算等。你只需要在自定义类中实现相应的**特殊方法（魔法方法）**即可。 [[1](https://blog.csdn.net/weixin_44705554/article/details/145534410), [2](https://cloud.tencent.com/developer/article/1753849), [3](https://www.cnblogs.com/Micro0623/p/11813448.html)]

以下是几种最常用的运算符及其对应的特殊方法：

1. 算术运算符

当对象使用算术符号时，Python 会自动调用对象内部对应的特殊方法：

| 运算符 [[1](https://edu.51cto.com/video/43434.html)] | 对应特殊方法               | 说明 |
| ---------------------------------------------------- | -------------------------- | ---- |
| `+`                                                  | `__add__(self, other)`     | 加法 |
| `-`                                                  | `__sub__(self, other)`     | 减法 |
| `*`                                                  | `__mul__(self, other)`     | 乘法 |
| `/`                                                  | `__truediv__(self, other)` | 除法 |

**代码示例**： [[1](https://blog.csdn.net/weixin_30838923/article/details/113507501)]

python

```
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        # 定义 + 运算符的行为
        return Vector(self.x + other.x, self.y + other.y)
        
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # 输出: Vector(4, 6)
```

 

2. 比较运算符

如果想让自定义对象进行大小或相等比较，需要实现以下方法： [[1](https://blog.csdn.net/weixin_47267103/article/details/145451818)]

| 运算符 | 对应特殊方法          | 说明     |
| ------ | --------------------- | -------- |
| `==`   | `__eq__(self, other)` | 等于     |
| `<`    | `__lt__(self, other)` | 小于     |
| `>`    | `__gt__(self, other)` | 大于     |
| `<=`   | `__le__(self, other)` | 小于等于 |

3. 原地（In-place）与反射（Reflected）运算

- **原地运算**：如 `+=`、`-=`，对应的特殊方法为 `__iadd__`、`__isub__` 等。
- **反射运算**：如果常量在运算符左侧（例如 `3 + obj`），且对象位于右侧，则需要实现以 `r` 开头的方法（如 `__radd__`）。

# 2.python自定义的对象能不能放到`set`中？能去重吗？

**可以，但需要满足特定条件**。默认情况下，自定义对象是不允许放入 `set` 中的，也无法去重。要让自定义对象支持 `set` 并成功去重，必须在类中同时实现 `__hash__` 和 `__eq__` 这两个魔法方法。 [[1](https://www.cnblogs.com/zengzzzzz/p/14661675.html), [2](https://www.reddit.com/r/Python/comments/1k5c8dk/would_a_set_class_that_can_hold_mutable_objects/?tl=zh-hans)]

为什么需要这两个方法？

`set` 依靠哈希表实现去重和快速查找： [[1](https://blog.csdn.net/m0_56738500/article/details/126743252)]

1. **`__hash__`**：提供对象的“指纹”。当对象放入 `set` 时，会调用该方法计算哈希值。如果两个对象的哈希值不同，`set` 就认为它们是不同的对象。
2. **`__eq__`**：判断“相等性”。只有当两个对象的哈希值相同时，`set` 才会调用 `__eq__` 进一步确认它们是否真的内容相同。若返回 `True`，则判定为重复。 [[1](https://www.cnblogs.com/zengzzzzz/p/14661675.html)]

示例代码

以下是如何通过重写这两个方法，让包含相同属性的自定义对象被正确去重的标准写法：

python

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        """当对象的属性相同时，判定为相等"""
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __hash__(self):
        """根据对象的属性生成哈希值"""
        return hash((self.name, self.age))
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"

# 测试去重
p1 = Person("张三", 20)
p2 = Person("张三", 20)
p3 = Person("李四", 25)

unique_set = {p1, p2, p3}
print(unique_set) 
# 输出结果: {Person(张三, 20), Person(李四, 25)} (成功去重，p1 和 p2 被视为同一个对象)
```



核心注意事项

- **属性与哈希的一致性**：用于计算哈希值的属性（在 `__hash__` 中使用的属性）必须是**不可变的**（如字符串、数字、元组）。
- **对象状态改变**：如果把对象放入 `set` 后修改了它的属性，其哈希值会改变，这会导致 `set` 内部结构混乱，甚至引发内存错误。因此，通常建议这类自定义对象在创建后属性保持只读。 [[1](https://www.cnblogs.com/Neeo/articles/11212390.html), [2](https://www.reddit.com/r/Python/comments/1k5c8dk/would_a_set_class_that_can_hold_mutable_objects/?tl=zh-hans)]

# 3.python自定义的对象能不能作为`dict`的键？

**可以。** Python 自定义的对象完全可以作为 `dict` 的键，但前提是该对象必须是**可哈希的（Hashable）**。 [[1](https://www.volcengine.com/article/776638), [2](https://blog.csdn.net/qq_43019433/article/details/125312326)]

要让自定义对象能够作为字典的键，你需要满足以下两个条件并正确实现相应的方法： [[1](https://blog.csdn.net/woshiaotian/article/details/20286149)]

1. **实现 `__hash__()` 方法**：该方法必须返回一个整数，用于在字典的哈希表中快速定位键。
2. **实现 `__eq__()` 方法**：用于判断两个对象是否“相等”，以此来解决哈希冲突。 [[1](https://blog.csdn.net/woshiaotian/article/details/20286149), [2](https://blog.csdn.net/qq_43019433/article/details/125312326)]

默认行为

如果你**什么都不做**：

- 默认情况下，Python 自定义类的实例是可哈希的。
- 它们的哈希值基于对象的**内存地址**。
- 只要两个实例不是同一个对象（内存地址不同），即使它们的内部属性完全一样，Python 也会把它们当作完全不同的键。 [[1](https://zhuanlan.zhihu.com/p/1535483250)]

自定义键相等的规则

如果你希望“属性相同”的两个不同实例被视为字典里的**同一个键**，你需要重写 `__hash__()` 和 `__eq__()`。 [[1](https://blog.csdn.net/woshiaotian/article/details/20286149)]

**代码示例：**

python

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        """当两个点的 x 和 y 坐标相同时，判定为同一个键"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
        
    def __hash__(self):
        """基于坐标生成哈希值"""
        return hash((self.x, self.y))

# 测试使用
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

my_dict = {}
my_dict[p1] = "这是 p1"

# p1 和 p2 属性相同，__eq__ 返回 True，__hash__ 返回值相同
print(my_dict.get(p2))  # 输出: 这是 p1

# p3 是不同的键
print(my_dict.get(p3))  # 输出: None
```

 

⚠️ 核心注意事项：不可变性

作为字典键的对象，其哈希值在其**整个生命周期内绝对不能改变**。 [[1](https://www.volcengine.com/article/776638)]

- 如果你在把对象存入字典后，修改了用于计算哈希值的属性（例如上面例子中的 `x` 和 `y`），那么这个对象在字典中的位置就“找不到了”。

- 因此，通常建议作为 `dict` 键的对象应该是**不可变的**（即尽量不要在初始化后修改它的属性）。

  # 4.python自定义的对象能不能使用上下文语法？

  **可以的**。在 Python 中，自定义对象完全可以使用上下文语法（即 `with` 语句）。 [[1](https://blog.csdn.net/cnds123/article/details/117703436), [2](https://cloud.tencent.com/developer/article/1793869)]

  要让自定义对象支持 `with` 语句，只需要在该类中实现**上下文管理协议**（即实现 `__enter__()` 和 `__exit__()` 两个特殊方法），或者使用 `@contextmanager` 装饰器。 [[1](https://zhuanlan.zhihu.com/p/36554990), [2](https://blog.csdn.net/cnds123/article/details/117703436)]

  以下是两种实现方式的简明示例：

  方式一：使用类方法（魔术方法）

  这是最标准的方式。当进入 `with` 块时，`__enter__` 会被触发；当离开 `with` 块时，`__exit__` 会被触发（即使发生异常也会被执行）。 [[1](https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p03_make_objects_support_context_management_protocol.html), [2](https://zhuanlan.zhihu.com/p/36554990)]

  python

  ```
  class Resource:
      def __enter__(self):
          print("准备阶段：获取资源或打开连接")
          return self  # 返回的对象会赋值给 as 关键字后的变量
  
      def __exit__(self, exc_type, exc_val, exc_tb):
          print("清理阶段：释放资源或关闭连接")
          # 返回 False（或不返回）会让 with 块内的异常正常向上抛出
          # 返回 True 则会吞掉 with 块内的异常
  
  # 使用上下文语法
  with Resource() as res:
      print("执行阶段：正在使用资源")
  ```

    

  方式二：使用 `contextlib` 模块（生成器方式）

  如果你不想定义一个完整的类，可以使用 Python 标准库提供的 `contextlib`，代码会更加简洁直观。 [[1](https://blog.csdn.net/cnds123/article/details/117703436)]

  python

  ```
  from contextlib import contextmanager
  
  @contextmanager
  def my_resource():
      print("准备阶段：获取资源")
      try:
          yield "返回的资源对象"  # yield 之前的代码对应 __enter__
      finally:
          print("清理阶段：释放资源")  # yield 之后的代码对应 __exit__
  
  # 使用上下文语法
  with my_resource() as res:
      print(f"执行阶段：正在使用 {res}")
  ```

    

  这种语法在管理文件流、数据库连接、多线程锁（Lock）或网络连接时非常有用，能确保资源在操作完成后被安全释放，即便报错也不例外。

# 参考文档

### Python上下文管理器实践指南：自定义和内置用法： https://zhuanlan.zhihu.com/p/661778674