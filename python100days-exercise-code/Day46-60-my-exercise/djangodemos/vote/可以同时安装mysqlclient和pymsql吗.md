**可以同时安装**。这两个库在底层互不冲突，因为它们在 Python 中是作为独立的第三方包存在于各自的目录中的。

为什么可以共存？

- **mysqlclient** 是基于 Python 的 C API 开发的，执行速度快，底层依赖 MySQL 的 C 语言客户端库。
- **PyMySQL** 是纯 Python 实现的，不依赖 C 语言环境，安装配置非常简单，并且高度兼容 `mysqlclient`（也可以通过 `pymysql.install_as_MySQLdb()` 伪装成 `mysqlclient` 来使用）。

使用建议与注意事项

尽管可以共存，但在代码中只能选择一个作为数据库驱动来建立连接。

- **框架兼容性**：如果您在使用 **Django** 框架，它默认推荐 `mysqlclient` 作为 MySQL 后端驱动。当由于编译安装困难报错时，很多开发者会通过 PyMySQL 来替代 **[\**\*\*![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAB/UlEQVR4AbSST0iUURTFf+/LxKyoZmWbNioSiBREMzouXLSIkYKQNjUqAy5azVAUIf1hCoIsqqlWswjGKSYZZm/Qsn8TtLVNWpjQQsTFQKjV973Oy6ZpUNyIj3vmnXvvu2fO+3gem1xbJJCyA6Tsa5J2WVgR3ig/vZ7ZtQ6SNoOlJOwW7mnoruB4UUIZ8bqoF0jaU+qmhPuEOMxjc4VH5iohDgEPhZScDGj/F/UC4IY/auASaRNQXY6HuIAlRcBCtez2VYHy5y7Kn0rE5jo4+dVyfGYEaw3V5XgrI4Q5y1Ge8NSWKNgu1/b48CUMQRlML3t/vGDXzwqQ5f10kbdzO8ja7Twj/6cW4GN4Jd4rVua5DXv4/pgK8zT4nUTaEkIP2PNg+vGDKM2UgDiWywyZHuImwTY6VZvnF2OerEY1UOBIR+1ukfYM35sPMnvgog6eEM5p+I721ThjFiRYUBLVN/Cc5RYltcjbnXzbn9OhY7KcYNBka82/zNCiXkUCwQSYOO+mh5maaqRo9wAvhagE4sTNuHgtiraRcTusgrvWhAQYVVKWWo5K0yLe8qx4t2oNQo68XuP/WGEJjxzgZkY9Iu0Vwq19+rcYi6FrLDW513ZDB25K6PYaWK6rFmOGPrlzVwCMHk132yT9+x4waNIbYsjc0uAkac2AzOhnM/EbAAD//2hPdxgAAAAGSURBVAMAhd64IYuHAbMAAAAASUVORK5CYII=)\*\**\*⁠解决Django连接MySQL报错问题](https://cloud.tencent.com/developer/article/1755110)**。
- **API调用**：在您自己编写的代码中，请保持统一。例如 `import pymysql` 就使用 `pymysql.connect`，而 `import MySQLdb`（mysqlclient）就使用 `MySQLdb.connect`，不要在同一个连接池或事务中混用两者。

如果您在项目中遇到特定的报错或想要在这两