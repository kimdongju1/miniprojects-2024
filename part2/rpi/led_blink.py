# led_blink.py
# Red led 
import RPi.GPIO as GPIO
import time 

# RGB LED 핀번호 셋팅
red_pin = 4
green_pin = 6
blue_pin = 5

GPIO.setmode(GPIO.BCM) # GPIO.BOARD(1~40) 잘 안씀
GPIO.setup(red_pin, GPIO.OUT) # 4번핀으로 출력 
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

try:
    while(True):
        GPIO.output(red_pin, False)
        GPIO.output(green_pin, False)
        GPIO.output(blue_pin, False)
        time.sleep(1) # 1초가 기본, 0.5초 // R

        GPIO.output(red_pin, False)
        GPIO.output(green_pin, True)
        GPIO.output(blue_pin, False)
        time.sleep(0.5) # 1초가 기본, 0.5초 // G

        GPIO.output(red_pin, False)
        GPIO.output(green_pin, False)
        GPIO.output(blue_pin, True)
        time.sleep(0.5) # 1초가 기본, 0.5초 // B

        GPIO.output(red_pin, True)
        GPIO.output(green_pin, True)
        GPIO.output(blue_pin, True)
        time.sleep(0.5) # 1초가 기본, 0.5초 // White
        
except KeyboardInterrupt:
    GPIO.cleanup



