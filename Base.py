# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="MI EQUIPO"
__date__ ="$10/11/2013 12:01:55 PM$"

class Base:
            def __init__(self,positionX, positionY, image):
                self.positionX = positionX
                self.positionY = positionY
                self.image = image
                self.rect = self.image.get_rect(topleft = (self.positionX, self.positionY))