Se le agregaron y mejoraron varias cosas, para empezar se revisó el tema del audio y se encontró con
una muy buena librería de cosas documentadas en la página https://www.pygame.org/docs/ref/mixer.html
e ahí se extrajeron las líneas para agregar la librería y posteriormente citar el audio de efecto FX
como los formatos no admiten .mp3, pensé en usar un conversor en línea, pero luego recordé la misma
página de scratch de donde saqué en formato vector los monos de mi juego personal, por lo que fui a 
revisar su galería de sonidos y a descargar unos cuantos que sonaban chistososo, no hubo necesidad de 
cambiarles el formato porque cuando lo descargué, ya tenían el formato de .wav, así que solamente fue
el descargarla y ponerla en la misma carpeta del proyecto, por lo que fue muy fácil.
En segundo lugar, fue revisar el formato de dirección para las balas, ya que originalmente la dirección
estaba apuntando a la derecha pero se requiería un cambio de dirección, por lo que se estableció una multi
dirección en formato reloj por medio de las teclas 78946123 que van en el teclado numérico de la derecha de
las computadoras, con esas "flechas" se puede mover un 'aim' o una mira amarilla que visualmente apoya la 
dirección a la que la bala saldrá disparada, sale con la misma dirección en suma de x, sin embargo, en las 
diagonales x+y se creó una normalización para que la velocidad se operara y quedara igual que las demás.
Por último, se agregó con flecha arriba y flecha abajo, el cambio de velocidad en el recorrido que hace la 
bala al ser disparada desde el objeto en alguna de las direcciones deseadas.



## 🧩 Práctica 3: Disparos

**Tema:** Crear y mover proyectiles.

### 🎯 Objetivo

**Aprender:**

- Uso de listas para manejar múltiples objetos.

- Movimiento de balas.

- Crear nuevas instancias de objetos.

### 🧠 Funciones nuevas

- **pygame.Rect()** – Representa objetos con posición y tamaño.

- Listas dinámicas para agregar o eliminar balas.

### 🧩 Tarea

- Cambia la velocidad del disparo.

- Dispara en diferentes direcciones.

- Agrega sonido con pygame.mixer.Sound.

### 💻 Código base

```python
import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 3 - Disparos")

x, y = 50, 300
balas = []
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            balas.append(pygame.Rect(x + 40, y + 15, 10, 5))

    for bala in balas:
        bala.x += 10

    balas = [b for b in balas if b.x < 600]

    pantalla.fill((20, 20, 20))
    pygame.draw.rect(pantalla, (0, 255, 0), (x, y, 40, 40))
    for b in balas:
        pygame.draw.rect(pantalla, (255, 0, 0), b)
    pygame.display.update()

pygame.quit()

```
