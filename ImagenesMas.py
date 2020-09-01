import numpy as pd
import cv2

img = cv2.imread('Flash.jpg',0)
cv2.imshow('Flash.jpg',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows ()
elif k == ord('s'):
    cv2.imwrite('Flash.jpg',img)
    cv2.destroyAllWindows()
    cv2.imShow('Flash.jpg',img)