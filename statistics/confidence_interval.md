# 点推定の復習

点推定　＝　ピンポイント予想

標本平均（標本によって変わるので実は確率変数）母集団の平均や分散を推定する。

標本分散sは標本から計算した分散(sample variance)であるが、通常ほしいのは母集団の分散である不偏分散
不偏分散uは分散と違ってn-1で割ったもの(unviaced variance)

なぜn-1で割るのか

nが大きくなれば1/nも1/(n-1)もあまり変わらないが、nが小さい場合は
標本分散では真の分散を過小評価してしまう。

なぜなら、標本平均と実際の平均は違うから。

そこの差を計算するとn/(n-1)となる。計算式は下記がわかりやすい。
https://mathtrain.jp/huhenbunsan


# 母平均の区間推定（母分散既知）

## 区間推定とは

母集団のパラメータ（母平均など）を推定する場合点推定はピンポイント予想であったが、
ある範囲をもって推定するのが区間推定。
その時の区間が信頼区間(confidence Inerval)

母分散がわかっている場合、母分散を使って母平均を推定する。
（通常母分散だけがわかっているということはない）

95%信頼区間とは
「母集団から標本を取ってきて、その標本平均から母平均の95%信頼区間を求める、という作業を100回やったときに、95回はその区間の中に母平均が含まれる」
ということ。

ここでいう95%というのは変えることができ99%信頼区間とかも計算することができる。
この値を信頼係数（または信頼度）という。

### 信頼区間の求め方

1. 標本平均を求める
2. 標本平均の標準化をする（中心極限定理をもちいる）
3. 標準正規分布の95%の面積になるような点を求めるため上側2.5%（左右対称なので下側も2.5%）
点を標準正規分布表から求める。
4. 式をμについて変形すると信頼区間が求まる。

信頼区間は信頼係数が大きければ広がる。

信頼区間はサンプルサイズが大きければ狭まる。
