#!/bin/bash

cd ~
sudo apt-get update
sudo apt-get install libpng12-dev -y
sudo apt-get install python-pkg-resources python3-pkg-resources -y
sudo apt-get install python-gpiozero -y
sudo pip install wiringpi2
cd ~
sudo chmod 755 /home/pi/gbz_tools/Pngview/pngview2
sudo sed -i '/\"exit 0\"/!s/exit 0/python \/home\/pi\/gbz_tools\/combo_button.py \&\nexit 0/g' /etc/rc.local
