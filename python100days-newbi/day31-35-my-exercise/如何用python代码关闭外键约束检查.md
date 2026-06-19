在Python中关闭外键约束检查，最常见的方法是在执行数据库操作前，通过执行原生的 SQL 语句（或特定的 PRAGMA 指令）来临时禁用它。

针对不同的数据库类型，核心代码如下： [[1](https://blog.csdn.net/v123411739/article/details/24868041), [2](https://www.cnblogs.com/lsgxeva/p/12488365.html), [3](https://cloud.tencent.com/developer/article/2395022)]

1. MySQL / MariaDB

使用 `cursor.execute()` 执行 `SET FOREIGN_KEY_CHECKS = 0` 来关闭检查，操作完成后再开启。 [[1](https://blog.csdn.net/v123411739/article/details/24868041), [2](https://cloud.tencent.com/developer/article/2395022)]

python

```
import mysql.connector

# 建立连接
conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='test_db')
cursor = conn.cursor()

# 1. 关闭外键约束检查
cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

# 2. 执行你的批量插入、更新或删除操作
# cursor.execute("DELETE FROM parent_table") 

# 3. 重新开启外键约束检查（非常重要！）
cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

# 提交事务并关闭
conn.commit()
cursor.close()
conn.close()
```

 

2. SQLite

SQLite 默认不强制开启外键约束。如果你手动开启了，需要使用 `PRAGMA foreign_keys = OFF` 来关闭。 [[1](https://www.reddit.com/r/SQL/comments/1pkufn7/foreign_key_constraint_failed/?tl=zh-hans), [2](https://www.cnblogs.com/lsgxeva/p/12488365.html), [3](https://developer.aliyun.com/article/397842)]

python

```
import sqlite3

# 建立连接
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# 1. 关闭外键约束检查
cursor.execute("PRAGMA foreign_keys = OFF;")

# 2. 执行你的操作...

# 3. 重新开启外键约束检查
cursor.execute("PRAGMA foreign_keys = ON;")

conn.commit()
conn.close()
```

 

3. 使用 SQLAlchemy (ORM)

如果你在 Python 中使用的是 SQLAlchemy，可以通过事件监听或直接执行语句在连接建立时关闭检查： [[1](https://blog.csdn.net/zaaaacki/article/details/109405954)]

python

```
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:password@localhost/test_db')

# 监听连接池事件，确保每次获取连接时都关闭外键检查
@event.listens_for(engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cursor.close()

# 创建Session
Session = sessionmaker(bind=engine)
session = Session()

# 执行你的数据库操作...

session.commit()
session.close()
```

 