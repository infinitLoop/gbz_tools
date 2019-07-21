#!/bin/bash

cd /home/pi
sudo apt-get update
sudo apt-get install cmake -y
git clone https://github.com/juj/fbcp-ili9341.git
mkdir /home/pi/fbcp-ili9341/build
cd /home/pi/fbcp-ili9341/build
# pi Zero
cmake -DARMV6Z=ON -DILI9341=ON -DSPI_BUS_CLOCK_DIVISOR=6 -DGPIO_TFT_DATA_CONTROL=24 -DGPIO_TFT_RESET_PIN=25 -DSTATISTICS=0 -DDISPLAY_ROTATE_180_DEGREES=ON ..
# pi 3
#cmake -DARMV8A=ON -DILI9341=ON -DSPI_BUS_CLOCK_DIVISOR=6 -DGPIO_TFT_DATA_CONTROL=24 -DGPIO_TFT_RESET_PIN=25 -DSTATISTICS=0 -DDISPLAY_ROTATE_180_DEGREES=ON ..
make -j
if ! grep '^\/home\/pi\/fbcp-ili9341\/build\/fbcp-ili9341 \&' /etc/rc.local; then
    sudo sed -i '/\"exit 0\"/!s/exit 0/\/home\/pi\/fbcp-ili9341\/build\/fbcp-ili9341 \&\nexit 0/g' /etc/rc.local
fi
sudo /home/pi/fbcp-ili9341/build/fbcp-ili9341 &
cd ~
