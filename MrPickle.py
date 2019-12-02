import pygame
import Util_Functions
IMG_DIR="C:/Users/joleon/Desktop/BurgerTime/Proyecto Ingenieria/MrPickle"
#Base12=[]
#Stairs12=[]
stairsandbase=[]
FacingRight= True


class MrPickle(pygame.sprite.Sprite):
    frame=0
    def __init__(self,x,y,Vx,Vy):
     pygame.sprite.Sprite.__init__(self)
     self.images=[]
     for i in range(0,24):
        img = Util_Functions.load_image("MrPickle"+str(i)+".png", IMG_DIR, alpha=True)
        imgBig = pygame.transform.smoothscale(img,(15, 20))
        self.images.append(imgBig)

        # By default, use image 0
     self.image = self.images[0]
     tranColor = self.image.get_at((1, 1))
     self.image.set_colorkey(tranColor)
     self.Vx=Vx
     self.Vy=Vy
     self.x=x
     self.y=y
     self.rect = self.image.get_rect()
     self.rect.center = (self.x,self.y)


    def moveupE(self):
      #self.y -= self.Vy
      self.rect.move_ip(0, -1)
      #self.rect.center = (self.x, self.y)
      self.frame += 1
      if self.frame > 2*2:
        self.frame = 0
      self.image = self.images[self.frame//2+4]

    def movedownE(self):
      #self.y += self.Vy
      self.rect.move_ip(0, 1)
      #self.rect.center = (self.x, self.y)
      self.frame += 1
      if self.frame > 2*2:
        self.frame = 0
      self.image = self.images[self.frame//2+2]

    def moveleftE(self):
      #FacingRight = False
      #self.x -= self.Vx
      self.rect.move_ip(-1,0)
      #self.rect.center = (self.x, self.y)
      self.frame += 1
      if self.frame > 2*5:
        self.frame = 0
      self.image = self.images[self.frame//4]

    def moverightE(self):
      #FacingRight = True
      #self.x += self.Vx
      self.rect.move_ip(1,0)
      self.frame += 1
      if self.frame > 2*5:
        self.frame = 0
      self.image = pygame.transform.flip(self.images[self.frame//4],True,False)


    def update(self,Cheff,Base12,Stairs12,pepperSpray):
        #global player
        global FacingRight
        if not pepperSpray.rect.colliderect(self.rect):
            if (self.rect.y== Cheff.rect.y):
             if CollisionWithFloor(Base12,self):
                if (self.rect.x > Cheff.rect.x) and ColisionBLeftE(Base12,self):
                 self.moveleftE()
                 #FacingRight = False
                 #self.rect.center = (self.x, self.y)
                if (self.rect.x < Cheff.rect.x) and ColisionBRightE(Base12,self):
                 self.moverightE()
                 #FacingRight = True
                 #self.rect.center = (self.x, self.y)

            elif (self.rect.y < Cheff.rect.y):
                if ColisionEDownE(Stairs12,self):
                 self.movedownE()
                 #self.rect.center = (self.x, self.y)
                if CollisionWithFloor(Base12,self):
                    if FacingRight:
                          if ColisionBRightE(Base12,self)== True:
                           self.moverightE()
                           #self.rect.center = (self.x, self.y)
                          else:
                            FacingRight = False
                    else:
                        if ColisionBLeftE(Base12,self):
                            self.moveleftE()
                            #self.rect.center = (self.x, self.y)
                        else:
                            FacingRight =True

            elif (self.rect.y > Cheff.rect.y):
                if ColisionEUpE(Stairs12,self):
                 self.moveupE()
                 #self.rect.center = (self.x, self.y)

                if CollisionWithFloor(Base12,self):
                    if FacingRight:
                          if ColisionBRightE(Base12,self)== True:
                           self.moverightE()
                           #self.rect.center = (self.x, self.y)
                          else:
                            FacingRight = False
                    else:
                        if ColisionBLeftE(Base12,self):
                            self.moveleftE()
                            #self.rect.center = (self.x, self.y)
                        else:
                            FacingRight =True



def CollisionWithFloor(Bases,MrHotDog):
    for base in Bases:
        if MrHotDog.rect.colliderect(base.rect):
          return True


def ColisionBRightE(Bases,self):
    for base in Bases:
        if self.rect.colliderect(base.rect):
          if  base.rect.right-2>= self.rect.right and self.rect.bottom<=base.rect.bottom:
              return True
    return False

def ColisionBLeftE(Bases,self):
    for base in Bases:
        if self.rect.colliderect(base.rect):
          if  base.rect.left+2<= self.rect.left and self.rect.bottom<=base.rect.bottom:
            return True
    return False

def ColisionEDownE(Escaleras,self):
    for escalera in Escaleras:
        if self.rect.colliderect(escalera.rect):
          if  escalera.rect.bottom>= self.rect.bottom+5:
           self.rect.x=escalera.rect.centerx
           return True
    return False

def ColisionEUpE(Escaleras,self):
    for escalera in Escaleras:
        if self.rect.colliderect(escalera.rect):
          if  self.rect.bottom-5>=escalera.rect.top:
              self.rect.centerx=escalera.rect.centerx
              return True
    return False