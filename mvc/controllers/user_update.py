import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 

render = web.template.render("mvc/views",base="user_update")

class User_update:
    def GET(self, localId):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            db = firebase.database()
            user = db.child("users").child(localId).get()
            return render.user_update(user) 
        except Exception as error:
            print("Error user update.GET: {}".format(error))
    def POST(self, localId):
        try: 
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            db = firebase.database()
            formulario = web.input()
            telefono = formulario.telefono
            nivel = formulario.nivel
            estatus = formulario.estatus
            data = {
                "telefono": telefono,
                "nivel": nivel,
                "estatus": estatus, 
            }
            db.child("users").child(localId).update(data)
            return web.seeother("/user_list") 
        except Exception as error:
            print("Error user update.GET: {}".format(error))