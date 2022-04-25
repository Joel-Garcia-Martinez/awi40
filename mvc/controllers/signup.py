import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 



class Signup: #crea la clase de inicio de sesion 
    def GET(self): #obtiene el valor
        message = None #crea un condicional #crea un valor nulo
        return render.signup(message)