import re
# User data :          Score data:
#0= nombre             0=user nickname
#1=appelido            1= won games
#2=nickname            2= lost games
#3=pass
#4=equipo

#Utiliza el archivo de texto de usuarios y con la funcion split y el separador, para devolver un arreglo de string con todos los datos del usuario.
def read_all_users():
     filein=open("C:/Users/joleon/Desktop/BurgerTime/Data/Users.txt","r")
     y=re.split(",",filein.read())
     filein.close()
     return y

#Se utiliza para buscar un usuario.
def search_user(nickname):
    x=read_all_users()
    for i in x:
        if not(i==""):
             y=re.split("/", i)
             if (not(y==""))and(y[2]==nickname):
               return y

    return None

#Verifica los datos para aprobar o no el acceso al sistema.
def log_on(nickname , password):
    user=search_user(nickname)
    if (user!=None):
        if (user[3]==password):
            return True
    return False

#Guarda los datos de cada usuario.
def save_user(fname,sname,nickname,password):
    if ((search_user(nickname)==None)):
        fileout= open ("C:/Users/joleon/Desktop/BurgerTime/Data/Users.txt","r")
        tmp=fileout.read()
        fileout.close()
        fileout= open ("C:/Users/joleon/Desktop/BurgerTime/Data/Users.txt","w")
        if(tmp==""):
            fileout.write(fname+"/"+sname+"/"+nickname+"/"+password)
        else:
            fileout.write(tmp+","+fname+"/"+sname+"/"+nickname+"/"+password)
        fileout.close()
        save_new_score(nickname)
        return True
    else:
        return False

#Guarda el record de cada usuario.
def save_new_score(nickname):
    scorefile=open("C:/Users/joleon/Desktop/BurgerTime/Data/HighScores.txt","r")
    tmp=scorefile.read()
    scorefile.close()
    scorefile=open("C:/Users/joleon/Desktop/BurgerTime/Data/HighScores.txt","w")
    if(tmp==""):
        scorefile.write(nickname+"/0/0")
    else:
        scorefile.write(tmp+","+nickname+"/0/0")
    scorefile.close

#Lee las puntuaciones de todos los usuarios.
def read_all_scores():
    scorefile=open("score.txt","r")
    tmp=scorefile.read()
    scorefile.close()
    return re.split(",",tmp)

#Busca el record de un usuario.
def search_user_score(nickname):
    list=read_all_scores()
    for i in list:
        if not(i==""):
             y=re.split("/", i)
             if (not(y==""))and(y[0]==nickname):
                 return y
    return None

#Cambia la informacion de los usuarios menos el nickname.
def update_user_data(fname,sname,nickname,password,team):
    list=read_all_users()
    fileout= open ("C:/Users/joleon/Desktop/BurgerTime/Data/Users.txt","w")
    for i in (list):
        if((i!="")and(re.split("/",i)[2]!=nickname)):
         fileout.write(i+",")
    fileout.write(fname+"/"+sname+"/"+nickname+"/"+password+"/"+team)
    fileout.close()

#Cambia la informacion de las puntuaciones de los usuarios.
def update_user_score(nickname,win,lost):
    list=read_all_scores()
    fileout= open ("score.txt","w")
    for i in (list):
        if((i!="")and(re.split("/",i)[0]!=nickname)):
         fileout.write(i+",")
    fileout.write(nickname+"/"+win+"/"+lost)
    fileout.close()

#Se le asigna un juego ganado al usuario.
def set_user_win(nickname):
    score=search_user_score(nickname)
    if (score):
        win= str(int(score[1])+1)
        lost=str(int(score[2]))
        update_user_score(nickname,win,lost)
        return True
    return False

#Se le asigna un juego perdido al usuario.
def set_user_lost(nickname):
    score=search_user_score(nickname)
    if (score):
        win= str(int(score[1]))
        lost=str(int(score[2])+1)
        update_user_score(nickname,win,lost)
        return True
    return False
