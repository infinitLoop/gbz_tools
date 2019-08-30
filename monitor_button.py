from gpiozero import Button
from subprocess import check_call
from signal import pause
from os import system
from time import sleep

# GPIO Pin for button trigger to hide battery monitor icon
monitorPin = 7

# Set to True to hold button for X seconds to show/hide icon
##    False will make button act on release
monitorButtonHold = True 
monitorHoldTime = 1 # in seconds

# Set to True to use the same button for Safe Shutdown
# Set to False to use shutdown_button.py for a different button 
###   or to only toggle icon with the button and not do shutdown
doShutdown = False
shutdownHoldTime = 3  # in seconds

# Folder and file locations
folder = "/home/pi/gbz_tools"
stateFile = "%s/monitor_icon.state" % folder
batteryMonitor = "%s/battery_monitor.py" % folder

# giving it a little delay when changing state
REFRESH_RATE = 1


#########

# Functions
def shutdown():
    check_call(['sudo', 'poweroff'])

def toggleIcon():
    # toggle state
    global showIcon
    showIcon = (not showIcon)
    # kill the current monitor
    system("sudo pkill -f \"python " + batteryMonitor + "\"")
    # write new state
    with open(stateFile, 'w') as f:
        f.write(str(showIcon))
    # reload monitor
    sleep((REFRESH_RATE/2))
    system("python " + batteryMonitor + " &")
    sleep((REFRESH_RATE/2))

#########
# initial setup
# read showIcon toggle file
try:
    with open(stateFile, 'r') as f:
        showIcon = (f.read() == "True")
except IOError:
    showIcon = True

# button interrupts
if monitorButtonHold:
    monitorButton = Button(monitorPin, hold_time = monitorHoldTime)
    monitorButton.when_held = toggleIcon()
else:
    monitorButton = Button(monitorPin)
    monitorButton.when_released = toggleIcon()
 
if doShutdown:
    shutdownButton = Button(monitorPin, hold_time = shutdownHoldTime)
    shutdownButton.when_held = shutdown()
    
pause()

