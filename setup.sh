#!/bin/bash

sudo apt update

# Not sure if this is needed
# apt upgrade

sudo apt install -y python3-pip

pip3 --version

pip3 install praw

pip3 install -U requests

pip3 install -U pathlib

pip3 install fbchat

pip3 install python-dotenv

sudo apt install -y snapd

sudo snap install -y gallery-dl

sudo snap connect gallery-dl:removable-media

sudo apt-get install -y python-dev libxml2-dev libxslt1-dev zlib1g-dev

# Modification of the fbchat package in order to make it work
sudo cp package-modifications/_state.py /usr/local/lib/python3.6/dist-packages/fbchat/_state.py


