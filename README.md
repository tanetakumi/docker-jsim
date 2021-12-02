# Docker Jsim
created by tanetakumi

# How to create Environment
Docker ubuntu:20.04

automatic 
1. download jsim from [Jsim](http://www.wrcad.com/)
2. untar (tar.gz)
3. make jsim by build-essential
4. copy jsim to /usr/local/bin

# linux knowledge


## 「/bin」「/usr/bin」「/usr/local/bin」ディレクトリの使い分け

[参考サイト](https://linuc.org/study/knowledge/544/)

```
「/bin」ディレクトリには、シングルユーザモードでも利用できるコマンドを置く
「/usr/bin」や「/usr/local/bin」に置かれているコマンドなどはシングルユーザモードで利用できない。
シングルユーザモードは、基本的にOSが壊れて正常に起動できないなど非常時に利用するものだから、「/bin」にはごく基本的かつ非常時に利用するコマンドが置かれることになる。
```

## github リポジトリ名　命名規則
基本的に規則はない
慣習は、アルファベット小文字と一部のascii文字を使う。
単語の区切りに関しては、ハイフンを使うのがよい。


## python 命名規則   
[参考サイト](https://qiita.com/naomi7325/items/4eb1d2a40277361e898b)

パッケージ	　

    全小文字 なるべく短くアンダースコア非推奨	
    tqdm, requests ...

モジュール	
    
    全小文字 なるべく短くアンダースコア可	
    sys, os,...

クラス	

    最初大文字 + 大文字区切り
    MyFavoriteClass

メソッド、関数、変数

    全小文字 + アンダースコア区切り
    my_func

