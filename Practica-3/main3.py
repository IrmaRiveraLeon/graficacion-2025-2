import math
import pygame

pygame.init()
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Práctica 3 - Disparos (center spawn + speed con flechas)")

# Jugador
x, y = 50, 300
PLAYER_W, PLAYER_H = 40, 40

# Configuración de balas
BULLET_SPEED = 12
BULLET_SIZE = (10, 5)
balas = []

clock = pygame.time.Clock()
running = True

# Dirección inicial del disparo (vector unitario)
aim_dir = (1, 0)

# Cargar sonido (aseguras que shot.wav esté en la carpeta)
shoot_sound = pygame.mixer.Sound("shot.wav")

def normalizar(vx, vy):
    mag = math.hypot(vx, vy)
    if mag == 0:
        return 0, 0
    return vx / mag, vy / mag

def dibujar_aim(surf, px, py, dirx, diry):
    long = 30
    cx = px + PLAYER_W // 2
    cy = py + PLAYER_H // 2
    endx = cx + dirx * long
    endy = cy + diry * long
    pygame.draw.line(surf, (200, 200, 0), (cx, cy), (endx, endy), 3)
    pygame.draw.circle(surf, (255, 200, 0), (int(endx), int(endy)), 5)

font = pygame.font.SysFont(None, 18)

while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # Ajustar velocidad con flechas arriba/abajo
            if event.key == pygame.K_UP:
                BULLET_SPEED += 1
            if event.key == pygame.K_DOWN:
                BULLET_SPEED = max(1, BULLET_SPEED - 1)

            # Disparo
            if event.key == pygame.K_SPACE:
                dx, dy = aim_dir
                vx = dx * BULLET_SPEED
                vy = dy * BULLET_SPEED

                # Calcular posición de spawn: parte central del jugador + pequeño desplazamiento hacia aim
                cx = x + PLAYER_W // 2
                cy = y + PLAYER_H // 2
                offset_x = int(dx * (PLAYER_W // 2 + max(BULLET_SIZE)))  # empuja la bala hacia fuera del sprite
                offset_y = int(dy * (PLAYER_H // 2 + max(BULLET_SIZE)))
                spawn_x = cx + offset_x - BULLET_SIZE[0] // 2
                spawn_y = cy + offset_y - BULLET_SIZE[1] // 2

                rect = pygame.Rect(spawn_x, spawn_y, BULLET_SIZE[0], BULLET_SIZE[1])
                balas.append({'rect': rect, 'vx': vx, 'vy': vy})
                shoot_sound.play()

            # Dirección con keypad (num pad)
            if event.key == pygame.K_KP_8:   # arriba
                aim_dir = normalizar(0, -1)
            if event.key == pygame.K_KP_2:   # abajo
                aim_dir = normalizar(0, 1)
            if event.key == pygame.K_KP_4:   # izquierda
                aim_dir = normalizar(-1, 0)
            if event.key == pygame.K_KP_6:   # derecha
                aim_dir = normalizar(1, 0)
            if event.key == pygame.K_KP_7:   # arriba-izquierda
                aim_dir = normalizar(-1, -1)
            if event.key == pygame.K_KP_9:   # arriba-derecha
                aim_dir = normalizar(1, -1)
            if event.key == pygame.K_KP_1:   # abajo-izquierda
                aim_dir = normalizar(-1, 1)
            if event.key == pygame.K_KP_3:   # abajo-derecha
                aim_dir = normalizar(1, 1)

    # Actualizar balas
    for b in balas:
        b['rect'].x += b['vx']
        b['rect'].y += b['vy']

    # Limpiar balas fuera de pantalla
    balas = [b for b in balas if -50 < b['rect'].x < ANCHO + 50 and -50 < b['rect'].y < ALTO + 50]

    pantalla.fill((20, 20, 20))

    # Dibujar jugador (rectángulo)
    pygame.draw.rect(pantalla, (0, 255, 0), (x, y, PLAYER_W, PLAYER_H))

    # Dibujar balas
    for b in balas:
        pygame.draw.rect(pantalla, (255, 0, 0), b['rect'])

    # Dibujar aim desde el centro del jugador
    dibujar_aim(pantalla, x, y, aim_dir[0], aim_dir[1])

    # UI
    v_text = font.render(f"Vel bala: {BULLET_SPEED}  |  Balas: {len(balas)}", True, (220, 220, 220))
    pantalla.blit(v_text, (8, 8))
    ayuda = font.render("Numpad 8/2/4/6/7/9/1/3: dirección  |  Arriba/Abajo: cambiar vel  |  Espacio: disparar", True, (140,140,140))
    pantalla.blit(ayuda, (8, 26))

    pygame.display.flip()

pygame.quit()
