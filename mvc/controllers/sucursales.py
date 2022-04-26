import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 

render = web.template.render("mvc/views",base="sucursales")

class Sucursales: 
    def GET(self): 
        message = None 
        return render.sucursales(message) 

    def POST(self): 
        try: 
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            auth = firebase.auth()
            db=firebase.database()
            formulario = web.input() #indica un formulario que el usuario puede rellenar 
            numsuc = formulario.numsuc 
            ubicacion = formulario.ubicacion 
            apertura = formulario.apertura
            temperatura = formulario.temperatura
            humedad = formulario.humedad
            sistema = formulario.sistema
            email = formulario.email #interpreta el email formulario
            password = formulario.password #interpreta la cotrasena del formulario
            print(email, password) #imprime contrasena y usuario insertados
            user = auth.sign_in_with_email_and_password(email, password) #indica que el usuario es la informacion del formulario
            print(user['localId']) #nos imprime el id del usuario

            data = {
                "Numero de sucursal": numsuc,
                "Ubicacion": ubicacion,
                "Fecha de apertura": apertura,
                "Temperatura": temperatura,
                "Humedad": humedad,
                "Sistema de enfriamiento": sistema,
                "Administrador que la creo": email,
                "Contrasena": password,
            }
            datitos = db.child("sucursales").child(user['localId']).set(data)
            return web.seeother("/welcome") #si es valido nos envia al html
        except Exception as error: #a menos que
            formato = json.loads(error.args[1]) #toma el argumento con la posicion 1 del arreglo de errores
            error = formato['error'] #indica que existe un error
            message = error['message'] #muestra el mensaje con el error
            return render.sucursales(message)