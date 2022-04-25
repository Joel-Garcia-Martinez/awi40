import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 

render = web.template.render("mvc/views",base="recover")

class Recover:
    def GET(self):
        message = "None"
        return render.recover(message)
    def POST(self):
        try:
            message = "None"
            formulario = web.input()
            email = formulario.email
            auth.send_password_reset_email(email)
            return web.seeother('/login') 
        except Exception as error:
            formato = json.loads(error.args[1])
            error = formato['error']
            message = error['message']
            print("Error recover.POST: {}".format(message))
            return render.recover(message)