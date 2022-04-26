import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 

render = web.template.render("mvc/views",base="login")

class Login: #crea la clase de inicio de sesion 
    def GET(self): #obtiene el valor
        message = None #crea un condicional #crea un valor nulo
        return render.login(message) #indica un inicio de sesion exitoso

    def POST(self): #devuelve el valor
        try: #crea un condicional
            firebase = pyrebase.initialize_app(token.firebaseConfig) #inicializa los id de firebase
            auth = firebase.auth()
            db = firebase.database()
            formulario = web.input() #indica un formulario que el usuario puede rellenar 
            email = formulario.email #interpreta el email formulario
            password = formulario.password #interpreta la cotrasena del formulario
            print(email, password) #imprime contrasena y usuario insertados
            user = auth.sign_in_with_email_and_password(email, password) #indica que el usuario es la informacion del formulario
            print(user['localId']) #nos imprime el id del usuario
            web.setcookie('cookie', user['localId'])
            
            datitos = db.child("users").child(user['localId']).get()
            print(datitos.val())
            if datitos.val()['nivel'] == 'administrador' and datitos.val()['estatus'] == 'activo':
                return web.seeother("/welcome")
            elif datitos.val()['nivel'] == 'operador' and datitos.val()['estatus'] == 'activo':
                return web.seeother("/welcome2") 
            else:
                message = 'Cuenta deshabilitada'
                return render.login(message)

            return web.seeother("/welcome") #si es valido nos envia al html
        except Exception as error: #a menos que
            formato = json.loads(error.args[1]) #toma el argumento con la posicion 1 del arreglo de errores
            error = formato['error'] #indica que existe un error
            message = error['message'] #muestra el mensaje con el error
            return render.login(message)