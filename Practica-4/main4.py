import pygame
import random
pygame.init()

#Música de fondo
pygame.mixer.music.load("Dance-Space.mp3")
pygame.mixer.music.play(-1)

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 4 - Colisiones con Puntaje")

#Sonidos
sonido_shot = pygame.mixer.Sound("shot.wav")
sonido_hit = pygame.mixer.Sound("hit.wav")

#Jugador
jugador = pygame.Rect(50, 200, 40, 40)

#Balas y enemigos
balas = []
enemigos = [pygame.Rect(500, 300, 40, 40)]

#Puntuación 
puntuacion = 0
fuente = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

def mover_enemigo(e):
    """Coloca al enemigo en una nueva posición aleatoria sin encimarse."""
    while True:
        nuevo_x = random.randint(300, 550)
        nuevo_y = random.randint(20, 350)
        nuevo_rect = pygame.Rect(nuevo_x, nuevo_y, 40, 40)

        encimado = False  
        for b in balas:
            if nuevo_rect.colliderect(b):
                encimado = True

        if not encimado:
            e.x = nuevo_x
            e.y = nuevo_y
            break

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Disparo
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            balas.append(pygame.Rect(jugador.x + 40, jugador.y + 15, 10, 5))
            sonido_shot.play()

    # Movimiento jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and jugador.y > 10:
        jugador.y -= 5
    if teclas[pygame.K_DOWN] and jugador.y < 350:
        jugador.y += 5

    # Movimiento balas
    for b in balas:
        b.x += 10

    balas = [b for b in balas if b.x < 600]

    # Colisiones
    for b in balas[:]:
        for e in enemigos[:]:
            if b.colliderect(e):
                balas.remove(b)
                sonido_hit.play()

                # Sumar puntos
                puntuacion += 10

                mover_enemigo(e)

    pantalla.fill((0, 0, 0))
    pygame.draw.rect(pantalla, (0, 255, 0), jugador)

    for b in balas:
        pygame.draw.rect(pantalla, (255, 255, 0), b)

    for e in enemigos:
        pygame.draw.rect(pantalla, (255, 0, 0), e)

    # Mostrar puntuación
    texto = fuente.render(f"Puntos: {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))

    pygame.display.update()

pygame.quit()
