# How to create data container

## pull busy box
```
docker image pull busybox
```
## create data container
```
docker container run -it -v /data001 --name d0001 busybox /bin/sh
```
## save test file
```
echo " test " > /data001/testfile.txt
```
## use the volume from another container 
```
docker container run -it --volumes-from d0001 --name c0004 -h c0004 busybox
# cat /data001/testfile.txt
```

## Backup data container volume
/ctdir配下に" backup.tar"というファイルでバックアップする。
Windowsの場合MobyLinux(裏で動いているlinux)上のディレクトリに生成されてしまうので、
簡単にアクセスできない場所に保存されてしまう。
```
docker container run --rm --volumes-from d0001 -v /hostdir:/ctdir busybox tar cvf /ctdir/backup.tar /data001
```
## Backup data container volume for windows
事前設定として、Cドライブの共有設定が必要 (DockerDesktop ＞ setting ＞ SharedDrives)
```
docker container run --rm --volumes-from d0001 -v c:/ban:/ctdir busybox tar cvf /ctdir/backup.tar /data001
```
## Restore volume
```
docker container run -it -v /data001 --name c0005 -h c0005 busybox /bin/sh
docker container run --rm --volumes-from c0005 -v /hostdir:/ctdir busybox tar xvf /ctdir/backup.tar -C /
```
tar の -C　…これは解凍先のディレクトリを変更する。
つまり、/hostdirにあるbackup.tarファイルを/data0001配下（c0005でマウント）に展開している。

##おまけ
tar の --strip=1　…これはtarアーカイブ内のディレクトリを1階層分無視する。
