import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 

render = web.template.render("mvc/views/",base="welcome2")

class Welcome2: #genera la clase bienvenido para mostrar al usuario en caso de acceder exitosamente 
    def GET(self): #obtiene el valor 
        mycookie = web.cookies().get("cookie")
        if mycookie != "None":
            return render.welcome2()
        elif mycookie == None:
            return web.seeother("/login")
        else:
            return web.seeother("/login")