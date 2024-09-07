import time
import pygame
import random
import json 
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
SONIDO_BALA = pygame.mixer.Sound("JUEGO/sounds/disparo.wav")
SONIDO_ELIMINACION = pygame.mixer.Sound("JUEGO/sounds/eliminacion.wav")
SONIDO_DANO = pygame.mixer.Sound("JUEGO/sounds/daño.wav")
SONIDO_VIDA = pygame.mixer.Sound("JUEGO/sounds/vida.wav")
SONIDO_MUERTE = pygame.mixer.Sound("JUEGO/sounds/wasted.wav")
WAST_IMP = pygame.image.load("JUEGO/imgs/wast.png")
WAST = pygame.transform.scale(WAST_IMP, (800, 500))

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
        if tiempo_entre_enemigos_base > 260:
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
            SONIDO_DANO.play()

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
                if tiempo_entre_balas > 100:
                    tiempo_entre_balas -= 50
            elif item.tipo == 2:
                if cubo.velocidad <= 20:
                    cubo.velocidad += 4
            elif item.tipo == 3:
                vida += 1
                SONIDO_VIDA.play()

        if item.y > ALTO:
            items.remove(item)

    VENTANA.blit(texto_vida,(20,20))
    VENTANA.blit(texto_puntos,(20,50))
    pygame.display.update()

SONIDO_MUERTE.play()
time.sleep(2.5)
VENTANA.blit(WAST,(60,100))
pygame.display.update()
time.sleep(5)
pygame.quit()
nombre = input("Introduce tu nombre: ")
datos = {
    "nombre":nombre,
    "enemigos_esq":esquivados,
    "enemigos_elm":eliminados,
    "puntos":puntos
}

try:
    #Lectura
    with open("JUEGO/puntuaciones.json","r") as file:
        data_ = json.load(file)
except:
    data_ = []

data_.append(datos)

for q in range(len(data_)-1):
    if data_[q]["nombre"] == nombre:
        data_.pop(q)

#Escritura
with open("JUEGO/puntuaciones.json","w") as file:
    json.dump(data_, file, indent=4)

print("Gracias por jugar")

quit()