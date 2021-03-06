# 自由度とは

自由度とは統計量をお求めるのに用いられる標本数から制約の数を除いたもの。
つまり自由に動ける標本の数

### 簡単な例

4つの標本から平均を求める

Mean = a + b + c + d　/ 4

平均を固定した場合自由に動ける変数は　4-1で3つとなる。
これが自由度。

もう少し具体的にいうと、
平均が5だとする。

 5 = a + b + c + d / 4

そのうえで a, b, cに自由な値を入れると

 5 = 1 + 3 + 7 + d / 4

となり、dは一意に決まってしまう。つまり、この場合9しか取り得ない。
aかbかcかdのうち3つが決まると1つは自動的に決まってしまため、自由度は3ということになる。

N個の標本から平均を求めた場合、自由度はN-1

## 回帰分析の場合

y = ax + b

という2次元の単回帰分析を考える。

N個の標本から回帰直線を求めるのに必要な標本数は2個。
言い換えると、2個の点が決まると自動的に直線が決まる。

つまり他のN-2この標本だけが自由に動けるため、自由度はN-2となる。

では重回帰分析はどうなるか

3次元の場合を考える

z = ax + by + c

という3次元の重回帰分析から同様に考えた場合、どうなるか。
3次元なので、決まるのは一つの平面。

平面を決めるのに最低限必要な標本は3つであるため、自由度はN-3となる。

では一般化してみよう。

説明変数の数がk個ある場合、重回帰分析の標準の式は以下の通り
（&beta;は偏回帰係数）

y = &beta;0 + &beta;1 x1 + ... &beta;k xk

これはk+1次元となるため、これを決めるのに必要な標本数はk+1
つまり自由度はN-(k+1) = N-K-1


参考：
http://www2.toyo.ac.jp/~mihira/keizaitoukei2014/ols1.pdf
