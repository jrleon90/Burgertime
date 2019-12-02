import pygame
from pygame.locals import *
import os
import sys

 
# -----------
# Constantes
# -----------
FlipHorizontal = True
FlipVertical = False
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
IMG_DIR = "C:/Users/joleon/Desktop/BurgerTime/Proyecto Ingenieria/PeterPepper"


def load_image(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print ("Error, no se puede cargar la imagen: ")
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha == True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

 
# -----------------------------------------------
# Creamos los sprites (clases) de los objetos del juego:
 
 
class Cheff(pygame.sprite.Sprite):
    
    "Define el comportamiento de las paletas de ambos jugadores"
    # -- Attributes
    # Set speed vector
    Vx=5
    Vy=4
    FacingLeft = False
    FacingRight = False
    FacingUp = False
    FacingDown = False
    
    # This is a frame counter used to determing which image to draw
    frame = 0
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # List that the cat images will be saved in.
        self.images=[]
        # Load all the cat images, from cat1.png to cat8.png.
        for i in range(2,11):
            img = load_image("Cheff"+str(i)+".png", IMG_DIR, alpha=True)
            imgBig = pygame.transform.smoothscale(img,(28, 20))
            self.images.append(imgBig)
            
        # By default, use image 0
        self.image = self.images[8]
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values 
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = SCREEN_HEIGHT / 2
        self.collision = True
        
    def moveup(self):
        self.FacingLeft = False
        self.FacingRight = False
        self.FacingUp = True
        self.FacingDown = False
        self.rect.top -= self.Vy
        self.frame += 1
        if self.frame > 2*4:
            self.frame = 0
        self.image = self.images[self.frame//3+3]
        
    def movedown(self):
        self.FacingLeft = False
        self.FacingRight = False
        self.FacingUp = False
        self.FacingDown = True
        self.rect.bottom += self.Vy
        self.frame += 1
        if self.frame > 2*4:
            self.frame = 0
        self.image = self.images[self.frame//3+6] 
      
    def moveleft(self):
        self.FacingLeft = True
        self.FacingRight = False
        self.FacingUp = False
        self.FacingDown = False
        self.rect.left -= self.Vx
        self.frame += 1
         
        if self.frame > 2*4:
            self.frame = 0
        self.image = self.images[self.frame//3]   
        
    def moveright(self):
        self.FacingLeft = False
        self.FacingRight = True
        self.FacingUp = False
        self.FacingDown = False
        self.rect.left += self.Vx
        self.frame += 1
        if self.frame > 2*4:
            self.frame = 0
        self.image = pygame.transform.flip(self.images[self.frame//3],FlipHorizontal,FlipVertical)   
        