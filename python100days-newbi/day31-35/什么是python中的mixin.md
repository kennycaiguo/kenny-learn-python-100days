**Mixin（混入）**是**一种设计模式，通过多重继承将特定功能“混入”到子类中**。它旨在提供单一的、可复用的功能单元，本身不作为独立的类实例化，能有效避免因单一继承导致的类爆炸和代码冗余。 [[1](https://zhuanlan.zhihu.com/p/95857866), [2](https://cloud.tencent.com/developer/article/1550768), [3](https://www.cnblogs.com/gccbuaa/p/19227112)]

Mixin 的核心特征

- **功能单一**：每个 Mixin 类只负责做一件事（如增加日志功能、转换为 JSON 等）。
- **不能单独使用**：它依赖于主类，通常不包含 `__init__` 初始化方法。
- **多重继承**：通过 Python 的多重继承机制，将多个 Mixin 的特性组合到一个类中。 [[1](https://zhuanlan.zhihu.com/p/95857866), [2](https://cloud.tencent.com/developer/article/1550768), [3](https://www.cnblogs.com/gccbuaa/p/19227112)]

简单示例

这里定义了一个将字典转换为 JSON 字符串的 Mixin，并将其“混入”到业务类中：

python

```
import json

# 定义一个 Mixin，提供单一的 JSON 转换功能
class JsonMixin:
    def to_json(self):
        # 依赖于子类的 __dict__ 属性
        return json.dumps(self.__dict__)

# 基础业务类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 多重继承：继承主类和 Mixin 类
class Student(Person, JsonMixin):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

# 使用混入的功能
student = Student("张三", 18, "大一")
print(student.to_json())  # 输出: {"name": "张三", "age": 18, "grade": "\u5927\u4e00"}
```

请谨慎使用此类代码。

使用规范与技巧

- **继承顺序**：在多重继承中，Mixin 类通常放在主类（被混入类）的后面或旁边，确保优先调用主类或按方法解析顺序（MRO）执行。
- **命名约定**：社区通常习惯在 Mixin 类名末尾加上 `Mixin`（如 `JsonMixin`、`LogMixin`），以便于识别和维护。