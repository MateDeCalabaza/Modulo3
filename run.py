from flask import Flask, render_template, request

#Crear una instancia de la clase Flask, llamada "app"
app = Flask(__name__)

#Crear rutas con sus correspondientes funciones:
#En flask, a los decoradores se los conoce como "pocesador de contexto" y lo que sigue se trata de una RUTA. Lo que hicimos acá es llamar a un método de la instancia "app".
#Entre paréntesis se pone una barra invertida como parámetro, indicando que es la ruta inicial, es decir, la
#página de incio. Al lado se pone como argumento los tipos de solicitudes que puede hacerle el cliente al servidor, para luego otorgarle una respuesta. Luego se genera una función que determina qué sucederá al ingresar a esa URL, en este caso se utiliza la función "render_template" para redirigir a el archivo "index.html" que se encuentra dentro de la carpeta "templates".
#Existen muchos tipos de solicitudes: GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONs, TRACE o PATCH 

#INICIO
@app.route('/', methods=["GET", "POST"])
def index():
    #Importamos el módulo request para poder específicar qué hacer frente a distintos tipos de solicitudes
    if request.method == "POST":
        #almacena los datos del campo «Nombre» del formulario en la variable «nombre». Luego recargamos la página (mediante el return) pero pasando la variable "nombre" como argumento.
        nombre = request.form["Nombre"]
        return render_template("/index.html", nombre = nombre)
    else:
        return render_template("/index.html")

#MIS PROYECTOS
@app.route('/mis-proyectos', methods=["GET"])
def mostrarproyectos():
    return render_template("/mis_proyectos.html")

#CONTACTO
@app.route("/contacto", methods=["GET"])
def contacto():
    return render_template("/contacto.html")

#BLOG
@app.route("/blog", methods=["GET"])
def mi_blog():
    return render_template("/blog.html")


#Ejecutar nuestra app cuando ejecutemos este archivo run.py
#A su vez, al ejecutar en modo "debug=true" lo estamos haciendo en modo de desarrollo
#Los parámetros que se utilizan son el host, el puerto y si lo usamos en modo debug o no.
if __name__ == '__main__':
    app.run(debug=True)