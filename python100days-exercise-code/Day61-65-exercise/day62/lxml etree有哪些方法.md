`lxml.etree` 是 Python 中处理 XML 和 HTML 最强大的库之一。它的核心方法可以分为**解析**、**查找**、**节点操作**和**输出**四大类，能帮你快速提取和修改网页或文件数据。 [[1](https://blog.csdn.net/weixin_51407397/article/details/130390928), [2](https://comate.baidu.com/zh/page/wmbxteyik8h)]

以下是核心方法的详细分类与介绍：

1. 解析与构建方法

这些方法用来把字符串或文件变成可以操作的“树”。 [[1](https://www.itheima.com/news/20210621/134110.html), [2](https://www.cnblogs.com/forlive/p/16373662.html)]

- `etree.HTML()`: 解析 HTML 字符串。如果代码不完整，它会自动补全。
- `etree.XML()`: 解析严格的 XML 字符串。
- `etree.parse()`: 读取本地文件进行解析。
- `etree.Element()`: 手动创建一个新的 XML 节点。
- `etree.SubElement()`: 给父节点添加子节点。 [[1](https://imonce.github.io/2019/10/21/3小时精通lxml-etree-Python中xml的读取、解析、生成和查找/), [2](https://developer.aliyun.com/article/1148376), [3](https://www.cnblogs.com/my_captain/p/7490292.html), [4](https://blog.csdn.net/weixin_51407397/article/details/130390928), [5](https://www.cnblogs.com/forlive/p/16373662.html)]
- 查找数据方法 (XPath)

这是 `etree` 最强大的地方，通过路径规则快速抓取内容。 [[1](https://cloud.tencent.com/developer/article/2216555), [2](https://blog.csdn.net/weixin_51407397/article/details/130390928)]

- `.xpath()`: 使用 XPath 语法查找所有匹配的节点。返回的是一个列表。
- `.find()`: 查找第一个符合条件的节点。
- `.findall()`: 查找所有符合条件的子节点。 [[1](https://cloud.tencent.com/developer/article/2216555)]
- 节点操作方法

当你抓取到节点后，可以用这些方法获取里面的文字或属性。 [[1](https://comate.baidu.com/zh/page/wmbxteyik8h)]

- `.text`: 获取节点的文本内容。
- `.get()`: 获取节点的属性值（如 `.get('href')`）。
- `.set()`: 修改或添加节点的属性（如 `.set('class', 'box')`）。
- `.append()`: 向节点添加子节点。
- `.remove()`: 删除指定的子节点。
- `.getparent()`: 获取当前节点的父节点。
- `.clear()`: 清空节点内的所有子节点和属性。 [[1](https://zhuanlan.zhihu.com/p/718442318)]
- 输出方法

这些方法用来把处理好的树结构变回字符串。 [[1](https://comate.baidu.com/zh/page/wmbxteyik8h)]

- `etree.tostring()`: 将节点或树转换为字节串。可以设置 `encoding='utf-8'` 和 `method='html'` 或 `xml`。

**比喻说明：**
你可以把 `etree` 解析出的节点想象成一个文件夹：

- `.text` 是文件夹里的文件内容。
- `.get()` 是查看文件夹的标签信息（属性）。
- `.xpath()` 就像电脑的全局搜索，能瞬间找出所有符合名字的子文件。 [[1](https://cloud.tencent.com/developer/article/2216555)]

详细使用教程和案例，可以参考 **[\**\*\*![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACCUlEQVR4AXyS3WuOYRzHP/cVWUleduQlDyWFI2kZG+MvIElGDOcSSTuRiYgs5YSkZZLVSomEpRwIh2gOSOzk8bra1tbWnr3c176/a9e93XtpdX+f3/V7+X5/3+vqcZz3ngbvuSRcEa4JN4Sbwi3htk+5o3hXaBKahYdCi9DqvWMEZsVorA+RhH4a82nzkwJGyJAfytfsnOKxGOEmkowUGzPq1rfesByNSiTmLthTssSaigznrFotg/UmkSR21qyzTSvK4HM9HN0IW5bC4fU6C/vXwIG18KUO2o8o1sLHg9BxSDMFLZK4Mwc1q6DxOZyshPKFcG4H/BuA+ip48lWETtjWBIXFUPkAXv6Ex98lIBdOt+Gdhor/YaAEf39Dn8ivvsHgEKQauvpGxHIR9C2S7Q8/wGu7uQ8CVRugtho6++FEjaa8IGKiuGu5epthzyZYMA8adkPFarhcAU4iTm9Kyydoa4fuPrj4FMrmQ0FXsfi6Q1d7BmdeQEmE023KhbNvIZUbp12s08Md3wmnRG7WQxV7oPWYHu2PuiKZ1eplOsuRlzPL7e0sBoFiF2xv1Bvozvvuw957sPU61D0SyQjC+1+w8oL+tNpqxCCgehAYTDQYP9XGT9oWBqODkhq9RlYM9RiDwDhjll8TsUGDCWXRhGI+t0CmacMZTCSHqQK20UjTo9VMwIgWcxgDAAD////voSoAAAAGSURBVAMAFRcClA2YTOkAAAAASUVORK5CYII=)\*\**\*⁠lxml官方入门教程（The lxml.etree Tutorial）翻译 - 知乎专栏](https://zhuanlan.zhihu.com/p/718442318)** 或 **[\**\*\*![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABLElEQVR4AcySPU7DQBCFv104QCq6VFCko0wuwB0oaQmRkj6Nm0gpHYmYK3AHGkpSpqMACYkmouIAoOWNs17bqSLS5EnPOz9vRp7Z9RyII2gQRvTCkBcxJN7xGSZ0iDA7WGxIrbGaET3PL4/S9UUIvOtc4LhyOd9ElLZichdRI5M+qvUSX5onztwDF65g4u55ZQcWK3PSKDUTsVpPhTMy9kVDmxq4jJ+qXrvIxecd5lW+qU0NqmQ8N/q9jxZhE3OtIzUIGadVRrPO3ZKbFgvmRDS1qQFf7L+DhtbrWtZsMQ23vGnu3N7GNlR/LVbmpFF0Ktq1rz0nXMtZiWjmc2BM4ClM6BBR2orJHUeNTFZW6+P9DjS3S1zSdTmth6R9dFO+wLQDq613wP9wcIM/AAAA//9fRA71AAAABklEQVQDAAZVeiFgx1nLAAAAAElFTkSuQmCC)\*\**\*⁠lxml模块常用方法整理总结](https://developer.aliyun.com/article/1148376)** 了解更多细节