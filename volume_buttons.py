from os import system
from gpiozero import Button
from signal import pause
from time import sleep

# Location of perisitant state file
folder = "/home/pi/gbz_tools"
stateFile = "%s/volume.state" % folder

# GPIO pin configuration
volumeUpPin = 27
volumeDownPin = 1

# icon configuration
showIcon = False
iconFolder = "%s/icons" % folder
# screen location
xLocation = 650
yLocation = 10

# Initial volume setting
vState = 80
# PCM or Speaker (USB audio)
sType = "Speaker"  
# Minimum/maximum volume and how much each press adjusts
vMin = 0
vMax = 100
vStep = 10
vSpeed = 0.5  # in seconds (lower is faster)


#########

# Functions
def volumeDown():
    global vState
    vState = max(vMin, vState - vStep)
    system("amixer sset -q '" + sType  + "' " + str(vState) + "%")

def volumeUp():
    global vState
    vState = min(vMax, vState + vStep)
    system("amixer sset -q '" + sType +  "' " + str(vState) + "%")

def readData(filepath):
    with open(filepath, 'rb') as file:
        return file.read()

def writeData(filepath):
    with open(filepath, 'wb') as file:
        file.write(str(vState))

def doVolume():
    while True:
        if volumeUpBtn.is_pressed:
            volumeUp()
            writeData(stateFile)
            sleep(vSpeed)
        elif volumeDownBtn.is_pressed:
            volumeDown()
            writeData(stateFile)
            sleep(vSpeed)

#########

# Initial File Setup
try:
    vState = int(readData(stateFile))
    system("amixer sset -q '" + sType + "' " + str(vState) + "%")
except:
    writeData(stateFile)
    system("amixer sset -q '" + sType + "' " + str(vState) + "%")

# Button interupts
volumeUpBtn = Button(volumeUpPin)
volumeDownBtn = Button(volumeDownPin)

volumeUpBtn.when_pressed = doVolume
volumeDownBtn.when_pressed = doVolume

pause()
