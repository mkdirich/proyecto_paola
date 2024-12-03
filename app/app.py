from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)

#Configurar la base de datos

def db_paola():
    return psycopg2.connect(
        dbname="paola",
        user="postgres",
        password="Abcd128910",
        host="localhost"
    )
    
def consultar_registros(tabla):
    try:
        connection = db_paola()
        
        tablas_permitidas = ['paola', 'maria', 'carmen']
        if tabla not in tablas_permitidas:
            raise ValueError("El nombre de la tabla no está permitido.")
        
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {tabla}"
            cursor.execute(sql)
            consulta = cursor.fetchall()
            for x in consulta:
                print(x)
    except Exception as e:
        print("Ocurrio un error inesperado")
    finally:
        if connection:
            connection.close()
            

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
    data={
        'titulo': 'Niñeras',
        'bienvenida': 'Bienvenidos, aqui puede revisar el historial de cualquiera de nuestras niñeras',
        'nineras' : lista_nineras,
        'numero_nineras' : len(lista_nineras)
    }
    return render_template("index.html", data=data, items=items)

@app.before_request
def before_request():
    print("Antes de la peticion")
    
@app.after_request
def after_request(response):
    print("Despues de la peticion")
    return response

@app.route('/consultar_niño/<nombre>') 
def consultar_niño(nombre): 
    # Lógica para consultar niños
    return render_template("consultar_niño.html", nombre=nombre)

@app.route('/nineras/<nombre>')
def nineras(nombre):
    detalle_ninera = {
        'nombre': nombre,
        'descripcion': 'Esta es la ninera ' + nombre,
        'imagen_url': f'static/img/{nombre.lower()}.jpg'
    }
    data={
        'titulo': 'nineras',
        'nombre': nombre,
        'detalle_ninera': detalle_ninera
    }
    return render_template("nineras.html", data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    return "Muy bien "

def pagina_no_encontrada(error):
    data={
        'titulo': 'no encontrado',
        'descripcion': 'La pagina a la que intenta acceder no se encontro por favor revise su busqueda'
    }
    return render_template('404.html', data=data), 404

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)
    