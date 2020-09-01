import cv2
import numpy as np

cap = cv2.VideoCapture(0)

redBajo1 = np.array([0,100,20], np.uint8)
redAlto1 = np.array([8,255,255],np.uint8)

redBajo2 = np.array([176,100,20], np.uint8)
redAlto2 = np.array([179,255,255], np.uint8)

while True:
    ret, frame = cap.read()
    if ret == True:
        frameHVS = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
        maskRed1 = cv2.inRange(frameHVS, redBajo1, redAlto1)
        maskRed2 = cv2.inRange(frameHVS, redBajo2, redAlto2)
        
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) and 0xFF == ord("s"):
            break
        
cap.release()
cv2.destroyAllWindows()
    