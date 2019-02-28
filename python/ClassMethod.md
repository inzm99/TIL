# Class Method とは

インスタンス化しなくても呼び出せるメソッド

通常、@classmethod デコレータをつけることで定義する

```python
class sampleClass:
    @classmethod
    def sampleMethod(cls,*args):
        print(cls)
```

classmethodは、第一引数にクラスを受け取るので、明示的にclsを第一引数に書くのが慣例
