# Proxy配下でdockerやdocker-composeを使う

dockerとdocker-compose
どちらもProxy配下で実行する場合は~/.docker/.config.jsonにproxyを書く。

windowsの場合は

C:\\Users\\username\\.docker\\config.json

```
{
 "proxies":
 {
   "default":
   {
     "httpProxy": "http://ID:PASS@proxy.domain.com:8080",
     "httpsProxy": "http://ID:PASS@proxy.domain.com:8080",
   }
 }
}
```

下手にENVやARGSで指定してしまうとdocker historyやdocker image inspectでproxyや認証Proxyの場合はID,PASSが漏れてしまうので注意。

セッティング後はdockerの再起動が必要。

[参考](https://docs.docker.com/network/proxy/#configure-the-docker-client)
