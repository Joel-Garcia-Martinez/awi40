import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 

render = web.template.render("mvc/views",base="user_list")

class User_list:
    def GET(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig)
        db = firebase.database()
        users = db.child("users").get()
        return render.user_list(users) 