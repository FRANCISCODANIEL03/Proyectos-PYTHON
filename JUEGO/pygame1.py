import pygame
import random
from personaje import Cubo
from enemigo import Enemigo
from bala import Bala
from item import Item

pygame.init()

pygame.mixer.init()

ANCHO = 900
ALTO = 700
VENTANA = pygame.display.set_mode([ANCHO,ALTO])
FPS = 60
FUENTE = pygame.font.SysFont("Comics Sans", 40)
SONIDO_BALA = pygame.mixer.Sound("JUEGO/SOUNDS/disparo.wav")
SONIDO_ELIMINACION = pygame.mixer.Sound("JUEGO/SOUNDS/eliminacion.wav")
SONIDO_DANO = pygame.mixer.Sound("JUEGO/SOUNDS/daño.wav")
SONIDO_VIDA = pygame.mixer.Sound("JUEGO/SOUNDS/vida.wav")
#SONIDO_MUERTE = pygame.mixer.Sound("JUEGO/SOUNDS/wasted.wav")

jugando = True

reloj = pygame.time.Clock()

vida = 3
puntos = 0
eliminados = 0
esquivados = 0

tiempo_pasado = 0
tiempo_entre_enemigos = 500
tiempo_entre_enemigos_base = 1000

cubo = Cubo(ANCHO/2,ALTO-75)

enemigos = []
balas = []
items = []

ultima_bala = 0
tiempo_entre_balas = 500

ultimo_item = 0
tiempo_entre_items = 3000

enemigos.append(Enemigo(ANCHO/2, 100))

def crear_bala():
    global ultima_bala

    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_balas:
        balas.append(Bala(cubo.rect.centerx, cubo.rect.centery))
        ultima_bala = pygame.time.get_ticks()
        SONIDO_BALA.play()

def crear_item():
        global ultimo_item

        if pygame.time.get_ticks() - ultimo_item > tiempo_entre_items:
            ultimo_item = pygame.time.get_ticks()
            items.append(Item(random.randint(100, ANCHO-100), random.randint(-1000, -100)))

def gestionar_teclas(teclas):
    """
    if teclas[pygame.K_w]:
        cubo.y -= cubo.velocidad
    if teclas[pygame.K_s]:
        cubo.y += cubo.velocidad
    """
    if teclas[pygame.K_a]:
        if cubo.x >= 0:
            cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        if cubo.x + cubo.ancho <= ANCHO:
            cubo.x += cubo.velocidad
    if teclas[pygame.K_SPACE]:
        crear_bala()

while jugando and vida > 0:
    tiempo_pasado += reloj.tick(FPS)

    if tiempo_pasado > tiempo_entre_enemigos:
        enemigos.append(Enemigo(random.randint(0,ANCHO),-100))
        tiempo_pasado = 0
        tiempo_entre_enemigos = random.randint(50, tiempo_entre_enemigos_base)
        if tiempo_entre_enemigos_base > 280:
            tiempo_entre_enemigos_base -= 20


    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()

    texto_vida = FUENTE.render(f"Vidas: {vida}", True, "white")
    texto_puntos = FUENTE.render(f"Puntos: {puntos}", True, "white")

    crear_item()
    gestionar_teclas(teclas)
    
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill("black")
    cubo.dibujar(VENTANA)
    
    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()

        if pygame.Rect.colliderect(cubo.rect, enemigo.rect):
            vida -= 1
            enemigos.remove(enemigo)

        if enemigo.y > ALTO:
            puntos += 1
            esquivados += 1
            enemigos.remove(enemigo)

        for bala in balas:
            if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                enemigo.vida -= 1
                balas.remove(bala)

        if enemigo.vida <= 0:
            enemigos.remove(enemigo)
            puntos += 2
            eliminados += 1
            SONIDO_ELIMINACION.play()
                
    for bala in balas:
        bala.dibujar(VENTANA)
        bala.movimiento()

        if bala.y < 0:
            balas.remove(bala)

    for item in items:
        item.dibujar(VENTANA)
        item.movimiento()

        if pygame.Rect.colliderect(item.rect, cubo.rect):
            items.remove(item)

            if item.tipo == 1:
                if tiempo_entre_balas > 200:
                    tiempo_entre_balas -= 80
            elif item.tipo == 2:
                if cubo.velocidad <= 20:
                    cubo.velocidad += 4
            elif item.tipo == 3:
                vida += 1

        if item.y > ALTO:
            items.remove(item)

    VENTANA.blit(texto_vida,(20,20))
    VENTANA.blit(texto_puntos,(20,50))
    pygame.display.update()

#SONIDO_MUERTE.play()
pygame.quit()

nombre = input("Introduce tu nombre: ")
with open('JUEGO/puntuaciones.txt','a') as archivo:
    archivo.write(f"{nombre} - \nEnemigos esquivados: {esquivados}\nEnemigos eliminados: {eliminados}\nPuntos Totales: {puntos}\n")

quit()