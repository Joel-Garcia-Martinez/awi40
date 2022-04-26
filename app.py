import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 

urls = (
    '/', 'Welcome',
    '/login', 'Login',
    '/login2', 'Login2',
    '/signup', 'Signup',
    '/welcome', 'Welcome',
    '/welcome2', 'Welcome2',
    '/logout','Logout',
    '/logout2','Logout2',
    '/recover', 'Recover', 
    '/principal', 'Principal',
    '/dashboard', 'Dashboard',
    '/dashboard2', 'Dashboard2',
    '/sucursales', 'Sucursales',
    '/user_list', 'User_list', 
    '/user_update(.*)', 'User_update',
    #nos proprciona un diccionario para acceder a los archivos y funciones
)
app = web.application(urls, globals()) #toma las urls de arriba e inicia con la ultima linea de este codigo
render = web.template.render('views') #indica un conteo de las veces que se visita la pagina 
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()

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

class Login2: #crea la clase de inicio de sesion 
    def GET(self): #obtiene el valor
        message = None #crea un condicional #crea un valor nulo
        return render.login2(message) #indica un inicio de sesion exitoso

    def POST(self): #devuelve el valor
        try: #crea un condicional
            firebase = pyrebase.initialize_app(token.firebaseConfig) #inicializa los id de firebase
            auth = firebase.auth()
             #extrae los usuarios registrados en firebase
            formulario = web.input() #indica un formulario que el usuario puede rellenar 
            email = formulario.email #interpreta el email formulario
            password = formulario.password #interpreta la cotrasena del formulario
            print(email, password) #imprime contrasena y usuario insertados
            user = auth.sign_in_with_email_and_password(email, password) #indica que el usuario es la informacion del formulario
            print(user['localId']) #nos imprime el id del usuario
            web.setcookie('cookie', user['localId'])
            return web.seeother("/welcome2") #si es valido nos envia al html
        except Exception as error: #a menos que
            formato = json.loads(error.args[1]) #toma el argumento con la posicion 1 del arreglo de errores
            error = formato['error'] #indica que existe un error
            message = error['message'] #muestra el mensaje con el error
            return render.login2(message)

class Logout:
    def GET(self):
        web.setcookie("cookie", "None")
        return web.seeother("/login")

class Logout2:
    def GET(self):
        web.setcookie("cookie", "None")
        return web.seeother("/login2")

class Welcome: #genera la clase bienvenido para mostrar al usuario en caso de acceder exitosamente 
    def GET(self): #obtiene el valor 
        mycookie = web.cookies().get("cookie")
        if mycookie != "None":
            return render.welcome()
        elif mycookie == None:
            return web.seeother("/login")
        else:
            return web.seeother("/login")

class Welcome2: #genera la clase bienvenido para mostrar al usuario en caso de acceder exitosamente 
    def GET(self): #obtiene el valor 
        mycookie = web.cookies().get("cookie")
        if mycookie != "None":
            return render.welcome2()
        elif mycookie == None:
            return web.seeother("/login")
        else:
            return web.seeother("/login")

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

class Signup: #crea la clase de inicio de sesion 
    def GET(self): #obtiene el valor
        message = None #crea un condicional #crea un valor nulo
        return render.signup(message) #indica un inicio de sesion exitoso

    def POST(self): #devuelve el valor
        try: #crea un condicional
            firebase = pyrebase.initialize_app(token.firebaseConfig) #inicializa los id de firebase
            auth = firebase.auth()
            db=firebase.database()
            formulario = web.input() #indica un formulario que el usuario puede rellenar 
            nombre = formulario.nombre
            telefono = formulario.telefono
            nivel = formulario.nivel
            estatus = formulario.estatus 
            email = formulario.email #interpreta el email formulario
            password = formulario.password #interpreta la cotrasena del formulario
            print(email, password) #imprime contrasena y usuario insertados
            user = auth.sign_in_with_email_and_password(email, password) #indica que el usuario es la informacion del formulario
            print(user['localId']) #nos imprime el id del usuario

            data = {
                "nombre": nombre,
                "telefono": telefono,
                "nivel": nivel,
                "estatus": estatus,
                "email": email,
                "password": password,
            }
            datitos = db.child("users").child(user['localId']).set(data)
            return web.seeother("/welcome") #si es valido nos envia al html
        except Exception as error: #a menos que
            formato = json.loads(error.args[1]) #toma el argumento con la posicion 1 del arreglo de errores
            error = formato['error'] #indica que existe un error
            message = error['message'] #muestra el mensaje con el error
            return render.signup(message)
        
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

class Dashboard: #genera la clase verificar 
    def GET(self): #obtiene el valor
        return render.dashboard()

class Dashboard2: #genera la clase verificar 
    def GET(self): #obtiene el valor
        return render.dashboard2()

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

class User_list:
    def GET(self):
        firebase = pyrebase.initialize_app(token.firebaseConfig)
        db = firebase.database()
        users = db.child("users").get()
        return render.user_list(users) 

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

if __name__ == "__main__": #crea condicion
    web.config.debug = False #hace que no se muestren los errores que no queramos al usuario
    app.run() #corre el app.py
