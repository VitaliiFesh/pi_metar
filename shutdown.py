import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def Shutdown(channel):
    print('Shutting Down')
    time.sleep(5)
    os.system('sudo shutdown -h now')
    
def Reboot(channel):
    print('Rebooting')
    time.sleep(15)
    os.system('sudo reboot')
    
GPIO.add_event_detect(21, GPIO.FALLING, callback=Reboot, bouncetime=2000)

while 1:
    time.sleep(1)