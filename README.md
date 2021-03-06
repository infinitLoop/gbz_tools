# Game Boy Zero Tools

This collection is intended to help add customizations to Raspberry-Pi-based retro handhelds, or other projects.  
It can support "safe" software shutdown, an on-screen battery monitor with customizable colors and placement, 
temperature-controlled fan, volume control, combo button controls and/or purpose-based buttons, 
as well as brightness control for LEDs or screen backlighting, and more.

Credit to HoolyHoo, whose GBZ and MintyPi projects were the basis of much of this: https://raw.github.com/HoolyHoo/

OSD controls are from  https://github.com/vascofazza/Retropie-open-OSD

### Hardware Notes

When using the Battery Monitor, it is recommended to use a 10k Ohm resistor in-line between the battery (positive) output and the monitor's (analog) input, 
and that you cut the battery power to the monitor when not in use by running the connection through a DPDT switch, to prevent power leakage.

The monitor script can support either an ADS-1X15 monitor connected to the SDA/SCL on the Pi, or a (programmed, or "flashed") MicrController (ie, ATMEGA) 
serial monitor connected over USB or UART.


Connecting via Microcontroller should look the same as these for the battery and power, but you would connect via USB or UART instead of the SDA/SCL to the pi.

<i>AdaFruit Powerboost 1000C Example (or any PSU that uses an [En]gage pin):</i>
![powerboost_example](/images/powerboost_battery_monitor_example.png)

<i>Generic Power Supply example (the difference being that the main power flow is also cut off at the DPDT switch):</i>
![generic_example](/images/generic_battery_monitor_example.png)


For the fan controls, you should use an NPN transistor (example: S8050) that is connected with the middle/positive lead to the GPIO pin you wish to use, 
and the two Ground leads to the fan's Ground/negative, and to a Ground on the GPIO, respectively.
![fan_example](/images/fan.png)

# Installation

First,download the library:
```
cd ~ && sudo git clone https://github.com/infinitLoop/gbz_tools.git
```
Then pick your options to install...

### Battery monitor install
```

sudo chmod 777 ~/gbz_tools/monitor_install.sh && sudo ~/gbz_tools/./monitor_install.sh

```
To change the settings for ADC type, battery voltage levels, icon customization, etc, edit the file:
```

sudo nano ~/gbz_tools/battery_monitor.py

```

### Dedicated battery monitor (/shutdown) button  
<i> (do not install if you want to do this with a combo hotkey control) </i>
```
sudo chmod 777 ~/gbz_tools/monitor_btn_install.sh && sudo ~/gbz_tools/./monitor_btn_install.sh
```
To set the GPIO pin for the button control and other button settings, edit the file:
```
sudo nano ~/gbz_tools/monitor_button.py
```

### Dedicated digital volume controls
<i> (do not install if you want to do this with a combo hotkey control) </i>
```
sudo chmod 777 ~/gbz_tools/volume_btn_install.sh && sudo ~/gbz_tools/./volume_btn_install.sh
```
To set the GPIO pins for the button controls and other button settings, edit the file:
```
sudo nano ~/gbz_tools/volume_buttons.py
```

### Combo hotkeys
Options include: Battery Monitor toggle, Digital Volume, Safe Shutdown, Brightness (Screen or LED), Bluetooth toggle, Wifi toggle, and On-screen informational readout 
```

sudo chmod 777 ~/gbz_tools/combo_btn_install.sh && sudo ~/gbz_tools/./combo_btn_install.sh

```
To set the GPIO pins for the button controls, enable the different controls, as wel as other button settings, edit the file:
```

sudo nano ~/gbz_tools/combo_button.py

```

### Temperature-controlled Fan
```

sudo chmod 777 ~/gbz_tools/fan_install.sh && sudo ~/gbz_tools/./fan_install.sh

```
To set the GPIO pins for the fan control, temperature threshold, and other settings, edit the file:
```

sudo nano ~/gbz_tools/fan.py

```
### ILI9341 SPI LCD Screen Driver 
<i> (this is set up for pi Zero - for pi3/a/b/+, edit the file before executing) </i>
```

sudo chmod 777 ~/gbz_tools/spi_screen_juj_install.sh && sudo ~/gbz_tools/./spi_screen_juj_install.sh

```
For pi3, edit the file prior to install:
```

sudo nano ~/gbz_tools/spi_screen_juj_install.sh

```

## Safe Shutdown
When doing safe shutdown that is triggered via the power switch (utilizing a circuit that will keep power active during the software shutdown), 
this should be added to the config.txt file for GPIO mapping, instead of using the button triggers above.

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
NOTE: If using RetroPie 4.3 or older, the overlay for "gpio-shutdown" may not be installed. it can be installed (instructions can be found in the first post here: 
https://sudomod.com/forum/viewtopic.php?f=43&t=8054 ), but an easier way is to use the shutdown script above, and leave the "gpio-shutdown" overlay
out of the config.txt.  You will still need to use the "gpio-poweroff" overlay to signal to the power supply to stay active during the software shutdown.


## Other useful software installations

### AdaFruit I2S Audio installations
```

cd ~; curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | sudo bash

```
Select <i> No </i> at the prompt during install, for the background process

to fix splashscreen video, run one of these:
```

## RetroPie 4.3-

sudo sed -i 's/omxplayer -o both -b --layer 10000/omxplayer -o alsa -b --layer 10000/g' /opt/retropie/supplementary/splashscreen/asplashscreen.sh

## RetroPie 4.4+

sudo sed -i 's/omxplayer -o both -b --layer 10000/omxplayer -o alsa -b --layer 10000/g' /etc/init.d/asplashscreen
   
```

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

## Screen Tip
For Small Screen sizing (320x240) on SPI, try this.

Edit the file:
```

sudo nano /boot/config.txt

```
Add in:
```

disable_overscan=1
overscan_scale=1

overscan_left=0
overscan_right=0
overscan_top=0
overscan_bottom=0

framebuffer_width=320
framebuffer_height=240

# 320x240 60hz 4:3, no margins, progressive
hdmi_cvt=320 240 60 1 0 0 0
hdmi_mode=87
hdmi_group=2

```

## PWM Audio
When using stero PWM audio, these settings work well.

Edit the file:
```
sudo nano /boot/config.txt
```
Add this in (change GPIO pins if use Alt PWM):
```
dtparam=audio=on
disable_audio_dither=1
audio_pwm_mode=0
##stereo
dtoverlay=pwm-2chan,pin=18,func=2,pin2=13,func2=4
##mono
#dtoverlay=pwm,pin=18,func=2
##alt mono
#dtoverlay=pwm,pin=13,func=4

```
