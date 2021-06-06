import cv2
# import numpy as np
import keyboard
import os

cameraX = 800
cameraY = 600

cap = cv2.VideoCapture(0)

while(True):
    if keyboard.is_pressed("1"):
        print("1. Görev Dikdortgende")
        cap.release()
        cv2.destroyAllWindows()
        os.system('..\\daire\\main.py') # Daha verimli
        break
    if keyboard.is_pressed("3"):
        print("3. Görev Dikdortgende")
        break

    ret, image = cap.read()
    image = cv2.resize(image, (cameraX, cameraY))
    original = image.copy()
    cv2.rectangle(original, (395, 295),
                (405, 305), (0, 128, 50), -1)
    blurred = cv2.medianBlur(image, 3)
    # blurred = cv2.GaussianBlur(hsv,(3,3),0)

    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,(15,0,0), (29, 255, 255))
    cnts,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    minArea = []
    minC = []
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 400:
            approx = cv2.approxPolyDP(c, 0.125 * cv2.arcLength(c, True), True)
            if(len(approx) == 4): 
                minArea.append(area)
                minC.append([area, c])
    if minArea:
        minArea.sort()
        print(minArea)
        mArea = minArea[0]
        mC = []
        for x in minC:
            if x[0] == mArea:
                mC = x[1]
        
        M = cv2.moments(mC)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        x = cx - cameraX/2
        y = (cy - cameraY/2) * -1
        print(cx, cy  , x , y)
        cv2.rectangle(original, (cx - 5, cy - 5),
                    (cx + 5, cy + 5), (0, 128, 255), -1)
        cv2.drawContours(original, [approx], 0, (0, 0, 255), 5)
        
    cv2.imshow('mask', mask)
    cv2.imshow('original', original)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break
    
cv2.destroyAllWindows()