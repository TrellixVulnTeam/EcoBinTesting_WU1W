def tipleft():    
    from time import sleep
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    forward = 18
    backward = 17
    GPIO.setup(forward,GPIO.OUT)
    GPIO.setup(backward,GPIO.OUT)
    GPIO.output(forward,1)
    sleep(0.3)
    GPIO.output(forward,0)
    sleep(1)
    GPIO.output(backward,1)
    sleep(0.435)
    GPIO.output(backward,0)

def tipright():
    from time import sleep
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    forward = 18
    backward = 17
    GPIO.setup(forward,GPIO.OUT)
    GPIO.setup(backward,GPIO.OUT)
    GPIO.output(backward,1)
    sleep(0.3)
    GPIO.output(backward,0)
    sleep(1)
    GPIO.output(forward,1)
    sleep(0.4)
    GPIO.output(forward,0)
    
tipleft()
