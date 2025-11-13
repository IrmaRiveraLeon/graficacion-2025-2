Para esta práctica, se revisó que la música de los efectos es .wav, mientras que la música de fondo 
para un bucle, debe de ser formato .mp3, se utilizó un convertor externo en la siguiente liga de:
https://convertio.co/es/download/b8354f6edd0e4b880ac9eb885faa50ad2f868a/ para poder cambiar formato
De ahí se hizo un respawn del enemigo en las coordenadas de pantalla aleatoria pero que aún así dieran
un espacio para que no se encimaran con las de nuestro jugador, a quien se le dio la instrucción de que
se pueda mover en el eje de las 'y' de arriba a abajo para poder manipularlo con las flechas y así 
poder pegarle al enemigo en donde sea que haya respawneado. También se puso una variable de contador
de puntos para que se viera en la pantalla cuántos dispaos se han acertado contra el mono enemigo.




## 🧩 Práctica 4: Colisiones

**Tema:** Detección de choques entre objetos.

### 🎯 Objetivo

**Aprender a:**

- Detectar colisiones entre rectángulos.

- Eliminar objetos al colisionar.

### 🧠 Funciones nuevas

- **pygame.Rect.colliderect()** – Detecta colisiones.

- Uso de bucles anidados y copias de listas.

### 🧩 Tarea

- Haz que los enemigos reaparezcan en posiciones aleatorias.

- Agrega un contador de puntos.

- Muestra el puntaje en pantalla.

### 💻 Código base

```python
import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 4 - Colisiones")

jugador = pygame.Rect(50, 300, 40, 40)
balas = []
enemigos = [pygame.Rect(500, 300, 40, 40)]
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            balas.append(pygame.Rect(jugador.x + 40, jugador.y + 15, 10, 5))

    for b in balas:
        b.x += 10
    balas = [b for b in balas if b.x < 600]

    for b in balas[:]:
        for e in enemigos[:]:
            if b.colliderect(e):
                balas.remove(b)
                enemigos.remove(e)

    pantalla.fill((0, 0, 0))
    pygame.draw.rect(pantalla, (0, 255, 0), jugador)
    for b in balas:
        pygame.draw.rect(pantalla, (255, 255, 0), b)
    for e in enemigos:
        pygame.draw.rect(pantalla, (255, 0, 0), e)
    pygame.display.update()

pygame.quit()

```
