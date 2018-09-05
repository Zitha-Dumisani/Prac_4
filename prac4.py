import RPi.GPIO as gpio
import time
import os
import spidev
import math

gpio.setmode(gpio.BCM)

freq=0
ic=0
freqs=[0.5,1,2]
inTime=time.time()
bON=True
potVal=0,lightVal=0,tempVal=0
ic=0
sList=["","","","",""]

#setup switches
bStop=gpio.setup(21,gpio.IN,pull_up_down=gpio.PUD_UP)
bReset=gpio.setup(20,gpio.IN,pull_up_down=gpio.PUD_UP)
bFreq=gpio.setup(16,gpio.IN,pull_up_down=gpio.PUD_UP)
bDisplay=gpio.setup(12,gpio.IN,pull_up_down=gpio.PUD_UP)

#button code
def reset(channel):
    inTime=time.time()
    bON=True
    os.system('cls')

def freq(channel):
    freq=(freq+1)%3

def stop(channel):
    if bON:
        bON=False
        sList=["","","","",""]
        ic=0
    else:
        bON=True

def display(channel):
    for i in range(0,5):
        print(sList[i])
    time.sleep(2)

#button interupts
gpio.add_event_detect(21,gpio.RISING,callback=stop,bouncetime=100)
gpio.add_event_detect(20,gpio.RISING,callback=reset,bouncetime=100)
gpio.add_event_detect(16,gpio.RISING,callback=freq,bouncetime=100)
gpio.add_event_detect(12,gpio.RISING,callback=display,bouncetime=100)

#create spi
spi=spidev.SpiDev()
spi.open(0,0)

def readADC(channel):

def tempVal():
    i=readADC(1)

    return 0
    
def potVal():
    i=readADC(2)

    return 

def lightVal():
    i=readADC(3)

    return 0


#default loop
try:
    while True:
        if bON:
            s=(time.time()+" "+(time.time()-inTime)+potVal()+"V "+tempVal()+"C "+lightVal()+"%")
            print(s)
            if ic<5:
                sList[ic]=s
            ic=ic+1
        time.sleep(freq)

except KeyboardInterrupt:
    spi.close()
    gpio.remove_event_detect(12)
    gpio.remove_event_detect(16)
    gpio.remove_event_detect(20)
    gpio.remove_event_detect(21)
    gpio.cleanup()