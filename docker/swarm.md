# Docker Swarm

## ホストマシンをSwarmでつなぐ

### まずは Swarm Cluster を作る

docker swarm init --advertise-addr [通信するIP]

### Swarm Cluster に Worker node を追加

追加したいホスト上で
docker swarm join --token [token] [宛先IP]

### Swarm Cluster に Manger node を追加

docker swarm join-token manager
で表示されたtokenを使って、
追加したいホスト上で
docker swarm join --token [token] [宛先IP]
 
### node を一覧表示

docker node ls

#### node の状態を変更する

Active：割当可能
Pause：割当不可だが、既存のタスクは実行
Drain：割当不可、既存のタスクも終了

```
docker node update --availability [Active or Pause or Drain] [node name]
```

## Servce と Task の実行

### Replica mode

ホストのCPUやメモリの状態で、自動的にタスクを振り分けて(scheduling)起動。

```
docker service create --replicas n [image name]
```

n:imageを何個起動するかを指定(replica number)

### Global mode

一つのホストで一つのタスクを起動するモード

```
docker service create --name [service name] --mode global [image name]
```

### 起動した servce の状態確認

```
docker service ls
```

#### servce 詳細

```
docker service inspect -pretty [service name]
```
結果
```
ID:     0u6a4s31ybk7yw2wyvtikmu50
Name:       redis
Mode:       REPLICATED
 Replicas:      3
Placement:
 Strategy:  SPREAD
UpdateConfig:
 Parallelism:   1
 Delay:     10s
ContainerSpec:
 Image:     redis:3.0.7
 ```

## Rolling Update ローリングアップデート

サービスの作成(redis:3.0.6をデプロイ）

```
docker service create --replicas 3 --name redis --update-delay 10s redis:3.0.6
```

アップデート開始(redisを3.0.6から3.0.7へUpdate)
```
docker service update -image redis:3.0.7 redis
```

サービスの監視(徐々にデプロイされるのが見れる）

```
docker service tasks redis
```
