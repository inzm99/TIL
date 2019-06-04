# How to pass arguments for Docker

## 環境変数を使う方法

`docker run` するときに「-e」オプションで環境変数を渡す。

```cmd
docker run -e BIND_ADDRESS=127.0.0.1 -e BIND_PORT=8080 -t example
```

### ファイルで渡す

環境変数を書いたテキスト（この場合envfile.txt) を渡すことによって環境変数を渡す。

```cmd
docker run --env-file envfile.txt -t example
```

```txt:envfile.txt
BIND_ADDRESS=127.0.0.1
BIND_PORT=8080
```

### Dockerfileに書く（デフォルト値を指定する）

```cmd
docker build -t example .
docker run -t example
```

```dockerfile:Dockefile
FROM alpine

ENV BIND_ADDRESS 127.0.0.1
ENV BIND_PORT 8080

CMD env
```

### シェルスクリプトファイルを渡して実行する

```dockerfile:Dockerfile
FROM alpine

COPY .entrypoint.sh /usr/local/bin/

ENTRYPOINT ["entrypoint.sh"]
```

```sh:entrypoint.sh
#!/bin/sh

echo ${BIND_ADDRESS:-127.0.0.1}
echo ${BIND_PORT:-8080}
```

### コマンドライン引数で渡す

たとえば、以下のentrypointを作成すると、docker run時の引数として渡したものをそのまま表示できる。

```cmd
docker run -t example hogehoge
-> hogehoge
```

```sh:entrypoint.sh
#!/bin/sh
echo $@
```

シェルスクリプトを駆使して引数として渡せるようにする。

```dockerfile:Dockerfile
FROM alpine

COPY .entrypoint.sh /usr/local/bin/

ENTRYPOINT ["entrypoint.sh"]
```

```cmd
docker build -t example .
docker run -t example -a 127.0.0.1 -p 8080
```

```sh:entrypoint.sh
#!/bin/sh

usage() {
  echo "Usage: $0 [-a bind-address] [-p bind-port]" 1>&2
  exit 1
}

while getopts a:p:h OPT
do
  case $OPT in
    a)  BIND_ADDRESS=$OPTARG
        ;;
    p)  BIND_PORT=$OPTARG
        ;;
    h)  usage
        ;;
  esac
done

echo ${BIND_ADDRESS:-127.0.0.1}
echo ${BIND_PORT:-8080}
```
