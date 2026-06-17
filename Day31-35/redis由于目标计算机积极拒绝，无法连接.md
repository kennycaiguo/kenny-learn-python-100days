“由于目标计算机积极拒绝”通常意味着您的 Redis 服务尚未启动，或者被系统防火墙拦截。 [[1](https://blog.csdn.net/lovely__RR/article/details/107088929), [2](https://comate.baidu.com/zh/page/uqqszo36mvo)]

请按照以下步骤排查和解决该问题： [[1](https://comate.baidu.com/zh/page/uqqszo36mvo)]

#### 安装了redis后需要把bin目录路径设置到环境变量

#### **1. 检查并启动 Redis 服务**
在尝试连接前，必须先启动 Redis 服务端程序。 [[1](https://www.cnblogs.com/mike-mei/p/17619665.html), [2](https://blog.csdn.net/lovely__RR/article/details/107088929)]

- **Windows**：打开命令行（CMD）进入 Redis 安装目录，执行 `redis-server.exe redis.windows.conf`。保持该黑框窗口处于打开状态。
- **Linux / macOS**：执行命令 `sudo systemctl start redis` 或 `redis-server /path/to/redis.conf`。 [[1](https://cloud.tencent.com/developer/article/2072857), [2](https://www.cnblogs.com/mike-mei/p/17619665.html)]

#### **2. 确认客户端连接方式**
启动服务端后，不要关闭该窗口，另起一个命令行窗口执行以下命令连接： [[1](https://www.cnblogs.com/mike-mei/p/17619665.html), [2](https://cloud.tencent.com/developer/article/2072857)]

bash

```
redis-cli -h 127.0.0.1 -p 6379
```

请谨慎使用此类代码。

#### **3. 检查配置文件 (redis.conf)**
如果确认服务已启动，但依然报错，请检查配置文件以确保允许本地连接： [[1](https://blog.csdn.net/Hdu_lc14015312/article/details/104504575), [2](https://juejin.cn/post/7387539709206134794)]

- 找到并打开 `redis.conf`。
- 确保已注释掉 `bind 127.0.0.1`（在该行前加 `#`），或确保其绑定了正确的 IP。