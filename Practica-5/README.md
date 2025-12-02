
Creo que el proyecto más divertido a parte del mio, ¡ha sido este! del cual puedo mencionar las cosas que se le aregaron para que pudiera funcionar.
En primer lugar, se anexaba en la práctica un sprite de un personaje rosita, para lo que se crearon a partir de ahí, unas cuantas copias con leves
modificaciones en los brazos y ojitos, luego se guardaron como frames del sprite, 4, por lo que se creó una mini función para que pudiera funcionar 
como si fuera un gif, por medio de un loop de animación con tiempo 

# Caminar
walk_frames = [
    pygame.transform.scale(pygame.image.load("personaje1.png"), (60, 80)),
    pygame.transform.scale(pygame.image.load("personaje2.png"), (60, 80)),
    pygame.transform.scale(pygame.image.load("personaje3.png"), (60, 80)),
    pygame.transform.scale(pygame.image.load("personaje2.png"), (60, 80))
]

Después de esto, creo que el juego estaba muy plano, por lo que se le aplicó una capa de color verde al mismo personaje y se le modificó en parte
para poder tener el rol de enemigo en pantalla, de ahí se agregó al programa con una muy interesante mecánica que es el avance automático al frente, 
pero para agregarle emoción al juego se le preparó una colisión con el objeto personaje, de tal modo que el juego termine cuando se hace la colisión.

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



También se agregó un sistema de disparos para que el personaje no muera y pueda defenderse, agregado un salto para poder esquivar al mono verde.
De ahí, que dispararle no tenía mucho sentido porque el zombi se eliminaba y listo, por lo que se agregó un respawn en la parte de la derecha de
la pantalla y esto le permite reiniciar su recorrido y volver a intimidar al personaje principal, de este modo sería un Game Loop, así que también
se le agregó un contador de kills en la pantalla, arriba a la izquierda en conjunto de los controles para el salto y para el disparo.


    # Instrucciones
    pantalla.blit(fuente.render("¡No dejes que se acerque!", True, color_texto), (10, 10))
    pantalla.blit(fuente.render("Espacio para saltar", True, color_texto), (10, 30))
    pantalla.blit(fuente.render("F para disparar", True, color_texto), (10, 50))

    # Kills
    pantalla.blit(fuente.render(f"Zombys: {kills}", True, color_texto), (10, 70))



Para que el juego pareciera en movimiento, se agregó el fondo con un desplazamiento visible en pantalla y un mapeo en X con reinicio para doble.


# Fondo
fondo = pygame.transform.scale(
    pygame.image.load("fondo.png").convert(),
    (600, 400)
)
    # MOVER FONDO (ya en el main)
    fondo_x -= vel_fondo
    if fondo_x <= -ANCHO:
        fondo_x = 0







___________________________________________________________________
## 🧩 Práctica 5: Fondo, sprites y animación

**Tema:** Mejorar la estética y animar al personaje.

### 🎯 Objetivo

**Aprender:**

- Cargar imágenes.

- Dibujar sprites.

- Simular desplazamiento.

### 🧠 Funciones nuevas

- **pygame.image.load()** – Carga imágenes.

- **pantalla.blit()** – Dibuja imágenes en la pantalla.

### 🧩 Tarea

- Anima el personaje cambiando imágenes.

- Mueve el fondo para simular desplazamiento.

- Combina salto, disparos y colisiones en un mini juego final.

### 💻 Código base

```python
import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 5 - Sprites y fondo")

fondo = pygame.image.load("fondo.png")
sprite = pygame.image.load("personaje.png")
x = 100
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pantalla.blit(fondo, (0, 0))
    pantalla.blit(sprite, (x, 300))
    pygame.display.update()

pygame.quit()

```
