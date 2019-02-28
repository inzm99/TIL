# loggerの設定

```python
import logging

logger = logging.getlogger(__name__)
```

__naeme__とすることで、どのファイルでのログかがわかる。
例えば別のpythonファイルをimportしたとすると、import元と先のどちらのログ化が一目でわかるようになる。

logger.setLevel(logging.DEBUG)

# handler

## Stream handler

標準出力

## File handler

ファイルに書き込む

```python
h = logging.FileHandler('logfile.log')
logger.addHandler(h)
```

# Logging filter

ロギングする際に特定の文字、例えばパスワードなんかを含んだログを出力させないようにフィルターをかけることができる。

# Logging config

## File Config

Logging.iniというようなファイルに設定を書いて読み込む方法

```python
logging.config.fileConfig('logging.ini')
```

## Dict Config

Dictionary型で指定する方法

```python
logging.config.DictConfig({

hogehoge

})
```
