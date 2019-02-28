# f-stringについて

Python3.6からの機能でformatではなく、新しいスタイルとして以下のように記述可能
Stringの頭にfをつけ、変数を{}で囲むことで代入できる。

```python
a = 'a'
print(f'a is {a}')
 
x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')
```

