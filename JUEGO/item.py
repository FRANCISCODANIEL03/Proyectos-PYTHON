import pygame
import random

class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tipo = random.randint(1,3)
        self.ancho = 40 if self.tipo == 1  else 30
        self.alto = 20 if self.tipo == 1  else 30
        self.velocidad = 5
        #self.color = "purple" if self.tipo == 1 else "green"
        if self.tipo == 1:
            self.img = "max_disparo.png"
        elif self.tipo == 2:
            self.img = "max_vel.png"
        else:
            self.img = "vida.png"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load(f"JUEGO/imgs/{self.img}").convert()
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.imagen = pygame.transform.rotate(self.imagen, 90) if self.tipo == 1 else pygame.transform.rotate(self.imagen, 360)

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        #pygame.draw.rect(ventana, self.color, self.rect)
        ventana.blit(self.imagen, (self.x, self.y))

    def movimiento(self):
        self.y += self.velocidad
