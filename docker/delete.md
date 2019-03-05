### 停止しているコンテナをすべて削除する
```
docker container prune
```
### 使われていないボリュームをすべて削除する
```
docker volume prune
```
### コンテナをすべて削除する
```
docker rm -f $(docker ps -a -q)
```
### コンテナが使っていないイメージをすべて削除する
```
docker image prune
```
### タグがついていないイメージをすべて削除する
```
docker rmi $(docker images -f 'dangling=true' -q)
```
imageタグが``` <none>:<none> ```のうちコンテナから参照されていないものを削除できる
コンテナから参照されていて消えないものはコンテナを先に消すことで削除できる
### コンテナ、イメージ、ボリュームの一括削除
```
docker system prune
```
停止コンテナ、未使用イメージ、未使用ボリュームをまとめて削除できる
