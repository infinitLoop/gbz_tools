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

Download the library:
```
cd ~; sudo git clone https://github.com/InfinitLoop/gbz_tools.git
```