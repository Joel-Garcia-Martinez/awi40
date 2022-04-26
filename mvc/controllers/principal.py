import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 

render = web.template.render("mvc/views",base="principal")

class Principal: #genera la clase verificar 
    def GET(self):
        try:#Se intenta con este codigo
            if web.cookies().get('localId') == "None" : #se verifica si nuestra cookie contiene algun dato
                return web.seeother("/login")#si nuestra cookie esta vacia, nos direccionara a la pagina de login
            elif web.cookies().get('localId') == None : #se verifica si nuestra cookie contiene algun dato
                return web.seeother("/login")#si nuestra cookie esta vacia, nos direccionara a la pagina de login
            else:
                return render.principal()
        except Exception as error:
            print("Error Inicio.GET: {}".format(error))

    def POST(self): #devuelve el valor
        formulario = web.input() #indica que el usuario insertara los datos
        email = formulario.email #email tiene el valor email
        password = formulario.password #contrasena toma el valor de contrasena 
        print(email, password) #imprime usuario y contrasena 
        return render.login() #verifica y devuelve un output