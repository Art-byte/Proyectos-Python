import numpy as np
import cv2

img = cv2.imread("Flash.jpg",0)
cv2.imshow("Flash.jpg",img)
cv2.waitKey()
cv2.destroyAllWindows()

