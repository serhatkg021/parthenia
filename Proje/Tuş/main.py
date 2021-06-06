import keyboard
import os

while True:
    if keyboard.is_pressed("1"):
        print("1. Görev")
        os.system('..\\daire\\main.py')
    if keyboard.is_pressed("2"):
        os.system('..\\dikdörtgen\\main.py')
    if keyboard.is_pressed("3"):
        print("3. Görev")