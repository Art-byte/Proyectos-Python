#Segundo examen parcial: José Arturo Pedraza Bonilla 
import cv2
import numpy as np

gauss = 3
kernel = 9

imagen1 = cv2.imread('C:/Users/Artur/Desktop/Examen2do/Imagen2.jpg')
cv2.imshow('Imagenen', imagen1)

grises = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
cv2.imshow("gris",grises)

gauss = cv2.GaussianBlur(grises, (gauss,gauss),0)
cv2.imshow("Gauss",gauss)

canny = cv2.Canny(gauss,50,200)
cv2.imshow("canny", canny)

#Eliminar las cosas inecesarias 
kernels = np.ones((kernel,kernel), np.uint8)
cerrar = cv2.morphologyEx(canny,cv2.MORPH_CLOSE, kernels)
cv2.imshow("cerrado",cerrar)

(contornos, hierachy) = cv2.findContours(cerrar.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print("Cantidad de Monedas: {}".format(len(contornos)))

cv2.drawContours(imagen1,contornos,-1,(0,0,255),2)
cv2.imshow("Contornos", imagen1)

cv2.waitKey()
