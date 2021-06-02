FROM ubuntu:20.04

LABEL maintainer="tanetakumi"

ENV DISPLAY host.docker.internal:0.0

ENV DEBIAN_FRONTEND=noninteractive

# ENV HOME /home/${USER}
ENV SHELL /bin/bash

RUN apt-get update && apt-get -y upgrade

RUN apt-get -y install build-essential

RUN apt-get -y install python3 && apt-get -y install python3-pip


RUN apt -y install git\
    && apt -y install wget\
    && apt -y install tar\
    && apt -y install vim\
    && apt -y install x11-apps\
    && apt-get -y install python3-tk

# set -ex コマンドの実行に失敗したらその場で終了する
RUN set -ex\ 
    \
    && wget -O jsim-2.0e.tar.gz "http://www.wrcad.com/ftp/pub/jsim-2.0e.tar.gz"\
    && tar -zxvf jsim-2.0e.tar.gz\
    && rm jsim-2.0e.tar.gz\
    && cd jsim-2.0e\
    && make\
    && cp jsim /usr/local/bin

RUN pip install -r requirments.txt
# 一般ユーザーアカウントを追加
# RUN useradd -m ${USER}
# 一般ユーザーにsudo権限を付与
# RUN gpasswd -a ${USER} sudo
# 一般ユーザーのパスワード設定
# RUN echo "${USER}:81418" | chpasswd
# ログインシェルを指定（アカウント情報の作成）
# RUN sed -i.bak "s#${HOME}:#${HOME}:${SHELL}#" /etc/passwd

# 以降のRUN/CMDを実行するユーザー
# USER ${USER}
# 以降の作業ディレクトリを指定
# WORKDIR ${HOME}

# http://www.wrcad.com/ftp/pub/jsim-2.0e.tar.gz