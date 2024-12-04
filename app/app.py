#IMPORTAMOS LAS LIBRERIAS NECESARIAS PARA EL PROYECTO
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from psycopg2.extensions import AsIs
#---------------------------------------------------------------------

# CONFIGURAR LA BASE DE DATOS 
def db_paola():
    return psycopg2.connect(
        dbname="nineras",
        user="postgres",
        password="Abcd128910",
        host="localhost"
    )  
#---------------------------------------------------------------------

app = Flask(__name__)

#CONSULTAS Y MODIFICACIONES A LA BASE DE DATOS
def consultar_registros(nombre):
    connection = None
    try:
        connection = db_paola()

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM %s", (AsIs(nombre),))
            consulta = cursor.fetchall()
            return consulta
    except Exception as e:
        print("Ocurrió un error inesperado:", e)
        return []
    finally:
        if connection:
            connection.close()
 #---------------------------------------------------------------------
            
#ESTABLECEMOS RUTAS Y RENDERIZAMOS UN ARCHIVO HTML
@app.route('/')
def home():
    lista_nineras = ['Paola', 'Maria', 'Carmen']
    items = [
        {
            'imagen_url': 'static/img/paola.jpg',
            'nombre_ninera': lista_nineras[0],
            'descripcion': 'Se encarga de la seguridad y bienestar de los niños, ofreciendo un ambiente seguro y amoroso. Supervisa actividades, prepara comidas y ayuda con las tareas escolares.',
            'boton': f'Conoce a {lista_nineras[0]}'
        },
        {
            'imagen_url': 'static/img/maria.jpg',
            'nombre_ninera': lista_nineras[1],
            'descripcion': 'Organiza actividades lúdicas y educativas, fomentando la creatividad y el desarrollo de habilidades sociales. Planifica juegos, manualidades y paseos al aire libre.',
            'boton': f'Conoce a {lista_nineras[1]}'
        },
        {
            'imagen_url': 'static/img/carmen.jpg',
            'nombre_ninera': lista_nineras[2],
            'descripcion': 'Capaz de ajustarse a diferentes horarios y necesidades familiares. Proporciona apoyo en diversas tareas del hogar, además de cuidar de los niños con cariño y atención.',
            'boton': f'Conoce a {lista_nineras[2]}'
        }
    ]
    data = {
        'titulo': 'Niñeras',
        'bienvenida': 'Bienvenidos, aquí puede revisar el historial de cualquiera de nuestras niñeras',
        'nineras': lista_nineras,
        'numero_nineras': len(lista_nineras)
    }
    return render_template("index.html", data=data, items=items)

@app.route('/nineras/<nombre>')
def nineras(nombre):
    registros = consultar_registros(nombre)
    print(registros) 
    name_column ={
        'paola': ['#', 'nombre', 'edad', 'ciudad', 'sexo', 'ninera_id'],
        'maria': ['#', 'nombre', 'edad', 'ciudad', 'sexo', 'ninera_id'],
        'carmen': ['#', 'nombre', 'edad', 'ciudad', 'sexo', 'ninera_id']
    }
    columnas = name_column.get(nombre.lower(), [])
    detalle_ninera = {
        'nombre': nombre,
        'descripcion': 'Esta es la niñera ' + nombre,
        'imagen_url': f'static/img/{nombre.lower()}.jpg'
    }
    data = {
        'titulo': 'niñeras',
        'nombre': nombre,
        'detalle_ninera': detalle_ninera,
        'registros': registros,
        'columnas': columnas
    }
    return render_template("nineras.html", data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    return "Muy bien"

def pagina_no_encontrada(error):
    data = {
        'titulo': 'no encontrado',
        'descripcion': 'La página a la que intenta acceder no se encontró, por favor revise su búsqueda'
    }
    return render_template('404.html', data=data), 404

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)
