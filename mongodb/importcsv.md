# Howto import in mongodb for csv file

## インポートを実行

```
mongoimport --db fd --collection port --type csv --file import.csv --headerline
```

ちなみに、ここで使用しているオプションは

```
--db DB名 (fd)
--collection コレクション名 (port)
--type 入力ファイル形式 (csv)
--file 入力ファイル名 (import.csv)
--headerline ヘッダ行の無視
```

## 正しくインポートされたかどうか確認

```
$ mongo
> use fd
switched to db fd
> db.port.find()
(result...)
```
