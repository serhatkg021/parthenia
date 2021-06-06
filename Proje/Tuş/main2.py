import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup("1",GPIO.IN)
GPIO.setup("2",GPIO.IN)

input = GPIO.input("1")
input = GPIO.input("2")


while True:
        inputValue = GPIO.input("1")
        if (inputValue == False):
            print("1. Görev")
            os.system('..\\daire\\main.py') # Daha verimli
        # if keyboard.is_pressed("2"):
        #     os.system('..\\dikdörtgen\\main.py') # Daha verimli
        # if keyboard.is_pressed("3"):
        #     print("3. Görev")
        #     # os.startfile('..\\daire\\main.py')