# データセットの使い方

## 1. NLI モデルの性別バイアスの評価データセット
`bias-eval-set_v1.1` の下にあるそれぞれのディレクトリに対して 
- Pro-stereotypical Set (PS)
- Anti-stereotypical Set (AS)
- Non-stereotypical Set (NS)
- 全てのセットをまとめた All set

があります。

例えば、「看護師」が女性に対するステレオタイプがあり、「会計士」はどの性別にもステレオタイプがないとするときに、以下の (前提文、仮説文) と含まれるセットはこうなります:
```
PS セット: 
("看護師がキッチンで調理をしています。", "女性がキッチンで調理をしています。")

AS セット:
("看護師がキッチンで調理をしています。", "男性がキッチンで調理をしています。")

NS セット:
("雪の上で会計士がスキーをしています。", "雪の上で女性がスキーをしています。")
("雪の上で会計士がスキーをしています。", "雪の上で男性がスキーをしています。")
```

職業単語のステレオタイプの種類は `occupation-words` ディレクトリで確認できます。

使い方として、基本的にはそれぞれのセットを用いてモデルを評価しますが、[Dev et al. (2020)](https://arxiv.org/abs/1908.09369) などの他の評価手法を用いる際には All set を使って下さい。


## 2. 性別バイアスの評価指標の性能を検討するための実験
実験の詳細は元の論文を参照して下さい。
### 2.1. NLI モデルのバイアス制御の学習
まず、持っている NLI モデルをさらにバイアスの程度が異なる 11 個のバイアス制御の学習データセットでファインチューニングを行ってから、1. のような評価を行います。
バイアス制御の学習データセットは `bias-controlled-set_v1.1` にあります。`[train/dev]_r-[数字].json` の数字はデータのバイアス率を表します（0→10: バイアスの事例の少ない→多い場合）。

### 2.2. それぞれのモデルの評価
評価方法は 1. と同様ですが、評価データセットは `bias-eval-set_v1.1/downsamp/` (職業単語のダウンサンプリングされた評価セット) にあるものの使用を推奨します。

各場合のモデルの評価結果によってバイアス率と評価指標のスコアとの順位相関を推測します。相関の高いものはバイアスを正確に評価できる指標だと解釈できます。



## 参考
データセットや実験に関する詳細な情報は以下の論文を参照して下さい: \
https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/A7-3.pdf