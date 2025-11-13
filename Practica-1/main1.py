import pygame
import sys
 
pygame.init()

#pantalla = pygame.display.set_mode((600, 400))
# Vamos a cambiar el modo de presentar la pantalla por medio de nombres independientes para posteriormente hacer colisión
anchoVentana = 600
altoVentana = 400
pantalla = pygame.display.set_mode((anchoVentana, altoVentana))
pygame.display.set_caption("Práctica 1 - Movimiento básico")

#x, y = 300, 200
# Se agregan las dimensiones para el personaje con respecto a la pantalla
personajeAncho = 50
personajeAlto = 50
x = anchoVentana // 2 - personajeAncho // 2
y = altoVentana // 2 - personajeAlto // 2

vel = 5
#Se agregan las variables de velocidad turbo rapidita y la velocidad como 'vel' normal
velTurbo = 10
velocidad = vel

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    teclas = pygame.key.get_pressed()

    #Se agrega el comando de teclado para shift y avance más rápidito
    if teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]:
        velocidad = velTurbo
    else:
        velocidad = vel

    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad


    #Estas son delimitaciones creadas de acuerdo al tamaño de la pantalla y del personaje
    if x < 0:
        x = 0
    if x + personajeAncho > anchoVentana:
        x = anchoVentana - personajeAncho
    if y < 0:
        y = 0
    if y + personajeAlto > altoVentana:
        y = altoVentana - personajeAlto    


    pantalla.fill((30, 30, 30))
    #Para el cambio de color, hay que cambiar el tono en RGB, en este caso lo puse rosa
    pygame.draw.rect(pantalla, (255, 100, 200), (x, y, 40, 40))
    pygame.display.update()

pygame.quit()
