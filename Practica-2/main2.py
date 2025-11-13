import pygame
import sys
pygame.init() 

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 2 - Doble Salto Fluido")

# cubo del personaje
x, y = 300, 300
vel_y = 0
gravedad = 0.5  # gravedad más suave
saltos = 0      # contador de saltos

# rectángulo del suelo
suelo_y = 340   # altura del suelo 
alto_suelo = 60 # grosor del suelo


clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Detecta salto solo cuando se presiona una vez la barra espaciadora
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and saltos < 2:
                if saltos == 0:
                    vel_y = -10   # primer salto fuerte
                else:
                    vel_y = -8    # segundo salto más corto
                saltos += 1

    # Movimiento del cubo personaje
    y += vel_y
    vel_y += gravedad

    # Detectar suelo
    if y >= suelo_y - 40:   # 40 = altura del cuadrado
        y = suelo_y - 40
        vel_y = 0
        saltos = 0 # reinicia el contador de saltos

    # Dibujar pantalla
    pantalla.fill((50, 50, 100))

    # Dibuja el suelo (rectángulo verde)
    pygame.draw.rect(pantalla, (0, 200, 0), (0, suelo_y, 600, alto_suelo))
    
    # Cambia color si está en segundo salto
    color = (255, 255, 0) if saltos <= 1 else (255, 150, 0)
    pygame.draw.rect(pantalla, color, (x, y, 40, 40))
    
    pygame.display.update()

pygame.quit()
