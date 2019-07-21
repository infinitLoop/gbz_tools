from os import popen
from time import sleep
import RPi.GPIO as GPIO

# set to True to write temperature readings to screen
debug = False
# GPIO pin to trigger fan to engage
triggerPin = 4
# temperature (in C ) to turn on the fan
triggerTemp = 50


#########

# Functions
def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(triggerPin, GPIO.OUT)
    GPIO.setwarnings(False)
    return()

def getCPUTemp():
    cmd = popen('vcgencmd measure_temp').readline()
    temp = (cmd.replace("temp=","").replace("'C\n",""))
    if debug:
        print("CPU temp: {0}".format(temp))
    return float(temp)

def checkTemp():
    CPU_temp = getCPUTemp()
    if CPU_temp > triggerTemp:
        enableFan(True)
        if debug:
            print("Fan is enabled")
    else:
        enableFan(False)
        if debug:
            print("Fan is disabled")
    return()

def enableFan(isActive):
    GPIO.output(triggerPin, isActive)
    return()

#########

# initial setup
setupGPIO()
# main loop
while True:
    checkTemp()
    sleep(5)

