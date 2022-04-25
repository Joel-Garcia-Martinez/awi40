import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 

render = web.template.render("mvc/views",base="dashboard2")

class Dashboard2: #genera la clase verificar 
    def GET(self): #obtiene el valor
        return render.dashboard2()