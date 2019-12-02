import pygame
import Cheff
import Stair
import Base
import Pepper
import MrHotDog
import MrEgg
import MrPickle
import Plate
import TopBread
import Meat
import time
import Tomato
import Lettuce
import BottomBread
import Cheese
import Level1
import Level2
import StairAndBase
import Util_Functions
from pygame.locals import *
import sys
 
# -----------
# Constantes
# -----------
pygame.init()
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 550

SONIDO_DIR = "sonidos"

Escalera_lista=pygame.sprite.RenderClear()
Base_lista=pygame.sprite.RenderPlain() 
movingsprites = pygame.sprite.RenderPlain()
enemySprites = pygame.sprite.Group()
map=[]

Text=pygame.font.SysFont("Verdana",16,False,False)




screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.flip()
pygame.mixer.init()
    # creamos la ventana y le indicamos un titulo:
pygame.display.set_caption("Burger Time")
IMG_DIR = "C:/Users/joleon/Desktop/BurgerTime/Proyecto Ingenieria"

 
# cargamos los objetos

black = 0,0,0
Base12=[]
Stairs12=[]
Plates=[]
Ingredientes=[]
CoordenadasX=[]
CoordenadasY=[]
CoordYIngr=[]
cheffLifeImageCont= pygame.transform.smoothscale((Util_Functions.load_image("CheffLifeCont1.png", IMG_DIR+"/PeterPepper/", alpha=True)),(12,12))
pepperSprayImageCont= pygame.transform.smoothscale((Util_Functions.load_image("PepperSprayCont.png", IMG_DIR, alpha=True)),(12,12))
pepperDelay = 0
lifeCont = 3
pepperCont = 3



def readlevel(level):
    x = y = 0
    for row in level:
        for col in row:
            if col == "W":
                base= Base.Base(x,y,Util_Functions.load_image("Base01.png",IMG_DIR))
                Base12.append(base)
                CoordenadasY.append(base.positionY)
                CoordenadasX.append(base.positionX)
            if col == "L":
                escaleraL=Stair.Stair(x,y,Util_Functions.load_image("Escalera22.png",IMG_DIR))
                Stairs12.append(escaleraL)
            if col == "M":
                escaleraM=Stair.Stair(x,y,Util_Functions.load_image("Escalera11.png",IMG_DIR))
                Stairs12.append(escaleraM)
            if col == "S":
                escaleraP=Stair.Stair(x,y,Util_Functions.load_image("Escalera01.png",IMG_DIR))
                Stairs12.append(escaleraP)
            if col == "w":
                plato1 = Plate.Plate(x,y,Util_Functions.load_image("Plato01.png",IMG_DIR))
                Plates.append(plato1)
                CoordenadasY.append(plato1.positionY)
                CoordenadasX.append(plato1.positionX)
            if col == "x":
                plato2 = Plate.Plate(x,y,Util_Functions.load_image("Plato02.png",IMG_DIR))
                Plates.append(plato2)
                CoordenadasY.append(plato2.positionY)
                CoordenadasX.append(plato2.positionX)
            if col == "y":
                plato3 = Plate.Plate(x,y,Util_Functions.load_image("Plato03.png",IMG_DIR))
                Plates.append(plato3)
                CoordenadasY.append(plato3.positionY)
                CoordenadasX.append(plato3.positionX)
            if col == "z":
                plato4 = Plate.Plate(x,y,Util_Functions.load_image("Plato04.png",IMG_DIR))
                Plates.append(plato4)
                CoordenadasY.append(plato4.positionY)
                CoordenadasX.append(plato4.positionX)
            if col == "1":
                PanS1= TopBread.TopBread(x,y,Util_Functions.load_image("TopBread01.png",IMG_DIR),False,"S1")
                Ingredientes.append(PanS1)
                CoordenadasY.append(PanS1.positionY)
                CoordenadasX.append(PanS1.positionX)
            if col == "2":
                PanS2= TopBread.TopBread(x,y,Util_Functions.load_image("TopBread02.png",IMG_DIR),False,"S2")
                Ingredientes.append(PanS2)
                CoordenadasY.append(PanS2.positionY)
                CoordenadasX.append(PanS2.positionX)
            if col == "3":
                PanS3= TopBread.TopBread(x,y,Util_Functions.load_image("TopBread03.png",IMG_DIR),False,"S3")
                Ingredientes.append(PanS3)
                CoordenadasY.append(PanS3.positionY)
                CoordenadasX.append(PanS3.positionX)
            if col == "4":
                PanS4= TopBread.TopBread(x,y,Util_Functions.load_image("TopBread04.png",IMG_DIR),False,"S4")
                Ingredientes.append(PanS4)
                CoordenadasY.append(PanS4.positionY)
                CoordenadasX.append(PanS4.positionX)
            if col == "5":
                PanI1= BottomBread.BottomBread(x,y,Util_Functions.load_image("BottomBread01.png",IMG_DIR),False,"I1")
                Ingredientes.append(PanI1)
                CoordenadasY.append(PanI1.positionY)
                CoordenadasX.append(PanI1.positionX)
            if col == "6":
                PanI2= BottomBread.BottomBread(x,y,Util_Functions.load_image("BottomBread02.png",IMG_DIR),False,"I2")
                Ingredientes.append(PanI2)
                CoordenadasY.append(PanI2.positionY)
                CoordenadasX.append(PanI2.positionX)
            if col == "7":
                PanI3= BottomBread.BottomBread(x,y,Util_Functions.load_image("BottomBread03.png",IMG_DIR),False,"I3")
                Ingredientes.append(PanI3)
                CoordenadasY.append(PanI3.positionY)
                CoordenadasX.append(PanI3.positionX)
            if col == "8":
                PanI4= BottomBread.BottomBread(x,y,Util_Functions.load_image("BottomBread04.png",IMG_DIR),False,"I4")
                Ingredientes.append(PanI4)
                CoordenadasY.append(PanI4.positionY)
                CoordenadasX.append(PanI4.positionX)
            if col == "a":
                Queso1= Cheese.Cheese(x,y,Util_Functions.load_image("Cheese01.png",IMG_DIR),False,"Q1")
                Ingredientes.append(Queso1)
                CoordenadasY.append(Queso1.positionY)
                CoordenadasX.append(Queso1.positionX)
            if col == "b":
                Queso2= Cheese.Cheese(x,y,Util_Functions.load_image("Cheese02.png",IMG_DIR),False,"Q2")
                Ingredientes.append(Queso2)
                CoordenadasY.append(Queso2.positionY)
                CoordenadasX.append(Queso2.positionX)
            if col == "c":
                Queso3= Cheese.Cheese(x,y,Util_Functions.load_image("Cheese03.png",IMG_DIR),False,"Q3")
                Ingredientes.append(Queso3)
                CoordenadasY.append(Queso3.positionY)
                CoordenadasX.append(Queso3.positionX)
            if col == "d":
                Queso4= Cheese.Cheese(x,y,Util_Functions.load_image("Cheese04.png",IMG_DIR),False,"Q4")
                Ingredientes.append(Queso4)
                CoordenadasY.append(Queso4.positionY)
                CoordenadasX.append(Queso4.positionX)
            if col == "e":
                Carne1= Meat.Meat(x,y,Util_Functions.load_image("Meat01.png",IMG_DIR),False,"M1")
                Ingredientes.append(Carne1)
                CoordenadasY.append(Carne1.positionY)
                CoordenadasX.append(Carne1.positionX)

            if col == "f":
                Carne2= Meat.Meat(x,y,Util_Functions.load_image("Meat02.png",IMG_DIR),False,"M2")
                Ingredientes.append(Carne2)
                CoordenadasY.append(Carne2.positionY)
                CoordenadasX.append(Carne2.positionX)

            if col == "g":
                Carne3= Meat.Meat(x,y,Util_Functions.load_image("Meat03.png",IMG_DIR),False,"M3")
                Ingredientes.append(Carne3)
                CoordenadasY.append(Carne3.positionY)
                CoordenadasX.append(Carne3.positionX)

            if col == "h":
                Carne4= Meat.Meat(x,y,Util_Functions.load_image("Meat04.png",IMG_DIR),False,"M4")
                Ingredientes.append(Carne4)
                CoordenadasY.append(Carne4.positionY)
                CoordenadasX.append(Carne4.positionX)

            if col == "i":
                Tomate1= Tomato.Tomato(x,y,Util_Functions.load_image("Tomate01.png",IMG_DIR),False,"T1")
                Ingredientes.append(Tomate1)
                CoordenadasY.append(Tomate1.positionY)
                CoordenadasX.append(Tomate1.positionX)
            if col == "j":
                Tomate2= Tomato.Tomato(x,y,Util_Functions.load_image("Tomate02.png",IMG_DIR),False,"T2")
                Ingredientes.append(Tomate2)
                CoordenadasY.append(Tomate2.positionY)
                CoordenadasX.append(Tomate2.positionX)
            if col == "k":
                Tomate3= Tomato.Tomato(x,y,Util_Functions.load_image("Tomate03.png",IMG_DIR),False,"T3")
                Ingredientes.append(Tomate3)
                CoordenadasY.append(Tomate3.positionY)
                CoordenadasX.append(Tomate3.positionX)
            if col == "l":
                Tomate4= Tomato.Tomato(x,y,Util_Functions.load_image("Tomate04.png",IMG_DIR),False,"T4")
                Ingredientes.append(Tomate4)
                CoordenadasY.append(Tomate4.positionY)
                CoordenadasX.append(Tomate4.positionX)
            if col == "m":
                Lechuga1= Lettuce.Lettuce(x,y,Util_Functions.load_image("Lettuce01.png",IMG_DIR),False,"L1")
                Ingredientes.append(Lechuga1)
                CoordenadasY.append(Lechuga1.positionY)
                CoordenadasX.append(Lechuga1.positionX)
            if col == "n":
                Lechuga2= Lettuce.Lettuce(x,y,Util_Functions.load_image("Lettuce02.png",IMG_DIR),False,"L2")
                Ingredientes.append(Lechuga2)
                CoordenadasY.append(Lechuga2.positionY)
                CoordenadasX.append(Lechuga2.positionX)
            if col == "o":
                Lechuga3= Lettuce.Lettuce(x,y,Util_Functions.load_image("Lettuce03.png",IMG_DIR),False,"L3")
                Ingredientes.append(Lechuga3)
                CoordenadasY.append(Lechuga3.positionY)
                CoordenadasX.append(Lechuga3.positionX)
            if col == "p":
                Lechuga4= Lettuce.Lettuce(x,y,Util_Functions.load_image("Lettuce04.png",IMG_DIR),False,"L4")
                Ingredientes.append(Lechuga4)
                CoordenadasY.append(Lechuga4.positionY)
                CoordenadasX.append(Lechuga4.positionX)

            x += 12
        y += 10
        x=0



# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
def play():
    global pepperCont
    global lifeCont
    global pepperDelay
    level=Level1.getmap()
    readlevel(level)
    jugador2 = Cheff.Cheff()
    pepperSpray = Pepper.Pepper ()
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 25)  # Activa repeticion de teclas
    Level1.loadConfig(jugador2,movingsprites)
    Level1.loadEnemies(enemySprites)

    while True:
        screen.fill(black)


        secs=pygame.time.get_ticks()/1000

        """if secs==59:
             secs=00
             mins+=1

            if mins == 59:
             secs=00
             mins=00
             hrs+=1

            secsStr=str(secs)
            minsStr=str(mins)
            hrsStr=str(hrs)
            screen.blit(Text.render(hrsStr+":"+minsStr+":"+secsStr,0,(255,255,255)),(280,29))"""

        secsStr=str(secs)
        screen.blit(Text.render("Tiempo:",0,(255,255,255)),(300,29))
        screen.blit(Text.render(secsStr+" s",0,(255,255,255)),(380,29))
        render_screen(Stairs12,Base12,Plates,Ingredientes)

        if lifeCont==3:
            screen.blit(cheffLifeImageCont,(635,29))
            screen.blit(cheffLifeImageCont,(655,29))
            screen.blit(cheffLifeImageCont,(675,29))
        if lifeCont==2:
            screen.blit(cheffLifeImageCont,(635,29))
            screen.blit(cheffLifeImageCont,(655,29))
        if lifeCont==1:
            screen.blit(cheffLifeImageCont,(635,29))

        if pepperCont==3:
            screen.blit(pepperSprayImageCont,(635,45))
            screen.blit(pepperSprayImageCont,(655,45))
            screen.blit(pepperSprayImageCont,(675,45))
        if pepperCont==2:
            screen.blit(pepperSprayImageCont,(635,45))
            screen.blit(pepperSprayImageCont,(655,45))
        if pepperCont==1:
            screen.blit(pepperSprayImageCont,(635,45))

        screen.blit(Text.render("Vida:",0,(255,255,255)),(590,22))
        screen.blit(Text.render("Pepper Spray:",0,(255,255,255)),(520,40))

        Base_lista.draw(screen)
        movingsprites.draw(screen)
        enemySprites.draw(screen)
        #pygame.draw.rect(screen,(255,0,255),mrHotDog)
        #pygame.draw.rect(screen,(255,255,0),mrHotDog2)
        

   
        
        # Actualizamos los obejos en pantalla
         
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and ColisionBLeft(Base12,jugador2):
                    jugador2.moveleft()
                if event.key == pygame.K_RIGHT and ColisionBRight(Base12,jugador2):
                    jugador2.moveright()
                if event.key == pygame.K_UP and ColisionEUp(Stairs12,jugador2): 
                    jugador2.moveup()                                    
                if event.key == pygame.K_DOWN and ColisionEDown(Stairs12,jugador2):
                    jugador2.movedown()
                if event.key == pygame.K_SPACE:
                  if pepperCont > 0:
                    pepperDelay = pygame.time.get_ticks()/1000
                    pepperCont-=1
                    if jugador2.FacingLeft == True:
                        pepperSpray.pepperLeft(jugador2.rect)
                        movingsprites.add(pepperSpray)
                    if jugador2.FacingRight == True:
                        pepperSpray.pepperRight(jugador2.rect)
                        movingsprites.add(pepperSpray)
                    if jugador2.FacingUp == True:
                        pepperSpray.pepperUp(jugador2.rect)
                        movingsprites.add(pepperSpray)
                    if jugador2.FacingDown == True:
                        pepperSpray.pepperDown(jugador2.rect)
                        movingsprites.add(pepperSpray)

        ColisionH(jugador2,Ingredientes,Base12,Plates)
        pygame.display.flip()
        clock.tick(25)
        pygame.draw.rect(screen,(255,255,0),pepperSpray)
        #jugador2.update() 
        #actualizamos la pantalla
        
       # todos = pygame.sprite.RenderPlain(jugador2)
        #todos.draw(screen)

        if pygame.sprite.groupcollide(movingsprites,enemySprites,False,False):
         lifeCont-=1
         jugador2.rect.center=(400,162)

        if (pepperDelay+1<=pygame.time.get_ticks()/1000):
            pepperSpray.hidePepper()

        enemySprites.update(jugador2,Base12,Stairs12,pepperSpray)

       
        
        #movingsprites.draw(screen)



        
def render_screen(escaleras,Bases,EscalerasBases):

    for es in escaleras:
        screen.blit(es.image,(es.positionX,es.positionY))
        #pygame.draw.rect(screen,(120,255,0),es)
    for bas in Bases:
        screen.blit(bas.image,(bas.positionX,bas.positionY))
        #pygame.draw.rect(screen,(255,0,255),bas)
    for esbas in EscalerasBases:
        screen.blit(esbas.image,(esbas.positionX,esbas.positionY))
    #pygame.display.flip()


def ColisionBRight(Bases,Cheff):
    for base in Bases:
        if Cheff.rect.colliderect(base.rect):
          if  (base.rect.right-2>= Cheff.rect.right) and (Cheff.rect.bottom<=base.rect.bottom):
            return True
    return False

def ColisionBLeft(Bases,Cheff):
    for base in Bases:
        if Cheff.rect.colliderect(base.rect):
          if  (base.rect.left+2<= Cheff.rect.left) and (Cheff.rect.bottom<=base.rect.bottom):
            return True
    return False

def ColisionEDown(Escaleras,Cheff):
    for escalera in Escaleras:
        if Cheff.rect.colliderect(escalera.rect):
          if  (escalera.rect.bottom-8>= Cheff.rect.bottom):
            Cheff.rect.centerx=escalera.rect.centerx
            return True
    return False

def ColisionEUp(Escaleras,Cheff):
    for escalera in Escaleras:
        if Cheff.rect.colliderect(escalera.rect):
          if  (Cheff.rect.bottom-3.75>=escalera.rect.top):
            Cheff.rect.centerx=escalera.rect.centerx
            return True
    return False


def Choque(Ingrediente,Cheff):
    for i in Ingrediente:
        if Cheff.rect.colliderect(i.rect):
            i.positionY+=10

def render_screen(Stairs12,Bases12,plato,Ingredientes):

    for es in Stairs12:
        screen.blit(es.image,(es.positionX,es.positionY))
    for bas in Bases12:
        screen.blit(bas.image,(bas.positionX,bas.positionY))
    for pla in plato:
        screen.blit(pla.image,(pla.positionX,pla.positionY))
    for ing in Ingredientes:
        screen.blit(ing.image,(ing.positionX,ing.positionY))
def ColisionB(Base,Cheff):
    for base in Base:
        if Cheff.rect.colliderect(base.rect):
            return True
    return False
def ColisionY(posY,obj1):
    cont=0
    for cory in CoordenadasY:
        if posY==cory:
            if (ColisionX(cont,obj1)):
                return True
        cont+=1
    return False
def ColisionX(posArreglo,obj1):
    if CoordenadasX[posArreglo]==obj1.positionX:
        return True

def ColisionE(EscalerasL,EscalerasM,EscalerasP,Cheff):
    for escaleraL in EscalerasL:
        if Cheff.rect.colliderect(escaleraL.rect):
            return True
    for escaleraM in EscalerasM:
        if Cheff.rect.colliderect(escaleraM.rect):
            return True
    for escaleraP in EscalerasP:
        if Cheff.rect.colliderect(escaleraP.rect):
            return True

def ColisionH (Cheff,Ingredientes,Base,Platos):

    for i in Ingredientes:
        for p in Platos:
            if (i.rect.colliderect(p.rect)):
                p.IngredienteOn=True
                break


    for ing in Ingredientes:
        if (Cheff.rect.colliderect(ing.rect)) and ing.Enable:
            ing.positionY+=12
            ing.rect.move_ip(0,12)
            ing.IsDown=True
        for ing2 in Ingredientes:

            if ing2.IsDown:
                while not(ColisionY(ing2.positionY,ing2)):
                    ing2.positionY+=1
                    ing2.rect.move_ip(0,1)
                    ing2.IsDown=False

    for ing3 in Ingredientes:
        for ing4 in Ingredientes:
            if (ing3.Number[0] != ing4.Number[0])and(ing3.positionY == ing4.positionY)and(ing3.positionX==ing4.positionX)and (ColisionPlatos(ing4,Platos)==False):
                ing4.positionY+=13
                ing4.rect.move_ip(0,13)
                while not(ColisionY(ing4.positionY,ing4)):
                    ing4.positionY+=1
                    ing4.rect.move_ip(0,1)
                if((ColisionPlatos(ing4,Platos)==True)):
                    ing4.Enable=False


    for plat in Platos:
        for i in Ingredientes:
             for i2 in Ingredientes:
                if (plat.IngredienteOn)and(i.Number[0] != i2.Number[0])and(i.positionY==i2.positionY)and(i.positionX==i2.positionX):
                   plat.ganar+=1
                   for i3 in Ingredientes:
                       if (i3.Number[0]!=i.Number[0])and (i3.positionY==i.positionY)and(i3.positionX==i.positionX):

                            while(colisionObj(i,i3)):
                                i.positionY-=1
                                i.rect.move_ip(0, -1)
                            for i4 in Ingredientes:
                                if (i4.Number[0]!=i.Number[0])and i4.positionY==i.positionY and i4.positionX==i.positionX:
                                    while(colisionObj(i4,i)):
                                        i.positionY-=1
                                        i.rect.move_ip(0, -1)
                            for i5 in Ingredientes:
                                if (i5.Number[0]!=i.Number[0])and i5.positionY==i.positionY and i5.positionX==i.positionX:
                                      while(colisionObj(i5,i)):
                                        i.positionY-=1
                                        i.rect.move_ip(0, -1)
                            for i6 in Ingredientes:
                                if (i6.Number[0]!=i.Number[0])and i6.positionY==i.positionY and i6.positionX==i.positionX:
                                      while(colisionObj(i6,i)):
                                        i.positionY-=1
                                        i.rect.move_ip(0, -1)
                            for i7 in Ingredientes:
                                if (i7.Number[0]!=i.Number[0])and i7.positionY==i.positionY and i7.positionX==i.positionX:
                                      while(colisionObj(i7,i)):
                                        i.positionY-=1
                                        i.rect.move_ip(0, -1)




def PasarNivel(Platos):
    cont=0
    cont2=0
    for p in Platos:
        cont+=1

    for p2 in Platos:
        cont2+=p2.ganar
        print(cont2)
    if (cont2==cont*5):
        return True
    return False

def colisionObj(obj1,obj2):
    if (obj1.rect.colliderect(obj2.rect)):
        return True
    return False

def ColisionPlatos(obj,Platos):
    for plat in Platos:
            if (plat.rect.colliderect(obj.rect)):
                return True
    return False

play()
   
