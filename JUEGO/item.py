import pygame
import random

class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tipo = random.randint(1,2)
        self.ancho = 30 if self.tipo == 2 else 40
        self.alto = 30 if self.tipo == 2 else 20
        self.velocidad = 5
        #self.color = "purple" if self.tipo == 1 else "green"
        self.img = "max_disparo.png" if self.tipo == 1 else "max_vel.png"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load(f"JUEGO/IMGS/{self.img}").convert()
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.imagen = pygame.transform.rotate(self.imagen, 90) if self.tipo == 1 else pygame.transform.rotate(self.imagen, 360)

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        #pygame.draw.rect(ventana, self.color, self.rect)
        ventana.blit(self.imagen, (self.x, self.y))

    def movimiento(self):
        self.y += self.velocidad
