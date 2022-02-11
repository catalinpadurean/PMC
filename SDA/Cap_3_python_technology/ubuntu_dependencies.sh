#! /usr/bin/bash

echo "Installing Python3 compilation dependencies for Ubuntu..."
sudo apt update

sudo apt install \
    build-essential zlib1g-dev libncurses5-dev \
    libgdbm-dev libnss3-dev libssl-dev \
    libreadline-dev libffi-dev make gcc tar \
    libsqlite3-dev uuid-dev curl

echo "Success!"