FROM ubuntu:20.04

# 各環境変数を設定
ENV USER tane
ENV HOME /home/${USER}
ENV SHELL /bin/bash

# 一般ユーザーアカウントを追加
RUN useradd -m ${USER}
# 一般ユーザーにsudo権限を付与
RUN gpasswd -a ${USER} sudo
# 一般ユーザーのパスワード設定
RUN echo "${USER}:81418" | chpasswd
# ログインシェルを指定（アカウント情報の作成）
RUN sed -i.bak "s#${HOME}:#${HOME}:${SHELL}#" /etc/passwd

# 以降のRUN/CMDを実行するユーザー
USER ${USER}
# 以降の作業ディレクトリを指定
WORKDIR ${HOME}