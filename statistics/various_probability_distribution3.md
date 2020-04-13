# 15 いろいろな確率分布3 (various probability distribution 3)

## 指数分布(exponential distribution)

次に何かが起こるまでの期間が従う分布

単位時間あたり &lambda; 回起こるとき確率密度関数f(x)は

![](https://bellcurve.jp/statistics/wp-body/wp-content/ql-cache/quicklatex.com-141fe1ae10445a3a1547c2ed647ae980_l3.png)

期待値E(X)は

![](https://bellcurve.jp/statistics/wp-body/wp-content/ql-cache/quicklatex.com-27d4771420e3a3a119e304f4ef21185d_l3.png)

分散V(X)は

![](https://bellcurve.jp/statistics/wp-body/wp-content/ql-cache/quicklatex.com-94bf7a1e9f7879b24f167eb7e53aa828_l3.png)

期間Xがx以下になる確率はxまでの累積分布関数F(x)として以下の通りとなる

![](https://bellcurve.jp/statistics/wp-body/wp-content/ql-cache/quicklatex.com-13a71e25092da3428245769d1f820682_l3.png)

## 離散一様分布

確率変数Xが離散型である場合にすべての事象の起こる確率が等しい分布
X=kとなる確率P(X=k)は

![](https://bellcurve.jp/statistics/wp-body/wp-content/ql-cache/quicklatex.com-fb662f0525a7ea5275ec1b823e0968ca_l3.png)

期待値E(X)は

![](https://bellcurve.jp/statistics/wp-body/wp-content/ql-cache/quicklatex.com-55ea49beb04e1536dc39a3d7a21b9647_l3.png)

分散V(X)は

![](https://bellcurve.jp/statistics/wp-body/wp-content/ql-cache/quicklatex.com-b462629c5df7fa2a84c56994adbe0577_l3.png)

## 連続一様分布

確率変数Xがどのような値でもその時の確率密度関数f(x)が一定の値をとる分布のこと
面積は１なので。

![](https://bellcurve.jp/statistics/wp-body/wp-content/ql-cache/quicklatex.com-28e0ef51c11ee78b769542725daaf4e8_l3.png)

f(x) = 0 (X<a, X>b)

期待値E(X)は

![](https://bellcurve.jp/statistics/wp-body/wp-content/ql-cache/quicklatex.com-ebc1fec6a0811f23fa4870ad63bfd0b3_l3.png)

分散V(X)は

![](https://bellcurve.jp/statistics/wp-body/wp-content/ql-cache/quicklatex.com-30666c45cca17df7a4aa646276610138_l3.png)

## 2変数の確率分布

確率変数が２つある場合にそれぞれの確率変数がとる値とその確率の分布を「同時確率分布」という

### 離散型

周辺確率関数とはただ一つだけの事象が起きる確率

### 連続型

XとYの童子確率分布を表す関数　＝　同時確率密度関数f(x,y)
確率Pはこの確率密度関数から

![](https://bellcurve.jp/statistics/wp-body/wp-content/ql-cache/quicklatex.com-007f0186e67e1b882ebb59416d26ebfe_l3.png)

### 期待値と分散

E(X+Y) = E(X) + E(Y)

E(XY) = E(X)E(Y)

V(X+Y) = V(X) + V(Y) + 2Cov(X,Y)

V(X-Y) = V(X) + V(Y) - 2Cov(X,Y)

Cov(X,Y) = E[(X- &mu; x)(Y - &mu; y)] = E(XY) - &mu; x &mu; y

ここから相関係数を計算できる
共分散Cov(X,Y)をそれぞれの標準偏差で割ったものが相関係数

![](hhttps://bellcurve.jp/statistics/wp-body/wp-content/ql-cache/quicklatex.com-f086eb6706d68398473f80c120d2d921_l3.png)

