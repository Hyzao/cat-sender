#!/bin/bash

sudo apt update

sudo apt install -Y python3-pip
sudo pip3 --version

sudo pip3 install praw

sudo pip3 install gallery-dl

sudo pip3 install -U requests

sudo pip3 install -U pathlib

sudo pip3 install fbchat

sudo apt install -Y snapd

sudo snap install -Y gallery-dl

sudo snap connect gallery-dl:removable-media

sudo apt-get install -Y python-dev libxml2-dev libxslt1-dev zlib1g-dev
