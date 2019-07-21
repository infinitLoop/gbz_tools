# Game Boy Zero Tools

This collection is intended to help add customizations to Raspberry-Pi-based retro handhelds, or other projects.  
It can support "safe" software shutdown, an on-screen battery monitor with customizable colors and placement, 
temperature-controlled fan, volume control, combo button controls and/or purpose-based buttons, 
as well as brightness control for LEDs or screen backlighting, and more.

Credit to HoolyHoo, whose GBZ and MintyPi projects were the basis of much of this: https://raw.github.com/HoolyHoo/

### Hardware Recommended

When using the Battery Monitor, it is recommended to use a 10k Ohm resistor in-line between the battery (positive) output and the monitor's (analog) input.

The monitor script can support either an ADS-1X15 monitor connected to the SDA/SCL on the Pi, or a (programmed, or "flashed") MicrController (ie, ATMEGA) serial monitor connected over USB or UART.

# Installation

First,download the library:
```
cd ~ && sudo git clone https://github.com/infinitLoop/gbz_tools.git
```

Then pick your options to install...

### Battery monitor install
```
cd ~/gbz_tools && sudo chmod 777 monitor_install.sh && sudo ./monitor_install.sh
```
To change the settings for ADC type, battery voltage levels, icon customization, etc, edit the file:
```
sudo nano ~/gbz_tools/battery_monitor.py
```
### Dedicated battery monitor (/shutdown) button  
[i] (do not install if you want to do this with a combo hotkey control) [/i]
```
cd ~/gbz_tools && sudo chmod 777 monitor_btn_install.sh && sudo ./monitor_btn_install.sh
```
To set the GPIO pin for the button control and other button settings, edit the file:
```
sudo nano ~/gbz_tools/monitor_button.py
```
### Dedicated digital volume controls
[i] (do not install if you want to do this with a combo hotkey control) [/i]
```
cd ~/gbz_tools && sudo chmod 777 volume_btn_install.sh && sudo ./volume_btn_install.sh
```
To set the GPIO pins for the button controls and other button settings, edit the file:
```
sudo nano ~/gbz_tools/volume_buttons.py
```
### Combo hotkeys
```
cd ~/gbz_tools && sudo chmod 777 combo_btn_install.sh && sudo ./combo_btn_install.sh
```
To set the GPIO pins for the button controls, enable the different controls, and other button settings, edit the file:
```
sudo nano ~/gbz_tools/combo_button.py
```
### Temperature-controlled Fan
```
cd ~/gbz_tools && sudo chmod 777 fan_install.sh && sudo ./fan_install.sh
```
To set the GPIO pins for the fan control, temperature threshold, and other settings, edit the file:
```
sudo nano ~/gbz_tools/fan.py
```
### JUJ SPI LCD Screen Driver 
[i] (for pi Zero - edit the file first for pi3/a/b/+) [/i]
```
cd ~/gbz_tools && sudo chmod 777 spi_screen_juj_install.sh && sudo ./spi_screen_juj_install.sh
```
For pi 3, edit the file prior to install:
```
sudo nano ~/gbz_tools/spi_screen_juj_install.sh
```

## Safe Shutdown
When doing Safe shutdown that is triggered via the power switch (utilizing a cicuit that will keep power active during shutdown), 
this should be added to the config.txt file for GPIO mapping.  

edit the file...
```
sudo nano /boot/config.txt
```
 with this, and update your pin numbers accordingly 
("shutdown" for the switch-shutdown trigger, and "poweroff" for the stay-alive signal):
```
dtoverlay=gpio-poweroff,gpiopin="17",active_low="y"
dtoverlay=gpio-shutdown,gpio_pin="27"
```

## Other useful software installations

### AdaFruit I2S Audio installations
```
cd ~; curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | sudo bash
```
Select [i] No [/i] at the prompt during install

### AdaFruit RetroGame GPIO Controls
```
cd ~; curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/retrogame.sh > retrogame.sh && sudo bash retrogame.sh
```
Edit the button configuration:
```
sudo nano /boot/retrogame.cfg
```
Something like...
```
UP        15  # Joypad up
DOWN      23  # Joypad down
LEFT      14  # Joypad left
RIGHT     22  # Joypad right
ENTER      5  # 'Start' button
SPACE      7  # 'Select' button
A         16  # 'A' button
B         13  # 'B' button
X          0  # 'X' button
Y          6  # 'Y' button
L          4  # Left shoulder button
R         26  # Right shoulder button
H         17  # Hotkey button
ESC      5 7  # Hold Start+Select to exit ROM
```

