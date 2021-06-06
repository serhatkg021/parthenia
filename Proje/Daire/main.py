import cv2
from daire import circleScan
import keyboard
import os

cameraX = 800
cameraY = 600

cap = cv2.VideoCapture(0)
# Cemberin merkezinin ekranın orta noktaya uzaklıgını x ve y cinsinden uzaklıgı 
while True:
    if keyboard.is_pressed("2"):
        print("2. Görev")
        cap.release()
        cv2.destroyAllWindows()
        os.system('..\\dikdörtgen\\main.py') # Daha verimli
        break
    if keyboard.is_pressed("3"):
        cap.release()
        cv2.destroyAllWindows()
        print("3. Görev")
        break
    
    ret, frame = cap.read()
    frame = cv2.resize(frame, (cameraX, cameraY))
    data = circleScan(frame, cameraX, cameraY)
    if data is not None:
        print("X : " ,data[0] , "  Y : " , data[1])

    cv2.imshow("output", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()