import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 



class Dashboard: #genera la clase verificar 
    def GET(self): #obtiene el valor
        return render.dashboard()