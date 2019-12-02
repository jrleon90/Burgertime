#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Gonzalo"
__date__ ="$Nov 3, 2013 5:15:51 PM$"

import pygame,Cheff
from pygame.locals import *
import os
import Util_Functions
import sys

IMG_DIR = "C:/Users/joleon/Desktop/BurgerTime/Proyecto Ingenieria"

def load_image(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print ("Error, no se puede cargar la imagen: ", ruta)
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha == True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

class Pepper(pygame.sprite.Sprite):
    frame = 0
    

    """def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.pepper_spray_left_images=[
            load_image("Pepper1L.png", IMG_DIR, alpha=True),
            load_image("Pepper2.png", IMG_DIR, alpha=True),
            load_image("Pepper3.png", IMG_DIR, alpha=True),
            load_image("Pepper1L.png", IMG_DIR, alpha=True)
            ]
        self.pepper_spray_right_images=[
            load_image("Pepper1.png", IMG_DIR, alpha=True),
            load_image("Pepper2.png", IMG_DIR, alpha=True),
            load_image("Pepper3.png", IMG_DIR, alpha=True),
            load_image("Pepper1.png", IMG_DIR, alpha=True)
            ]

        self.pepper_spray_up_images=[
            pygame.transform.rotate(load_image("Pepper1.png", IMG_DIR, alpha=True),90),
            pygame.transform.rotate(load_image("Pepper2.png", IMG_DIR, alpha=True),90),
            pygame.transform.rotate(load_image("Pepper3.png", IMG_DIR, alpha=True),90),
            pygame.transform.rotate(load_image("Pepper1.png", IMG_DIR, alpha=True),90)
             ]

        self.pepper_spray_down_images=[
            pygame.transform.rotate(load_image("Pepper1.png", IMG_DIR, alpha=True),90),
            pygame.transform.rotate(load_image("Pepper2.png", IMG_DIR, alpha=True),90),
            pygame.transform.rotate(load_image("Pepper3.png", IMG_DIR, alpha=True),90),
            pygame.transform.rotate(load_image("Pepper1.png", IMG_DIR, alpha=True),90)
            ]"""

    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = Util_Functions.load_image("Pepper3.png", IMG_DIR, alpha=True)
       self.rect = self.image.get_rect()



    def hidePepper(self):
        self.frame = 0
        self.kill()
    """
    def pepperLeft (self,rect):
        self.rect.midright = rect.midleft
        self.frame += 1
        if self.frame > 4*3:
            self.frame = 0
        self.image = self.pepper_spray_left_images[self.frame//4]

    def pepperRight (self,rect):
        self.rect.midleft = rect.midright
        self.frame += 1
        if self.frame > 4*3:
            self.frame = 0
        self.image = self.pepper_spray_right_images[self.frame//4]

    def pepperUp (self,rect):
        self.rect.midbottom = rect.midtop
        self.frame += 1
        if self.frame > 4*3:
            self.frame = 0
        self.image = self.pepper_spray_up_images[self.frame//4]

    def pepperDown (self,rect):
        self.rect.midtop = rect.midbottom
        self.frame += 1
        if self.frame > 4*3:
            self.frame = 0
        self.image = self.pepper_spray_down_images[self.frame//4]
    """
    def pepperLeft (self,rect):
        self.rect.midright = rect.midleft

    def pepperRight (self,rect):
        self.rect.midleft = rect.midright

    def pepperUp (self,rect):
        self.rect.midbottom = rect.midtop

    def pepperDown (self,rect):
        self.rect.midtop = rect.midbottom