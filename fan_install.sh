#!/bin/bash

cd ~
sudo apt-get update
sudo apt-get install rpi.gpio -y
if ! grep '^\/home\/pi\/gbz_tools\/fan.py \&' /etc/rc.local; then
    sudo sed -i '/\"exit 0\"/!s/exit 0/python \/home\/pi\/gbz_tools\/fan.py \&\nexit 0/g' /etc/rc.local
fi

