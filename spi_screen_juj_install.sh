#!/bin/bash

cd ~
sudo apt-get update
sudo apt-get install cmake -y
git clone https://github.com/juj/fbcp-ili9341.git
cd fbcp-ili9341
mkdir build
cd build
cmake -DARMV6Z=ON -DILI9341=ON -DSPI_BUS_CLOCK_DIVISOR=6 -DGPIO_TFT_DATA_CONTROL=24 -DGPIO_TFT_RESET_PIN=25 -DSTATISTICS=0 -DDISPLAY_ROTATE_180_DEGREES=ON ..
make -j
sudo sed -i '/\"exit 0\"/!s/exit 0/\/home\/pi\/fbcp-ili9341\/build\/fbcp-ili9341 \&\nexit 0/g' /etc/rc.local
cd ~