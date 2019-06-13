# How to pip install offline

1.download package

```sh
pip download -d <directory> --no-binary :all: <packagename>
```

2.install package

```sh
cd <directory>
pip install <packagename>.tar.gz
```
