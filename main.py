import pygame
import random

###inicializando la libreria###
pygame.init()

####configurar pantalla####
size=(500,500)
pantalla=pygame.display.set_mode(size)

####Configuración del Reloj####
reloj=pygame.time.Clock()

#####configuración de Colores####
#r= Red,  g=Green, b=Blue
negro=(0,0,0)
rojo=(255,0,0)
azul=(0,0,255)
verde=(0,255,0)
blanco=(255,255,255)
gris=(60,60,60)
color=(0,0,255)

####variable para controlar el juego#####
juego=True

#####VARIABLES DE CONTROL#####
x=100
y=100
velocidadX=10
velocidadY=10
puntos=0
nivel=1
tiempo=80
contador=tiempo

#####configurando los tipos de letras####
letra=pygame.font.Font(None,60)

#######configurar el fondo#########
#fondo=pygame.image.load("fondo.jpg")

####Para mantener la ventana abierta#####
while juego:
    ##### Para controlar los eventos#####
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            juego=False

        ######control del mouse######
        if event.type==pygame.MOUSEBUTTONDOWN:
            if x-50<=event.pos[0]<=x+50:
                if y-50<=event.pos[1]<=y+50:
                    x=random.randrange(50,750)
                    y=random.randrange(50,550)
                    contador=tiempo
                    nivel=nivel+1
                    color=(random.randrange(0,250), random.randrange(0,250) ,random.randrange(0,250))


    #######controles del tiempo#####
    contador=contador-1
    if contador==0:
        juego=False



    #####Desliegue de la pantalla#####
    pantalla.fill(color)
    #pantalla.blit(fondo,(0,0))

    pygame.draw.circle(pantalla,blanco,(x,y),50)

    x=x+velocidadX
    if x>=800:
        velocidadX=-10
    if x<=0:
        velocidadX=+10

    y=y+velocidadY
    if y>=600:
        velocidadY=-10
    if y<=0:
        velocidadY=+10



    #######DESPLEGAR EL TEXTO DENTRO DEL JUEGO########
    mensaje=letra.render("Nivel: "+str(nivel),1,blanco) ##texto se convirtio en una imagen
    pantalla.blit(mensaje,(10,20)) #mostrar una imagen

    mensaje=letra.render("Tiempo: "+str(contador),1,blanco)
    pantalla.blit(mensaje,(500,20))

    #################FIN DE TEXTO########################

    pygame.display.update()
    reloj.tick(30)

pygame.quit()