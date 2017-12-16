import RPi.GPIO as GPIO
import time
import os
import sys
TouchPin = 27
button = 22
timeout = time.time() + 5
def setup():
        GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
        GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(17,GPIO.OUT)
        GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
def loop():
        print("s")
        while True:                
                inputval = GPIO.input(button)
                if(time.time()>timeout):
                        GPIO.output(17,GPIO.LOW)
                        break
                elif(inputval==True):
                        GPIO.output(17,GPIO.LOW)
                        print('c')
                        break                    
                          
                
			

def destroy():
        GPIO.output(17, GPIO.LOW)     # led off
if __name__ == "__main__":     # Program start from here
        setup()
        try:
                while True:
                        if(GPIO.input(TouchPin) == GPIO.HIGH):
                                print 'T'
                                GPIO.output(17,GPIO.HIGH)
                                loop()
		
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                destroy()
