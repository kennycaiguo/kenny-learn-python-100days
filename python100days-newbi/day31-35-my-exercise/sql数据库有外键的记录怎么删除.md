删除包含外键的记录时，直接执行删除会触发外键约束报错。主要取决于您的业务需求，可通过以下三种最常用的方式进行处理： [[1](https://support.huaweicloud.com/trouble-taurusdb/taurusdb_trouble_0207.html), [2](https://www.cnblogs.com/shiningrise/p/17846415.html), [3](https://www.cnblogs.com/weiqt/articles/1834441.html), [4](https://help.aliyun.com/zh/dts/user-guide/solution-with-foreign-key-references-on-delete-cascade)]

1. 先删子表，后删主表（常规方法）

必须先删除引用该记录的外键表（从表/子表）数据，然后再删除被引用的主表记录。 [[1](https://www.cnblogs.com/shiningrise/p/17846415.html)]

sql

```
-- 1. 先删除子表中关联的记录
DELETE FROM 子表名 WHERE 关联字段 = '某值';

-- 2. 再删除主表中的记录
DELETE FROM 主表名 WHERE 主键字段 = '某值';
```

 

2. 临时关闭外键检查（快速删除/清空）

如果您想直接删除主表记录，或者需要清空整张表但不想处理繁琐的依赖顺序，可以在操作前**临时禁用外键约束**。 [[1](https://blog.csdn.net/qq_37439115/article/details/120815854), [2](https://cloud.tencent.com/developer/article/1354599)]

sql

```
-- 以 MySQL 为例
SET FOREIGN_KEY_CHECKS = 0; -- 临时关闭外键约束
DELETE FROM 主表名 WHERE 主键字段 = '某值';
SET FOREIGN_KEY_CHECKS = 1; -- 操作完成后，恢复外键约束
```

 

3. 设置“级联删除”（长期有效）

若希望删除主表记录时，数据库自动删除所有引用该记录的子表数据，可以在建表时通过 `ON DELETE CASCADE` 声明外键。
已有外键的需先删除原外键，再重新添加： [[1](https://www.cnblogs.com/weiqt/articles/1834441.html), [2](https://blog.csdn.net/leleshengh520/article/details/143757369)]

sql

```
-- 1. 删除原外键约束（以具体约束名为准）
ALTER TABLE 子表名 DROP FOREIGN KEY 外键名称;

-- 2. 重新添加带有级联删除的外键约束
ALTER TABLE 子表名 
ADD CONSTRAINT 外键名称 
FOREIGN KEY (外键字段) REFERENCES 主表名(主键字段) 
ON DELETE CASCADE;

-- 3. 之后直接删除主表记录，子表关联数据会自动被删
DELETE FROM 主表名 WHERE 主键字段 = '某值';
```

 