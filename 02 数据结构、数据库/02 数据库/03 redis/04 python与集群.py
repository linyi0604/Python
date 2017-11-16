#coding:utf8

if __name__ == '__main__':
    # 1创建集群连接
    startup_nodes = [{"host":"192.168.85.70","pory":7000},
                     {"host": "192.168.85.70", "pory": 7001},
                     {"host": "192.168.85.70", "pory": 7003}
                     ]
    cluster_redis = StricRedisCluster(startup_nodes,decode_response="true")
    cluster_redis.set("name","A")
    res = cluster_redis.get("name")
    print(res)