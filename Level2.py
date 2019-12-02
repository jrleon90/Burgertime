import Cheff
import MrHotDog
import Pepper
import MrEgg
import MrPickle

def getmap():
    level = [
"",
"",
"",
"",
"",
"",
"",
"",
"                                          1234            ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"",
"                              L",
"",
"                               ",
"",
"                               ",
"            1234                          abcd           ",
"          WWWWWWWWWWWWWWWMWWWWWWWWMWWWWWWWWWWWWWW        ",
"                                                         ",
"                         L        L                      ",
"                                                         ",
"                                                         ",
"                                                         ",
"                                                         ",
"            efgh                          efgh           ",
"      WMWWWWWWWWWWWWWWWWWWWWWWMWWWWWWWWWWWWWWWWWWWWMW    ",
"                                                         ",
"       L                      L                    L     ",
"                                                         ",
"                                                         ",
"                                                         ",
"                                                         ",
"            5678                                         ",
"     WWWWWWWWWWWWWWWWWWMWWWWWWWWWWWMWWWWWWWWWWWWWWWWWW   ",
"                                                         ",
"                       L           L                     ",
"                                                         ",
"                                                         ",
"                                                         ",
"                                                         ",
"                                          5678           ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
"                                                         ",
"                                                         ",
"                                                         ",
"                                                         ",
"           wxyz                           wxyz           ",]
    return level

def loadConfig(jugador2,movingsprites):
    jugador2.rect.x = 288
    jugador2.rect.y = 392



    movingsprites.add(jugador2)

def loadEnemies(enemySprites):
    mrHotDog = MrHotDog.MrHotDog(220,162,0.5,0.5)
    mrHotDog2 = MrHotDog.MrHotDog(200,322,0.25,0.25)
    #mrEgg = MrEgg.MrEgg(280,322,0.25,0.25)
    #mrPickle = MrPickle.MrPickle(350,300,0.25,0.25)
    enemySprites.add(mrHotDog)
    enemySprites.add(mrHotDog2)
    #enemySprites.add(mrEgg)
    #enemySprites.add(mrPickle)


