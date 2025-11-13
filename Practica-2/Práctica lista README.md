Se agregaró un cambio de fuerza en el salto, la línea que lo hace es la de la vel al caer
Se agregó una condición en donde existe un doble salto que hasta incluye un cambio de color,
para eso se hizo un contador tipo variable de salto en la que el salto podía ser doble para
volver a ser contabilizado por el contador de la condición.
Por último, se agregó un rectángulo como suelo con las coordenadas en x y de color verde.



## 🧩 Práctica 2: Saltos y gravedad

**Tema:** Simular un salto realista con gravedad.

### 🎯 Objetivo

**Comprender:**

- Velocidad vertical y aceleración por gravedad.

- Control de salto con SPACE.

### 🧠 Funciones nuevas

- Variables de física (velocidad, gravedad).

- pygame.key.get_pressed() para salto.

### 🧩 Tarea

- Cambia la fuerza del salto.

- Agrega doble salto.

- Dibuja un suelo visible.

### 💻 Código base
```python
import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 2 - Saltos")

x, y = 300, 300
vel_y = 0
gravedad = 1
en_suelo = True
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE] and en_suelo:
        vel_y = -15
        en_suelo = False

    y += vel_y
    vel_y += gravedad

    if y >= 300:
        y = 300
        vel_y = 0
        en_suelo = True

    pantalla.fill((50, 50, 100))
    pygame.draw.rect(pantalla, (255, 255, 0), (x, y, 40, 40))
    pygame.display.update()

pygame.quit()
```
