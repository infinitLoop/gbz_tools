#!/bin/bash

cd ~
sudo apt-get update
sudo apt-get install python-gpiozero -y
cd ~
if ! grep '^\/home\/pi\/gbz_tools\/volume_buttons.py \&' /etc/rc.local; then
    sudo sed -i '/\"exit 0\"/!s/exit 0/python \/home\/pi\/gbz_tools\/volume_buttons.py \&\nexit 0/g' /etc/rc.local
fi
#sudo python /home/pi/gbz_tools/volume_buttons.py &


