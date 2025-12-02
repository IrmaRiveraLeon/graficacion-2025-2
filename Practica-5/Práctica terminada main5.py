import pygame
pygame.init()

# CONFIGURACIÓN DE PANTALLA
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Práctica 5 - Animaciones")
clock = pygame.time.Clock()

# Fondo
fondo = pygame.transform.scale(
    pygame.image.load("fondo.png").convert(),
    (600, 400)
)

# Caminar
walk_frames = [
    pygame.transform.scale(pygame.image.load("personaje1.png"), (60, 80)),
    pygame.transform.scale(pygame.image.load("personaje2.png"), (60, 80)),
    pygame.transform.scale(pygame.image.load("personaje3.png"), (60, 80)),
    pygame.transform.scale(pygame.image.load("personaje2.png"), (60, 80))
]

# Brincar
jump_img = pygame.transform.scale(
    pygame.image.load("jump.png"),
    (60, 80)
)

# Disparo
bullet_img = pygame.transform.scale(
    pygame.image.load("bullet.png"),
    (30, 30)
)

# Enemigo animación
enemy_frames = [
    pygame.transform.scale(pygame.image.load("enemy1.png").convert_alpha(), (40, 60)),
    pygame.transform.scale(pygame.image.load("enemy2.png").convert_alpha(), (40, 60))
]

# Instrucciones en pantalla
fuente = pygame.font.Font(None, 24)
color_texto = (255, 255, 255)

# VARIABLES DEL PERSONAJE
x = 100
y = 250
vel_y = 0
en_suelo = True

frame = 0
frame_vel = 0

# FONDO EN MOVIMIENTO
fondo_x = 0
vel_fondo = 3

# LISTA DE BALAS
balas = []

# ENEMIGO
enemy_frame = 0
enemy_frame_vel = 0

enemy_x = 550
enemy_y = 250

# SISTEMA DE KILLS Y RESPAWN
kills = 0
enemy_active = True
enemy_respawn_timer = 0

running = True

# Main Loop
while running:
    clock.tick(30)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # CONTROLES DEL PERSONAJE
    keys = pygame.key.get_pressed()

    # SALTO
    if keys[pygame.K_SPACE] and en_suelo:
        vel_y = -12
        en_suelo = False

    # DISPARO
    if keys[pygame.K_f]:
        balas.append([x + 40, y + 20])

    # FÍSICAS
    y += vel_y
    vel_y += 0.6

    if y >= 250:
        y = 250
        vel_y = 0
        en_suelo = True


    # ANIMACIÓN DEL PERSONAJE
    if en_suelo:
        frame_vel += 1
        if frame_vel >= 6:
            frame = (frame + 1) % len(walk_frames)
            frame_vel = 0
        personaje = walk_frames[frame]
    else:
        personaje = jump_img

    # ANIMACIÓN DEL ENEMIGO
    enemy_frame_vel += 1
    if enemy_frame_vel >= 12:
        enemy_frame = (enemy_frame + 1) % len(enemy_frames)
        enemy_frame_vel = 0

    enemy_img = enemy_frames[enemy_frame]

    # MOVIMIENTO DEL ENEMIGO
    if enemy_active:
        enemy_x -= 3
        if enemy_x < -80:
            enemy_x = 600

    # RESPWAN DEL ENEMIGO
    if not enemy_active:
        enemy_respawn_timer -= 1
        if enemy_respawn_timer <= 0:
            enemy_active = True
            enemy_x = 600

    # MOVER FONDO
    fondo_x -= vel_fondo
    if fondo_x <= -ANCHO:
        fondo_x = 0

    # MOVER BALAS
    for b in balas:
        b[0] += 10

    # Eliminar balas fuera de pantalla
    balas = [b for b in balas if b[0] < ANCHO]

    # COLISIONES BALA VS ENEMIGO
    enemigo_rect = pygame.Rect(enemy_x, enemy_y, 80, 100)

    for b in balas:
        bala_rect = pygame.Rect(b[0], b[1], 20, 20)
        if bala_rect.colliderect(enemigo_rect) and enemy_active:
            enemy_active = False
            kills += 1
            enemy_respawn_timer = 60
            enemy_x = -200

    # COLISIÓN ENEMIGO VS JUGADOR
    player_rect = pygame.Rect(x, y, 50, 60)

    if enemy_active and player_rect.colliderect(enemigo_rect):
        print("GAME OVER")
        running = False

    # DIBUJAR TODO
    pantalla.blit(fondo, (fondo_x, 0))
    pantalla.blit(fondo, (fondo_x + ANCHO, 0))

    pantalla.blit(personaje, (x, y))

    for b in balas:
        pantalla.blit(bullet_img, (b[0], b[1]))

    if enemy_active:
        pantalla.blit(enemy_img, (enemy_x, enemy_y))

    # Instrucciones
    pantalla.blit(fuente.render("¡No dejes que se acerque!", True, color_texto), (10, 10))
    pantalla.blit(fuente.render("Espacio para saltar", True, color_texto), (10, 30))
    pantalla.blit(fuente.render("F para disparar", True, color_texto), (10, 50))

    # Kills
    pantalla.blit(fuente.render(f"Zombys: {kills}", True, color_texto), (10, 70))

    pygame.display.update()

pygame.quit()
