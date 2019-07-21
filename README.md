# Game-Boy-Zero-Tools

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

Install the battery monitor
```
cd ~/gbz_tools && sudo chmod 777 monitor_install.sh && sudo ./monitor_install.sh
```
Install the dedicated battery monitor (/shutdown) hotkey  (do not install if you want to do this with a combo hotkey control)
```
cd ~/gbz_tools && sudo chmod 777 monitor_btn_install.sh && sudo ./monitor_btn_install.sh
```
Install the dedicated digital volume controls (do not install if you want to do this with a combo hotkey control)
```
cd ~/gbz_tools && sudo chmod 777 volume_btn_install.sh && sudo ./volume_btn_install.sh
```
Install the combo hotkeys
```
cd ~/gbz_tools && sudo chmod 777 combo_btn_install.sh && sudo ./combo_btn_install.sh
```
Install the fan controls
```
cd ~/gbz_tools && sudo chmod 777 fan_install.sh && sudo ./fan_install.sh
```
Install the JUJ SPI Driver (for rPi Zero)
```
cd ~/gbz_tools && sudo chmod 777 spi_screen_juj_install.sh && sudo ./spi_screen_juj_install.sh
```
