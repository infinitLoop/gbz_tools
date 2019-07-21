#!/usr/bin/env python2.7

from gpiozero import Button
from signal import pause
from subprocess import check_call
from os import system
from time import sleep
import wiringpi
import pickle

## Set the GPIO Pins for the button presses
hotkeyPin = 17
volumeUpPin = 27
volumeDownPin = 1
brightnessUpPin = 15
brightnessDownPin = 23
ledLightPin = 12
wifiPin = 4
bluetoothPin = 26
shutdownPin = 14
monitorPin = 7

## Set the Combos to enable
doVolume = False
doBrightness = True
doShutdown = False
doMonitor = True
doBluetooth = True
doWifi = True

# True will cycle through brightness setttings at startup
doBrightnessStartupCheck = True

# Folder and file locations
folder = "/home/pi/gbz_tools"
stateFile = "%s/combo.state" % folder
batteryMonitor = "%s/battery_monitor.py" % folder
pngView = "%s/Pngview/pngview2" % folder
iconFolder = "%s/icons" % folder

## VOLUME SETTINGS
# Initial volume setting
vState = 80
# PCM or Speaker (USB audio)
sType = "PCM"  
# Minimum/maximum volume and how much each press adjusts
vMin = 0
vMax = 100
vStep = 10  # used for icons too, so if changed, other icons need to be set up
vSpeed = 1  # in seconds (lower is faster)

## Brightness settings
bMin = 0 
bMax = 256 # 256 for led bulb, 1024 for screen backlight
bStep = 16  # amount to adjust each time
bIsScreenBacklight = False

# in seconds, how long to show icons on button press
displayTime = 3


#########

# Functions
def brightnessUp():
    if brightnessUpBtn.is_pressed:
        comboStates['brightness'] = min(bMax, int(comboStates['brightness']) + bStep)
        controlBrightness()

def brightnessDown():
    if brightnessDownBtn.is_pressed:
        comboStates['brightness'] = max(bMin, int(comboStates['brightness']) - bStep)
        controlBrightness()

def controlBrightness():
    wiringpi.pwmWrite(ledLightPin, comboStates['brightness'])
    sleep(.2)

def volumeDown():
    comboStates['volume'] = max(vMin, int(comboStates['volume']) - vStep)
    system("amixer sset -q '" + sType  + "' " + str(comboStates['volume']) + "%")

def volumeUp():
    comboStates['volume'] = min(vMax, int(comboStates['volume']) + vStep)
    system("amixer sset -q '" + sType +  "' " + str(comboStates['volume']) + "%")

def controlVolume():
    while True:
        killPngview()
        if volumeUpBtn.is_pressed:
            volumeUp()
        elif volumeDownBtn.is_pressed:
            volumeDown()
        writeData(stateFile)
        system(pngView + " -b 0 -l 999999 " + iconFolder + "/Volume" + str(comboStates['volume']) + ".png &")
        sleep(vSpeed)
    killPngview()

def toggleWifi():
    if comboStates['wifi'] == 1:
        system("sudo rfkill block wifi")
        system(pngView + " -b 0 -l 999999 " + iconFolder + "/wifiOff.png &")
        comboStates['wifi'] = 0
    else:
        system("sudo rfkill unblock wifi")
        system(pngView + " -b 0 -l 999999 " + iconFolder + "/wifiOn.png &")
        comboStates['wifi'] = 1
    sleep(displayTime)
    killPngview()

def toggleBluetooth():
    if comboStates['bluetooth'] == 1:
        system("sudo rfkill block bluetooth")
        system(pngView + " -b 0 -l 999999 " + iconFolder + "/bluetoothOff.png &")
        comboStates['bluetooth'] = 0
    else:
        system("sudo rfkill unblock bluetooth")
        system(pngView + " -b 0 -l 999999 " + iconFolder + "/bluetoothOn.png &")
        comboStates['bluetooth'] = 1
    sleep(displayTime)
    killPngview()

def shutdown():
    ## delay to show shutdown message
    for i in range(1, displayTime):
        system(pngView + " -b 0 -l 999999 " + iconFolder + "/shutdown.png &")
        sleep(1)
        killPngview()
        sleep(.5)
    check_call(['sudo', 'poweroff'])

def toggleMonitorIcon():
    # toggle state
    if comboStates['battery'] == 1:
        comboStates['battery'] = 0
    else:
        comboStates['battery'] = 1
    # kill the current monitor
    system("sudo pkill -f \"python " + batteryMonitor + "\"")
    # write new state
    writeData(stateFile)
    # reload monitor
    sleep(REFRESH_RATE/2)
    system("python " + batteryMonitor + " &")
    sleep(REFRESH_RATE/2)

def killPngview():
    system("sudo killall -q -15 pngview2")

def readData(filepath):
    with open(filepath, 'rb') as file:
        return pickle.load(file)

def writeData(filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(comboStates, file)

def checkFunction():
    while hotkeyBtn.is_pressed:
        if doBrightness and brightnessUpBtn.is_pressed:
            brightnessUp()
        elif doBrightness and brightnessDownBtn.is_pressed:
            brightnessDown()
        elif doVolume and (volumeUpBtn.is_pressed or volumeDownBtn.is_pressed):
            controlVolume()
        elif doShutdown and shutdownBtn.is_pressed:
            shutdown()
        elif doMonitor and monitorBtn.is_pressed:
            toggleMonitorIcon()
        elif doWifi and wifiBtn.is_pressed:
            toggleWifi()
        elif doBluetooth and bluetoothBtn.is_pressed:
            toggleBluetooth()

#########

# setting up buttons from pins 
hotkeyBtn = Button(hotkeyPin)
brightnessUpBtn = Button(brightnessUpPin)
brightnessDownBtn = Button(brightnessDownPin)
volumeUpBtn = Button(volumeUpPin)
volumeDownBtn = Button(volumeDownPin)
shutdownBtn = Button(shutdownPin)
monitorBtn = Button(monitorPin)
wifiBtn = Button(wifiPin)
bluetoothBtn = Button(bluetoothPin)

# initial state values
comboStates = {'wifi': 1, 'bluetooth': 1, 'volume': vState, 'brightness': bMax, 'battery': 1}

# Initial File Setup
try:
    comboStates = readData(stateFile)
except:
    writeData(stateFile)
finally:
    if doBrightness:
        wiringpi.wiringPiSetup()
        wiringpi.pinMode(ledLightPin, 2)
        if doBrightnessStartupCheck:
            for i in range(0,(bMax/bStep)):
                wiringpi.pwmWrite(ledLightPin, (i * bStep))
                sleep(.2)
        controlBrightness()
    if doVolume:
        controlVolume()
    if doWifi:
        if comboStates['wifi'] == 1:
            system("sudo rfkill unblock wifi")
        else:
            system("sudo rfkill block wifi")
    if doBluetooth:
        if comboStates['bluetooth'] == 1:
            system("sudo rfkill unblock bluetooth")
        else:
            system("sudo rfkill block bluetooth")

#  Button Interrupt
hotkeyBtn.when_pressed = checkFunction
pause()