## **〇、前言**

xml格式作为[netconf配置文件](https://zhida.zhihu.com/search?content_id=199817393&content_type=Article&match_order=1&q=netconf配置文件&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODM2MzQ2MDIsInEiOiJuZXRjb25m6YWN572u5paH5Lu2IiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MTk5ODE3MzkzLCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.3fmg2Ebz6JGy3uUwA4FjjhzcD0gKSm1dcbKBy9KjsLg&zhida_source=entity)的格式，有一定的研究价值，但是xml作为一种标记语言，非常不利于**“[network engineer](https://zhida.zhihu.com/search?content_id=199817393&content_type=Article&match_order=1&q=network+engineer&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODM2MzQ2MDIsInEiOiJuZXR3b3JrIGVuZ2luZWVyIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MTk5ODE3MzkzLCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.qCRR_cTrLZRtJjfmOpiDaj1FDqWRAoqJqwjbblxVyGs&zhida_source=entity)”**识别。解析xml文件是一件很烦的事情。Python内置的API：**xml.etree.ElementTree** 可以解决这个问题。但是其语法和特性非常麻烦。详见官网文档：

[xml.etree.ElementTree - The ElementTree XML API - Python 3.10.4 documentationdocs.python.org/3/library/xml.etree.elementtree.html](https://link.zhihu.com/?target=https%3A//docs.python.org/3/library/xml.etree.elementtree.html)

xml是一种固有的分层数据格式，最自然的表示方式是解析成树状。 ElementTree将整个 xml 文档解析成树状结构， Element就表示这个树状结构中的单节点。

整个xml文档与Python交互（读取和写入文件）是在ElementTree（相当于整棵树）上完成。单个 xml 元素及其子元素的交互是在Element（相当于leaf）上完成。

[![img](https://pic1.zhimg.com/v2-f3a5624bfc841f37742566e5c0223348.jpg?source=7e7ef6e2&needBackground=1)浅谈xmltodict模块15 赞同 · 4 评论 ](https://zhuanlan.zhihu.com/p/501918775)文章

### **1、ElementTree的xml形态**

```xml
<?xml version="1.0" encoding="utf-8"?>
<dev_info id="netmiko_inventory">
   <R1 type="cisco">
       <device_type>cisco_ios</device_type>
       <username>admin</username>
       <password>cisco</password>
       <ip>192.168.47.10</ip>
   </R1>
   <SW3 type="huawei">
       <device_type>huawei_vrpv8</device_type>
       <username>admin</username>
       <password>huawei</password>
       <ip>192.168.47.30</ip>
   </SW3>
</dev_info>
```

### **2、单个Element的xml形态**

```xml
<device_type desc="platform">cisco_ios</device_type>
```

## **一、Element常用属性和XML对应**

Element常用属性对应的xml格式

```xml
<tag attrib=“netmiko_inventory”>text</tag>
```

例：

```xml
<device_type desc="platform">cisco_ios</device_type>
    tag       attrib         text       tag
```

### **1、tag**

tag是str对象，表示xml标签，例子中的前后闭合的device_type

### **2、attrib**

attrib是一个dict对象，表示xml属性，例子中的desc="platform"

### **3、text**

text就是xml数据标签包裹的内容，也是Element的内容，例子中的 cisco_ios

### **4、child elements**

child elements则是xml一对标签中包含的子集，如下图，类似于R1和SW3标签中包裹的内容

```xml
<?xml version="1.0" encoding="utf-8"?>
<dev_info id="netmiko_inventory">
   <R1 type="cisco">
       <device_type>cisco_ios</device_type>
       <username>admin</username>
       <password>cisco</password>
       <ip>192.168.47.10</ip>
   </R1>
   <SW3 type="huawei">
       <device_type>huawei_vrpv8</device_type>
       <username>admin</username>
       <password>huawei</password>
       <ip>192.168.47.30</ip>
   </SW3>
</dev_info>
```

## **二、ElementTree**

ElementTree可以把整个xml文件解析成树形结构。

xml文件：

```xml
<?xml version="1.0" encoding="utf-8"?>
<dev_info id="netmiko_inventory">
   <R1 type="cisco">
       <device_type>cisco_ios</device_type>
       <username>admin</username>
       <password>cisco</password>
       <ip>192.168.47.10</ip>
   </R1>
   <SW3 type="huawei">
       <device_type>huawei_vrpv8</device_type>
       <username>admin</username>
       <password>huawei</password>
       <ip>192.168.47.30</ip>
   </SW3>
</dev_info>
```

### **1、Python的ElementTree解析：**

使用ElementTree能快速的把xml文件解析成ElementTree

```python
from xml.etree import ElementTree as ET

# 直接读取xml文件，形成ElementTree结构
tree = ET.parse('lab1.xml')
root = tree.getroot() # 获取root tag

print(root.tag) # 打印root的tag
print(root.attrib) # 打印root的attrib
# 使用root索引访问标签的值，[0]是R1标签，[0]是R1标签中的第一个标签device_type, .text是取这个标签的值，自然值就是cisco_ios
print(root[0][0].text)
print('\n')

for child in root: # 打印root的child层的tag和attrib
   print(child.tag, child.attrib)
```

解析结果

```bash
username@usernamedeMacBookPro1 xmlLab %python -u"/Users/username/Coding/Test/xmlLab/xml_lab1.py"
dev_info # 注意，标签tag的数据结构是str
{'id': 'netmiko_inventory'} # 注意，属性attrib的数据结构是dict
cisco_ios

R1 {'type': 'cisco'} # 由此可见，遍历出来的tag是str，attrib是dict
SW3 {'type': 'huawei'}
username@usernamedeMacBookPro1 xmlLab %
```

### **2、Element之查找**

Element有很丰富的查找方法，总结如下：

```text
iter(tag=None) 遍历Element的child，可以指定tag精确查找
findall(match) 查找当前元素tag或path能匹配的child节点
find(match) 查找当前元素tag或path能匹配的第一个child节点
get(key, default=None) 获取元素指定key对应的attrib，如果没有attrib，返回default。
```

**（1）iter**

Element使用iter迭代器可以递归地遍历它下面的所有child

```python
>>> from xml.etree import ElementTree as ET
>>> tree = ET.parse('lab1.xml')
>>> root = tree.getroot()
>>> 
>>> for dev in root.iter('username'):
...     print(dev.tag)
... 
username
username
>>> 
>>> for dev in root.iter('username'):
...     print(dev.text)
... 
admin
admin
>>> 
>>> for dev in root.iter('password'):
...     print(dev.text)
... 
cisco
huawei
>>> 
>>> for dev in root.iter('R1'):
...     print(dev.attrib)
... 
{'type': 'cisco'}
>>> 
>>> for dev in root.iter('SW3'):
...     print(dev.attrib)
... 
{'type': 'huawei'}
>>>  
>>> for dev in root.iter():
...     print(dev.attrib)
... 
{'id': 'netmiko_inventory'}
{'type': 'cisco'}
{}
{}
{}
{}
{'type': 'huawei'}
{}
{}
{}
{}
>>> for dev in root.iter():
...     print(dev.tag)
... 
dev_info
R1
device_type
username
password
ip
SW3
device_type
username
password
ip
>>> 
>>> for dev in root.iter():
...     print(dev.text)
... 

   

       
cisco_ios
admin
cisco
192.168.47.10

       
huawei_vrpv8
admin
huawei
192.168.47.30
>>>
```

**（2）findall、find**

Element使用finall可以查找当前元素tag或path能匹配的child节点

```python
>>> from xml.etree import ElementTree as ET
>>> tree = ET.parse('lab1.xml')
>>> root = tree.getroot()
>>>
>>> for user_passwd in root.findall('R1'):
...     cisco_user = user_passwd.find('username').text
...     cisco_passwd = user_passwd.find('password').text
...     print(f'cisco user: {cisco_user} password: {cisco_passwd}')
... 
cisco user: admin password: cisco
>>>
```

**ElementTree的查找非常方便，可以加以利用，个人强烈不建议使用ElementTree去修改xml文件**

## **三、Element修改**

ElementTree可以使用很多方法来修改xml文件，确认修改完毕后，可以使用ElementTree.write()方法写入

**不建议网工使用该功能**

### **1、修改方法**

```text
Element.text 直接修改字段
Element.remove() 删除字段
Element.set() 添加或修改属性attrib
with Element.append() 添加新的child
```

### **2、修改示例**

把R1的ip地址由192.168.47.10修改成192.168.47.1

修改前的xml文件

```xml
<?xml version="1.0" encoding="utf-8"?>
<dev_info id="netmiko_inventory">
   <R1 type="cisco">
       <device_type>cisco_ios</device_type>
       <username>admin</username>
       <password>cisco</password>
       <ip>192.168.47.10</ip>
   </R1>
   <SW3 type="huawei">
       <device_type>huawei_vrpv8</device_type>
       <username>admin</username>
       <password>huawei</password>
       <ip>192.168.47.30</ip>
   </SW3>
</dev_info>
```

修改代码

```python
>>> from xml.etree import ElementTree as ET
>>> tree = ET.parse('lab1.xml')
>>> root = tree.getroot()
>>>
>>> for dev in root.iter('R1'):
...     dev.find('ip').text = str('192.168.47.1')
... 
>>> tree.write('./lab1.xml')
```

修改后的xml：

```xml
<dev_info id="netmiko_inventory">
   <R1 type="cisco">
       <device_type>cisco_ios</device_type>
       <username>admin</username>
       <password>cisco</password>
       <ip>192.168.47.1</ip> # 注意看修改后的地址
   </R1>
   <SW3 type="huawei">
       <device_type>huawei_vrpv8</device_type>
       <username>admin</username>
       <password>huawei</password>
       <ip>192.168.47.30</ip>
   </SW3>
</dev_info>
```

### **3、删除示例**

删除SW3的标签部分

```xml
<dev_info id="netmiko_inventory">
   <R1 type="cisco">
       <device_type>cisco_ios</device_type>
       <username>admin</username>
       <password>cisco</password>
       <ip>192.168.47.1</ip>
   </R1>
   <SW3 type="huawei">
       <device_type>huawei_vrpv8</device_type>
       <username>admin</username>
       <password>huawei</password>
       <ip>192.168.47.30</ip>
   </SW3>
</dev_info>
```

修改代码

```python
>>> for dev in root.findall('SW3'):
...     root.remove(dev)
... 
>>> tree.write('./lab1.xml')
```

修改后的xml：

```xml
<dev_info id="netmiko_inventory">
   <R1 type="cisco">
       <device_type>cisco_ios</device_type>
       <username>admin</username>
       <password>cisco</password>
       <ip>192.168.47.1</ip>
   </R1>
</dev_info>
```

## **四、后记**

**xml.etree.ElementTree提供的解析方法，适合网络工程师用来解析、查找xml元素，但其复杂的特性制约了修改和构建，因为网工毕竟不是“专业代码玩家”使用起来非常容易出错。个人不推荐使用它来修改、构建xml文件**