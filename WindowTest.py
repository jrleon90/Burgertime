#Import necesarios para que el juego corra.
from Tkinter import *
from Tkinter import _cnfmerge
from distutils import command
from TxtFunctions import *
import pygame

nicknameR=str()
score=[]


#Clase que se utiliza para la creacion de interfaces.
class Dialog(Widget):
    def __init__(self, master=None, cnf={}, **kw):
        cnf = _cnfmerge((cnf, kw))
        self.widgetName = '__dialog__'
        Widget._setup(self, master, cnf)
        self.num = self.tk.getint(
                self.tk.call(
                      'tk_dialog', self._w,
                      cnf['title'], cnf['text'],
                      cnf['bitmap'], cnf['default'],
                      *cnf['strings']))
        try: Widget.destroy(self)
        except TclError: pass
    def destroy(self): pass

def showmainwindow():
   registrationwindow.withdraw()
   loginwindow.withdraw()
   mainwindow.configure(background='black')
   mainwindow.minsize(300, 300)
   mainwindow.maxsize(300,300)
   mainwindow.title('Burger Time')
   #mainwindow.iconbitmap(default='C:/Users/joleon/Desktop/BurgerTime/Proyecto Ingenieria/Icon.ico')
   #photo = PhotoImage(file="C:/Users/joleon/Desktop/BurgerTime/Proyecto Ingenieria/BurgerTimeLogo.pbm")
   title = Label(mainwindow, image = photo)
   title.photo = photo
   title.pack(side="top", pady = 20)


   signupbuttom = Button(mainwindow,text = " Registrarse  ", command = showregistrationwindow)
   signupbuttom.pack(side="top", pady = 20)

   loginbuttom = Button (mainwindow,text = "Iniciar Sesion", command = showloginwindow)
   loginbuttom.pack(side="top",pady = 20)

   title4= Label (mainwindow,text = "Integrantes:",bg="black",fg="white")
   title5= Label (mainwindow,text = "- Leon, Jose.",bg="black",fg="white")
   title6= Label (mainwindow,text = "- Machado, Gonzalo.",bg="black",fg="white")
   title4.pack(side="top")
   title5.pack(side="top")
   title6.pack(side="top")

   mainwindow.mainloop()

def showregistrationwindow():
    mainwindow.withdraw()
    registrationwindow.wm_deiconify()

    title3 = Label(registrationwindow, image = photo)
    title3.photo = photo
    title3.pack(side="top", pady = 12)
    registrationwindow.minsize(230, 475)
    registrationwindow.maxsize(230, 475)
    registrationwindow.title('Registro')

    Lname = Label (registrationwindow,text="Nombre:",bg="black",fg="white")
    Lname.pack(side="top",pady = 10)
    #Tfname = Entry(registrationwindow,textvariable = name)
    Tfname.pack(side="top", pady=5)

    Llastname = Label(registrationwindow, text = "Apellido:",bg="black",fg="white")
    Llastname.pack(side="top",pady=10)
    #Tflastname = Entry(registrationwindow,textvariable = lastname)
    Tflastname.pack(side="top",pady=5)

    Lnickname = Label(registrationwindow, text ="Nickname:",bg="black",fg="white")
    Lnickname.pack(side="top",pady=10)
    #Tfnickname = Entry(registrationwindow,textvariable = nickname)
    Tfnickname.pack(side="top", pady=5)

    Lpassword = Label(registrationwindow,text="Password:",bg="black",fg="white")
    Lpassword.pack(side="top",pady=10)
    #Tfpassword = Entry(registrationwindow,textvariable = password)
    Tfpassword.pack(side="top",pady=5)

    bregister = Button(registrationwindow,text="Registrarse",command = register)
    bregister.pack(side="top", pady= 20)

    breturnmain = Button(registrationwindow,text="Regresar",command = returnfromregistration)
    breturnmain.pack(side="top")

    registrationwindow.mainloop()

def register():
    name = Tfname.get()
    lastname = Tflastname.get()
    nickname = Tfnickname.get()
    password = Tfpassword.get()
    if name=="" or lastname=="" or nickname=="" or password=="":
      D = Dialog(None, {'title': 'ERROR',
                      'text':
                      'Debe llenar todos los campos'
                     ,
                      'bitmap': 'warning',
                      'default': 0,
                      'strings': ('Ok',)})
    else:
     save_user(name,lastname,nickname,password)
     Dialog2 = Dialog(None, {'title': 'INFO',
                      'text':
                      'Registro Satisfactorio'
                     ,
                      'bitmap': 'info',
                      'default': 0,
                      'strings': ('Ok',)})
     registrationwindow.withdraw
     mainwindow.wm_deiconify()
     Tfname.delete(0, END)
     Tflastname.delete(0, END)
     Tfnickname.delete(0, END)
     Tfpassword.delete(0,END)

def returnfromregistration():
    registrationwindow.withdraw()
    mainwindow.wm_deiconify()
    Tfname.delete(0, END)
    Tflastname.delete(0, END)
    Tfnickname.delete(0, END)
    Tfpassword.delete(0,END)


def verify():
    nicknamelogin = Tfnicknamelogin.get()
    passwordlogin = Tfpasswordlogin.get()
    if (nicknamelogin=="" or passwordlogin==""):
        D = Dialog(None, {'title': 'ERROR',
                      'text':
                      'Debe llenar todos los campos'
                     ,
                      'bitmap': 'warning',
                      'default': 0,
                      'strings': ('Ok',)})
    else:
      Tfnicknamelogin.delete(0, END)
      Tfpasswordlogin.delete(0, END)

      if(log_on(nicknamelogin,passwordlogin)):
        #o=search_user_score(nickname)
        #score.append(o[1])
        #score.append(o[2])
        print ("Bienvenido al juego")
        Tfnicknamelogin.delete(0, END)
        Tfpasswordlogin.delete(0, END)
      else:
        D1 = Dialog(None, {'title': 'ERROR',
                      'text':
                      'Ud. no esta registrado'
                     ,
                      'bitmap': 'warning',
                      'default': 0,
                      'strings': ('Ok',)})


def showloginwindow():
    mainwindow.withdraw()
    loginwindow.wm_deiconify()
    title2 = Label(loginwindow, image = photo)
    title2.photo = photo
    title2.pack(side="top", pady = 20)

    loginwindow.minsize(230,400)
    loginwindow.maxsize(230,400)
    loginwindow.title('Iniciar Sesion')

    Lnicknamelogin = Label(loginwindow, text ="Nickname:",bg="black",fg="white")
    Lnicknamelogin.pack(side="top",pady=10)
    Tfnicknamelogin.pack(side="top", pady=5)

    Lpasswordlogin = Label(loginwindow,text="Password:",bg="black",fg="white")
    Lpasswordlogin.pack(side="top",pady=10)
    Tfpasswordlogin.pack(side="top",pady=5)

    Blogin =Button(loginwindow, text = "Entrar",command=verify)
    Blogin.pack(side="top",pady = 20)

    Breturn =Button(loginwindow, text = "Regresar",command=returnfromlogin)
    Breturn.pack(side="top",pady = 20)

    loginwindow.mainloop()

def returnfromlogin():
    loginwindow.withdraw()
    mainwindow.wm_deiconify()
    Tfnicknamelogin.delete(0, END)
    Tfpasswordlogin.delete(0,END)

#Main en el cual se declaran todas las variables que usan los entry, las ventanas y sus componentes.
if __name__ == '__main__':
   mainwindow = Tk()
   registrationwindow = Toplevel(background='black')
   loginwindow = Toplevel(background='black')
   name = str()
   lastname = str ()
   nickname = str ()
   password = str ()
   nicknamelogin = str ()
   passwordlogin = str ()
   Tfname= Entry(registrationwindow,textvariable= name)
   Tflastname= Entry(registrationwindow,textvariable= lastname)
   Tfnickname= Entry(registrationwindow,textvariable= nickname)
   Tfpassword= Entry(registrationwindow,textvariable= password,show="*")
   Tfnicknamelogin= Entry(loginwindow,textvariable= nicknamelogin)
   Tfpasswordlogin= Entry(loginwindow,textvariable= passwordlogin,show="*")
   photo = PhotoImage(file="C:/Users/joleon/Desktop/BurgerTime/Proyecto Ingenieria/BurgerTimeLogo.pbm")



   showmainwindow()