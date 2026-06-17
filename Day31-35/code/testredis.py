import redis

def inspect_redis_server(host='localhost', port=6379):
    # 1. 建立无密码连接
    client = redis.Redis(host=host, port=port, password=None, decode_responses=True)
    client.set('guido','U2Vuc2l0aXZlIGRhdGEgd2l0aCArIGFuZCAvIGNoYXJhY3RlcnM=')
    # client.delete('guido;')
    print(client.get("guido2"))
    # try:
    #     # 测试连接是否正常
    #     if client.ping():
    #         print(f"成功连接到 Redis 服务器: {host}:{port}")
            
    #         # 2. 获取服务器基本信息 (等同于 INFO 命令)
    #         info = client.info()
    #         print(f"\n--- Redis 服务器信息 ---")
    #         print(f"Redis版本: {info.get('redis_version')}")
    #         print(f"当前连接数: {info.get('connected_clients')}")
    #         print(f"内存使用总量: {info.get('used_memory_human')}")
    #         print(f"运行时间(秒): {info.get('uptime_in_seconds')}")

    #         # 3. 获取服务器上所有的 keys (谨慎操作：若键过多可能会阻塞服务器)
    #         keys = client.keys('*')
    #         print(f"\n--- 所有 Key 列表 (共 {len(keys)} 个) ---")
    #         for key in keys:
    #             print(f"Key: {key}")
                
    #     else:
    #         print("连接失败，请检查服务器是否开启。")
            
    # except Exception as e:
    #     print(f"发生错误: {e}")

if __name__ == "__main__":
    # 请根据您的实际Redis服务器 IP 修改 host
    inspect_redis_server(host='127.0.0.1', port=6379)


