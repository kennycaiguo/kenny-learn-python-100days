# 通俗易懂的学会：SQL窗口函数

## **一.窗口函数有什么用？**


在日常工作中，经常会遇到需要**在每组内排名**，比如下面的业务需求：

> 排名问题：每个部门按业绩来排名
> topN问题：找出每个部门排名前N的员工进行奖励
> 复购分析：App内要分析复购用户有多少
> 累计问题：医院要经常统计累计患者数

面对这类需求，就需要使用SQL的高级功能~窗口函数了

![img](https://pic4.zhimg.com/v2-2a22189c177593396e4721e8e89643dd_1440w.jpg)

## **二.什么是窗口函数？**

窗口函数，也叫[OLAP函数](https://zhida.zhihu.com/search?content_id=108719138&content_type=Article&match_order=1&q=OLAP函数&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODIwNzY5NDAsInEiOiJPTEFQ5Ye95pWwIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MTA4NzE5MTM4LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.YGg9RdJza_UeOEKg7m5hVXx_1qTnfXbZ7S9IMB4volo&zhida_source=entity)（Online Anallytical Processing，联机分析处理），可以对数据库数据进行进行复杂分析。

![动图](https://pic4.zhimg.com/v2-7f3941cb3b9bad4dff7fe3a6cf027ea9_b.webp)



窗口函数的基本语法如下：

```mysql
<窗口函数> over (partition by <用于分组的列名>
                order by <用于排序的列名>)
```

那么语法中的<窗口函数>都有哪些呢？

<窗口函数>的位置，可以放以下两种函数：

1） 专用窗口函数，包括后面要讲到的rank, dense_rank, [row_number](https://zhida.zhihu.com/search?content_id=108719138&content_type=Article&match_order=1&q=row_number&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODIwNzY5NDAsInEiOiJyb3dfbnVtYmVyIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MTA4NzE5MTM4LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.d0Vc-KM0zrlao9KmLFgMa-6qTKVBGPE9X1Md08M0qUU&zhida_source=entity)等专用窗口函数。

2） [聚合函数](https://zhida.zhihu.com/search?content_id=108719138&content_type=Article&match_order=1&q=聚合函数&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3ODIwNzY5NDAsInEiOiLogZrlkIjlh73mlbAiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxMDg3MTkxMzgsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.VTvTT-g0bq26EdtYyMBzhM8IfbaLKdeKRooAck9j0qU&zhida_source=entity)，如sum. avg, count, max, min等

因为窗口函数是对where或者group by子句处理后的结果进行操作，所以**窗口函数原则上只能写在select子句中**。



PS：如果不想看文字的，也可以看下面这个我最新的实操视频，实操演示更清楚：

![img](https://pic3.zhimg.com/v2-925ae72ddd53f39eef1deb2a4d3767e4_1440w.jpg)

视频《最通俗易懂的学会SQL窗口函数》

[![img](https://pic1.zhimg.com/v2-c64da0bbe4508837984c9e9b48438d5c_r.jpg?source=172ae18b)SQL从入门到进阶(视频+社群)中科院猴子 的专栏23 篇内容 · 6 赞同 · 8 订阅](https://www.zhihu.com/column/c_1890781095961782061)

## **三.如何使用？**

接下来，就结合实例，给大家介绍几种窗口函数的用法。

### **1.专用窗口函数rank**

例如下图，是班级表中的内容

![img](https://pic4.zhimg.com/v2-f8c3b3deb99122d75bb506fdbea81c8d_1440w.jpg)

如果我们想在每个班级内按成绩排名，得到下面的结果。

![img](https://pic3.zhimg.com/v2-3285d1d648de9f90864000d58847087a_1440w.jpg)

以班级“1”为例，这个班级的成绩“95”排在第1位，这个班级的“83”排在第4位。上面这个结果确实按我们的要求在每个班级内，按成绩排名了。

得到上面结果的sql语句代码如下：

```text
select *,
   rank() over (partition by 班级
                 order by 成绩 desc) as ranking
from 班级表
```

我们来解释下这个sql语句里的select子句。rank是排序的函数。要求是“每个班级内按成绩排名”，这句话可以分为两部分：

1）每个班级内：按班级分组

**partition by用来对表分组**。在这个例子中，所以我们指定了按“班级”分组（partition by 班级）
2）按成绩排名

**order by子句的功能是对分组后的结果进行排序**，默认是按照升序（asc）排列。在本例中（order by 成绩 desc）是按成绩这一列排序，加了desc关键词表示降序排列。

通过下图，我们就可以理解partiition by（分组）和order by（在组内排序）的作用了。

![img](https://pic4.zhimg.com/v2-451c70aa24c68aa7142693fd27c85605_1440w.jpg)

窗口函数具备了我们之前学过的group by子句分组的功能和order by子句排序的功能。那么，为什么还要用窗口函数呢？

这是因为，**group by分组汇总后改变了表的行数，一行只有一个类别。而partiition by和rank函数不会减少原表中的行数**。例如下面统计每个班级的人数。

![img](https://picx.zhimg.com/v2-a9342df7f64ec7d9a52b42adcdb48341_1440w.jpg)

```text
相信通过这个例子，你已经明白了这个窗口函数的使用：

select *,
   rank() over (partition by 班级
                 order by 成绩 desc) as ranking
from 班级表
```

现在我们说回来，为什么叫“窗口”函数呢？这是因为partition by分组后的结果称为“窗口”，这里的窗口不是我们家里的门窗，而是表示“范围”的意思。

**简单来说，窗口函数有以下功能：**

1）同时具有分组和排序的功能

2）不减少原表的行数

3）语法如下：

```text
<窗口函数> over (partition by <用于分组的列名>
                order by <用于排序的列名>)
```



PS：如果不想看文字的，也可以看下面这个我最新的实操视频，实操演示更清楚：

![img](https://pic3.zhimg.com/v2-925ae72ddd53f39eef1deb2a4d3767e4_1440w.jpg)

视频《最通俗易懂的学会SQL窗口函数》

[![img](https://pica.zhimg.com/v2-c64da0bbe4508837984c9e9b48438d5c_r.jpg?source=172ae18b)SQL从入门到进阶(视频+社群)中科院猴子 的专栏23 篇内容 · 6 赞同 · 8 订阅](https://www.zhihu.com/column/c_1890781095961782061)



### **2.其他专业窗口函数**

专用窗口函数rank, dense_rank, row_number有什么区别呢？

它们的区别我举个例子，你们一下就能看懂：



```text
select *,
   rank() over (order by 成绩 desc) as ranking,
   dense_rank() over (order by 成绩 desc) as dese_rank,
   row_number() over (order by 成绩 desc) as row_num
from 班级表
```

得到结果：

![img](https://picx.zhimg.com/v2-ad1d86f5a5b9f0ef684907b20b341099_1440w.jpg)

从上面的结果可以看出：

> rank函数：这个例子中是5位，5位，5位，8位，也就是如果有并列名次的行，会占用下一名次的位置。比如正常排名是1，2，3，4，但是现在前3名是并列的名次，结果是：**1，1，1**，4。
>
> dense_rank函数：这个例子中是5位，5位，5位，6位，也就是如果有并列名次的行，不占用下一名次的位置。比如正常排名是1，2，3，4，但是现在前3名是并列的名次，结果是：**1，1，1**，2。
>
> row_number函数：这个例子中是5位，6位，7位，8位，也就是不考虑并列名次的情况。比如前3名是并列的名次，排名是正常的**1，2，3**，4。
>
> 这三个函数的区别如下：



![img](https://pica.zhimg.com/v2-7b63c571dfa285c0aa0c8f944ca89482_1440w.jpg)

最后，需要强调的一点是：在上述的这三个专用窗口函数中，函数后面的括号不需要任何参数，保持()空着就可以。

现在，大家对窗口函数有一个基本了解了吗？

PS：如果不想看文字的，也可以看下面这个我最新的实操视频，实操演示更清楚：

![img](https://pic3.zhimg.com/v2-925ae72ddd53f39eef1deb2a4d3767e4_1440w.jpg)

视频《最通俗易懂的学会SQL窗口函数》

[![img](https://pica.zhimg.com/v2-c64da0bbe4508837984c9e9b48438d5c_r.jpg?source=172ae18b)SQL从入门到进阶(视频+社群)中科院猴子 的专栏23 篇内容 · 6 赞同 · 8 订阅](https://www.zhihu.com/column/c_1890781095961782061)



### **3.聚合函数作为窗口函数**

聚和窗口函数和上面提到的专用窗口函数用法完全相同，只需要把聚合函数写在窗口函数的位置即可，但是函数后面括号里面不能为空，需要指定聚合的列名。

我们来看一下窗口函数是聚合函数时，会出来什么结果：



```text
select *,
   sum(成绩) over (order by 学号) as current_sum,
   avg(成绩) over (order by 学号) as current_avg,
   count(成绩) over (order by 学号) as current_count,
   max(成绩) over (order by 学号) as current_max,
   min(成绩) over (order by 学号) as current_min
from 班级表
```

得到结果：

![img](https://pic4.zhimg.com/v2-c48f0218306f65049fcf9f98c184226d_1440w.jpg)

有发现什么吗？我单独用sum举个例子：



如上图，聚合函数sum在窗口函数中，是对自身记录、及位于自身记录以上的数据进行求和的结果。比如0004号，在使用sum窗口函数后的结果，是对0001，0002，0003，0004号的成绩求和，若是0005号，则结果是0001号~0005号成绩的求和，以此类推。



不仅是sum求和，平均、计数、最大最小值，也是同理，都是针对自身记录、以及自身记录之上的所有数据进行计算，现在再结合刚才得到的结果（下图），是不是理解起来容易多了？

![img](https://pic4.zhimg.com/v2-c48f0218306f65049fcf9f98c184226d_1440w.jpg)

比如0005号后面的聚合窗口函数结果是：学号0001~0005五人成绩的总和、平均、计数及最大最小值。

如果想要知道所有人成绩的总和、平均等聚合结果，看最后一行即可。

**这样使用窗口函数有什么用呢？**

聚合函数作为窗口函数，可以在每一行的数据里直观的看到，截止到本行数据，统计数据是多少（最大值、最小值等）。同时可以看出每一行数据，对整体统计数据的影响。



## **四.注意事项**

partition子句可是省略，省略就是不指定分组，结果如下，只是按成绩由高到低进行了排序：

```text
select *,
   rank() over (order by 成绩 desc) as ranking
from 班级表
```

得到结果：

![img](https://pica.zhimg.com/v2-c589fe21dd785ff5996174684cc4de84_1440w.jpg)

但是，这就失去了窗口函数的功能，所以一般不要这么使用。


## **五.总结**

### **1.窗口函数语法**

```text
<窗口函数> over (partition by <用于分组的列名>
                order by <用于排序的列名>)
```

<窗口函数>的位置，可以放以下两种函数：

1） 专用窗口函数，比如rank, dense_rank, row_number等

2） 聚合函数，如sum. avg, count, max, min等



### **2.窗口函数有以下功能：**

1）同时具有分组（partition by）和排序（order by）的功能

2）不减少原表的行数，所以经常用来在每组内排名



### **3.注意事项**

窗口函数原则上只能写在select子句中



### **4.窗口函数使用场景**

> 排名问题：每个部门按业绩来排名
> topN问题：找出每个部门排名前N的员工进行奖励
> 复购分析：App内要分析复购用户有多少
> 累计问题：医院要经常统计累计患者数

![img](https://pic3.zhimg.com/v2-925ae72ddd53f39eef1deb2a4d3767e4_1440w.jpg)

更多窗口函数的面试题和应用实操案例，可以看我最新实操视频：

[![img](https://pic1.zhimg.com/v2-c64da0bbe4508837984c9e9b48438d5c_r.jpg?source=172ae18b)SQL从入门到进阶(视频+社群)中科院猴子 的专栏23 篇内容 · 6 赞同 · 8 订阅](https://www.zhihu.com/column/c_1890781095961782061)



编辑于 2025-10-12 23:58・北京