FROM python:3.6

# Aqui estou criando alguns comandos uteis para usar no bash

RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \
    echo "export LS_OPTIONS='--color=auto'" >>~/.bashrc && \
    echo "eval "\`dircolors\`"" >>~/.bashrc && \
    echo "alias ls='ls \$LS_OPTIONS'" >>~/.bashrc && \
    echo "alias ll='ls \$LS_OPTIONS -l'" >>~/.bashrc && \
    echo "alias l='ls \$LS_OPTIONS -lA'" >>~/.bashrc

# A estou atualizando minha distro e instalando o uwsgi p django

RUN apt-get update --fix-missing && \
    apt-get install -y curl vim nano git locales zip unzip && \
    pip install uwsgi uwsgitop

# Aqui estou baixando o node 9.1.0 dentro do file /tmp, desempacotando, dps copiando para /usr, dps removendo o tar.xz
# que baixou e em seguida instalando o node.

RUN cd /tmp && \
    wget --quiet https://nodejs.org/dist/v9.1.0/node-v9.1.0-linux-x64.tar.xz && \
    tar xf node-v9.1.0-linux-x64.tar.xz && \
    cp -r node-v9.1.0-linux-x64/* /usr && \
    rm node-v9.1.0-linux-x64.tar.xz && \
    npm install -g pm2

# Criei uma pasta chamada dkdata
RUN mkdir /dkdata

# Cria e já entra dentro desta pasta app
WORKDIR /app

# Estou copiando o arquivo requirements para dentro de /app
COPY requirements.txt ./

# Vou instalar os pacotes dentro do requirements
RUN pip install -r requirements.txt

# Estou copiando minhas dependencias do projeto node do frontend
COPY frontend/package.json frontend/package.json
COPY frontend/package-lock.json frontend/package-lock.json

# Instalando as dependeincias do front
RUN cd frontend && npm install

# Copiar e onstruir meu projeto front
COPY frontend frontend
RUN cd frontend && npm run build

# Criei variaveis de ambiente necessárias para rodar o ambiente
ENV SHELL=/bin/bash PYTHONUNBUFFERED=1 NODE_ENV=production API_MOCK=0 PYTHONIOENCODING=UTF-8 LANG=en_US.UTF-8 \
    DJANGO_STATIC_ROOT=/dkdata/static DJANGO_LOG_FILE=/dkdata/queroestudar.log UWSGI_PROCESSES=3 PORT=3000 \
    HOST=0.0.0.0 API_BASE_URL=http://localhost:8000 DJANGO_DB_NAME=postgres DJANGO_DB_USER=app DJANGO_DB_PASSWORD=app

# Copia tudo que está na pasta raiz do projeto para dentro de /app do container.

# Copia tudo que está dentro do docker/bin para usr/bin.
COPY . /app
COPY docker/bin/* /usr/bin/