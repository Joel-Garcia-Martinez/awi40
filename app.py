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
             #extrae los usuarios registrados en firebase
            formulario = web.input() #indica un formulario que el usuario puede rellenar 
            email = formulario.email #interpreta el email formulario
            password = formulario.password #interpreta la cotrasena del formulario
            print(email, password) #imprime contrasena y usuario insertados
            user = auth.sign_in_with_email_and_password(email, password) #indica que el usuario es la informacion del formulario
            print(user['localId']) #nos imprime el id del usuario
            web.setcookie('cookie', user['localId'])
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
             #extrae los usuarios registrados en firebase
            formulario = web.input() #indica un formulario que el usuario puede rellenar 
            email = formulario.email #interpreta el email formulario
            password = formulario.password #interpreta la cotrasena del formulario
            print(email, password) #imprime contrasena y usuario insertados
            user = auth.sign_in_with_email_and_password(email, password) #indica que el usuario es la informacion del formulario
            print(user['localId']) #nos imprime el id del usuario

            data = {
                "email": email,
                "password": password
            }
            results = db.child("users").child(user['localId']).set(data)
            return web.seeother("/welcome") #si es valido nos envia al html
        except Exception as error: #a menos que
            formato = json.loads(error.args[1]) #toma el argumento con la posicion 1 del arreglo de errores
            error = formato['error'] #indica que existe un error
            message = error['message'] #muestra el mensaje con el error
            return render.signup(message)
        
class Principal: #genera la clase verificar 
    def GET(self): #obtiene el valor
        return render.principal()

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

if __name__ == "__main__": #crea condicion
    web.config.debug = False #hace que no se muestren los errores que no queramos al usuario
    app.run() #corre el app.py
    