# Vamos a cambiar el modo de presentar la pantalla por medio de nombres independientes para posteriormente hacer colisión
# Se agregan las dimensiones para el personaje con respecto a la pantalla
#Se agregan las variables de velocidad turbo rapidita y la velocidad como 'vel' normal
    #Se agrega el comando de teclado para shift y avance más rápidito
    #Estas son delimitaciones creadas de acuerdo al tamaño de la pantalla y del personaje
    #Para el cambio de color, hay que cambiar el tono en RGB, en este caso lo puse rosa










# 🎮 Curso de Gráficación con Pygame  
## Prácticas básicas de creación de juegos

Estas prácticas están diseñadas para aprender los fundamentos de **Pygame** paso a paso.  
Cada práctica presenta nuevas funciones, un ejemplo funcional y un reto o tarea para reforzar el aprendizaje.

---

## 🧩 Práctica 1: Movimiento básico
**Tema:** Mostrar una ventana y mover un personaje con el teclado.  

### 🎯 Objetivo
Aprender a:
- Crear una ventana en Pygame.
- Detectar teclas.
- Mover un objeto en la pantalla.

### 🧠 Funciones nuevas
- `pygame.init()` – Inicializa el motor de Pygame.  
- `pygame.display.set_mode()` – Crea la ventana.  
- `pygame.key.get_pressed()` – Detecta teclas presionadas.  
- `pygame.time.Clock()` – Controla los FPS (velocidad del juego).

### 🧩 Tarea 

- Cambia el color del personaje.

- Evita que salga de la pantalla.

- Aumenta la velocidad al presionar Shift.

### 💻 Código base
```python
import pygame

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 1 - Movimiento básico")

x, y = 300, 200
vel = 5
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= vel
    if teclas[pygame.K_RIGHT]:
        x += vel
    if teclas[pygame.K_UP]:
        y -= vel
    if teclas[pygame.K_DOWN]:
        y += vel

    pantalla.fill((30, 30, 30))
    pygame.draw.rect(pantalla, (0, 200, 255), (x, y, 40, 40))
    pygame.display.update()

pygame.quit()
