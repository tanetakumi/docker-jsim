# Docker Jsim
created by tanetakumi

# linux knowledge

## 「/bin」「/usr/bin」「/usr/local/bin」ディレクトリの使い分け

「/bin」ディレクトリには、シングルユーザモードでも利用できるコマンドを置く
「/usr/bin」や「/usr/local/bin」に置かれているコマンドなどはシングルユーザモードで利用できない。
シングルユーザモードは、基本的にOSが壊れて正常に起動できないなど非常時に利用するものだから、「/bin」にはごく基本的かつ非常時に利用するコマンドが置かれることになる。

