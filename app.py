import web #importa la libreria web.py
import pyrebase #importa la libreria para el uso de firebase
import firebase_config as token #configura el reconocimiento de token o id en firebase
import json #importa el archivo json 

urls = (
    '/', 'mvc.controllers.welcome.Welcome',
    '/login', 'mvc.controllers.login.Login',
    '/login2', 'mvc.controllers.login.Login2',
    '/signup', 'mvc.controllers.signup.Signup',
    '/welcome', 'mvc.controllers.welcome.Welcome',
    '/welcome2', 'mvc.controllers.welcome2.Welcome2',
    '/logout','mvc.controllers.logout.Logout',
    '/logout2','mvc.controllers.logout2.Logout2',
    '/recover', 'mvc.controllers.recover.Recover', 
    '/principal', 'mvc.controllers.principal.Principal',
    '/dashboard', 'mvc.controllers.dashboard.Dashboard',
    '/dashboard2', 'mvc.controllers.dashboard2.Dashboard2',
    #nos proprciona un diccionario para acceder a los archivos y funciones
)
app = web.application(urls, globals()) #toma las urls de arriba e inicia con la ultima linea de este codigo
render = web.template.render('views') #indica un conteo de las veces que se visita la pagina 
firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()

if __name__ == "__main__": #crea condicion
    web.config.debug = False #hace que no se muestren los errores que no queramos al usuario
    app.run() #corre el app.py
    