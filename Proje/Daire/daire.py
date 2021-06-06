import cv2
import numpy as np

# minDist = 120
# param1 = 50 
# param2 = 30
# minRadius = 5
# maxRadius = 0

def circleScan(frame, camX, camY):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray,(11,11),0)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1,120, param1=220, param2=30, minRadius=50, maxRadius=300)

    # circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(frame, (x - 5, y - 5),
                        (x + 5, y + 5), (0, 128, 255), -1)
            x = x - camX/2
            y = y - camY/2
            return [x,y]



# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
