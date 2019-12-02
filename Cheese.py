# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Cheese:
            def __init__(self,positionX, positionY, image,IsDown,Number):
                self.positionX = positionX
                self.positionY = positionY
                self.image = image
                self.rect = self.image.get_rect(topleft = (self.positionX, self.positionY))
                self.IsDown = IsDown
                self.Number=Number
                self.Enable= True
                self.Down=False