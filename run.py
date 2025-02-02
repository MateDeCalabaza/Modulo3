from flask import Flask

#Crear una instancia de la clase Flask, llamada "app"
app = Flask(__name__)

#Crear rutas con sus correspondientes funciones
#En flask, a los decoradores se los conoce como "pocesador de contexto" y lo que sigue se trata de una RUTA. Lo que hicimos acá es llamar a un método de la instancia "app"
#Entre paréntesis se pone una barra invertida como parámetro, indicando que es la ruta inicial, es decir, la
#página de incio. Al lado se pone como argumento los tipos de solicitudes que puede hacerle el cliente al servidor, para luego otorgarle una respuesta. Luego se genera una función que determina qué sucederá al ingresar a esa URL.
#Existen muchos tipos de solicitudes: GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONs, TRACE o PATCH 
@app.route('/', methods=["GET"])
def holamundo():
    return 'Hola Mundo!'

#Acá agregamos otra ruta, que como vemos dentro del paréntesis, tiene su dirección dentro de la ruta inicial.
@app.route('/mis-proyectos', methods=["GET"])
def mostrarproyectos():
    return 'Aquí se mostrarán mis proyectos'

#Ejecutar nuestra app cuando ejecutemos este archivo run.py
#A su vez, al ejecutar en modo "debug=true" lo estamos haciendo en modo de desarrollo
#Los parámetros que se utilizan son el host, el puerto y si lo usamos en modo debug o no.
if __name__ == '__main__':
    app.run(debug=True)