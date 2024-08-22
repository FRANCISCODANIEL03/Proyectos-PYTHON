import pygame
import random
from personaje import Cubo
from enemigo import Enemigo

ANCHO = 800
ALTO = 600
VENTANA = pygame.display.set_mode([ANCHO,ALTO])
FPS = 60

jugando = True

reloj = pygame.time.Clock()

tiempo_pasado = 0
tiempo_entre_enemigos = 500

cubo = Cubo(ANCHO/2,ALTO-75)

enemigos = []

enemigos.append(Enemigo(ANCHO/2, 100))

def gestionar_teclas(teclas):
    """
    if teclas[pygame.K_w]:
        cubo.y -= cubo.velocidad
    if teclas[pygame.K_s]:
        cubo.y += cubo.velocidad
    """
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad

while jugando:
    tiempo_pasado += reloj.tick(FPS)

    if tiempo_pasado > tiempo_entre_enemigos:
        enemigos.append(Enemigo(random.randint(0,ANCHO),-100))
        tiempo_pasado = 0

    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()

    gestionar_teclas(teclas)
    
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill("black")
    cubo.dibujar(VENTANA)
    
    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()

    pygame.display.update()

quit()