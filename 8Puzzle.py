# -- coding: utf-8 --
import sys
class operaciones():
    
    def validarPos(self,m):
        if m[0][0]!=1:
            orden = False
            return orden
        elif m[0][1]!=2:
            orden = False
            return orden
        elif m[0][2]!=3:
            orden = False
            return orden
        elif m[1][0]!=4:
            orden = False
            return orden
        elif m[1][1]!=5:
            orden = False
            return orden
        elif m[1][2]!=6:
            orden = False
            return orden
        elif m[2][0]!=7:
            orden = False
            return orden
        elif m[2][1]!=8:
            orden = False
            return orden
        elif m[2][2]!=0:
            orden = False
            return orden
    def up(self,m,k,j):
        m1=m
        m1[k][j]=m[k-1][j]
        m1[k-1][j]=0
        return m1
    def r(self,m,k,j):
        m1=m
        m1[k][j]=m[k][j+1]
        m1[k][j+1]=0
        return m1
    def l(self,m,k,j):
        m1=m
        m1[k][j]=m[k][j-1]
        m1[k][j-1]=0
        return m1
    def down(self,m,k,j):
        m1=m
        m1[k][j]=m[k+1][j]
        m1[k+1][j]=0
        return m1
          
    def posZero(self,m):
        for k in range(3):
            for j in range(3):

            #abs
                if m[k][j] == 0 :
                    #print ('x:'+str(k)+' y:'+str(j)) MANDAR A llamr funcion con movimientos
                    if k>0 : #necesitas validar si ya esta en la pos
                        move = operaciones().up(m,k,j)
                        m = move
                        #return m
                    elif j<2 :
                        move = operaciones().r(m,k,j)
                        m = move
                    elif j>0 :
                        move = operaciones().l(m,k,j)
                        m = move
                    elif k<2 :
                        move = operaciones().down(m,k,j)
                        m = move
                    return k,j,m
    def imprimir(self,m):
        a=""
        for k in range(3):
            for j in range(3):
                a+=str(m[k][j])+'\t'
             
            print(a)
        
            a=""



class Main():
    orden=True
    m=[[2,3,6],
    [4,5,0],
    [7,1,8]]

    a=""
    contador=0

    obj=operaciones()
    orden = obj.validarPos(m)

    

    for k in range(3):
        for j in range(3):
            #abs
            
            a+=str(m[k][j])+'\t'
             
        print(a)
        
        a=""
    #pos=obj.posZero(m)
    k,j,m=obj.posZero(m)
    #print (pos)
    #print(x)
    #print(y)   
    print('-------------------------')
    obj.imprimir(m)
    while(orden == False):
        contador = contador + 1
        k,j,m=obj.posZero(m)
        orden = obj.validarPos(m)
        print(contador)
            #contador = contador + 1
        print('-------------------------')
        obj.imprimir(m)


    print (orden)