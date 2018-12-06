def go():
    from time import sleep
    import RPi.GPIO as GPIO
	
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    forward = 18
    backward = 17

    GPIO.setup(forward,GPIO.OUT)
    GPIO.setup(backward,GPIO.OUT)
    print("TURNING")
    GPIO.output(backward,1)
    sleep(1)
    GPIO.output(backward,0)
    GPIO.output(forward,1)
    sleep(1)
    GPIO.output(forward,0)

go()
