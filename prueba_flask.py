#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify
from flask import request

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os
import time
#--------------------------------------------------------------------

app = Flask(__name__) 
CORS(app)

class SistemaPaquetesTuristicos:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
        )
        self.cursor = self.conn.cursor()

# Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS paquetes_turisticos (
                codigo INT,
                descripcion VARCHAR(255) NOT NULL,
                destino VARCHAR(255) NOT NULL,
                duracion VARCHAR(50) NOT NULL,
                alojamiento VARCHAR(255) NOT NULL,
                transporte VARCHAR(255) NOT NULL,
                actividades TEXT,
                precio DECIMAL(10, 2) NOT NULL,
                imagen_url VARCHAR(255),
                proveedor INT
            )
        ''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
      

# --------------------------------------------------------------------------------------------------------------- #

    def listar_paquetes_turisticos(self):
        self.cursor.execute("SELECT * FROM paquetes_turisticos")
        paquetes_turisticos = self.cursor.fetchall()
        return paquetes_turisticos

# --------------------------------------------------------------------------------------------------------------- #

    def consultar_paquete_turistico(self, codigo):
        # Consultamos un paquete turístico a partir de su código
        self.cursor.execute(f"SELECT * FROM paquetes_turisticos WHERE codigo = {codigo}")
        return self.cursor.fetchone()

# --------------------------------------------------------------------------------------------------------------- #

    def mostrar_paquete_turistico(self, codigo):
        # Mostramos los datos de un paquete turístico a partir de su código
        paquete = self.consultar_paquete_turistico(codigo)
        if paquete:
            print("-" * 40)
            print(f"Código.......: {paquete['codigo']}")
            print(f"Descripción..: {paquete['descripcion']}")
            print(f"Destino......: {paquete['destino']}")
            print(f"Duración.....: {paquete['duracion']}")
            print(f"Alojamiento..: {paquete['alojamiento']}")
            print(f"Transporte...: {paquete['transporte']}")
            print(f"Actividades..: {paquete['actividades']}")
            print(f"Precio.......: {paquete['precio']}")
            print(f"Imagen.......: {paquete['imagen_url']}")
            print(f"Proveedor....: {paquete['proveedor']}")
            print("-" * 40)
        else:
            print("Paquete turístico no encontrado.")

#------------------------------------------------------------------------------------------------------------#

    def agregar_paquete_turistico(self, codigo, descripcion, destino, duracion, alojamiento, transporte, actividades, precio, imagen, proveedor):
        # Verificamos si ya existe un paquete turístico con el mismo código
        self.cursor.execute(f"SELECT * FROM paquetes_turisticos WHERE codigo = {codigo}")
        paquete_existe = self.cursor.fetchone()
        if paquete_existe:
            return False

        # Si no existe, agregamos el nuevo paquete turístico a la tabla
        sql = "INSERT INTO paquetes_turisticos (codigo, descripcion, destino, duracion, alojamiento, transporte, actividades, precio, imagen_url, proveedor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (codigo, descripcion, destino, duracion, alojamiento, transporte, actividades, precio, imagen, proveedor)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return True
    
#------------------------------------------------------------------------------------------------------------#

    def modificar_paquete_turistico(self, codigo, nueva_descripcion, nuevo_destino, nueva_duracion, nuevo_alojamiento, nuevo_transporte, nuevas_actividades, nuevo_precio, nueva_imagen, nuevo_proveedor):
        sql = "UPDATE paquetes_turisticos SET descripcion = %s, destino = %s, duracion = %s, alojamiento = %s, transporte = %s, actividades = %s, precio = %s, imagen_url = %s, proveedor = %s WHERE codigo = %s"
        valores = (nueva_descripcion, nuevo_destino, nueva_duracion, nuevo_alojamiento, nuevo_transporte, nuevas_actividades, nuevo_precio, nueva_imagen, nuevo_proveedor, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

#------------------------------------------------------------------------------------------------------------#

    def eliminar_paquete_turistico(self, codigo):
        # Eliminamos un paquete turístico de la tabla a partir de su código  
        self.cursor.execute(f"DELETE FROM paquetes_turisticos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0


########################################## Cuerpo del programa ################################

# Crear una instancia de la clase SistemaPaquetesTuristicos
#sistema_paquetes = SistemaPaquetesTuristicos(host='localhost', user='root', password='', database='viajes')
sistema_paquetes = SistemaPaquetesTuristicos(host='rociogc02.mysql.pythonanywhere-services.com', user='rociogc02', password='Romasoa2070', database='rociogc02$viajes')

# Carpeta para guardar las imagenes
#ruta_destino = 'img/'
ruta_destino = '/home/rociogc02/mysite/img/'

# --------------------------------- Listar paquetes turisticos ---------------------------------

@app.route("/paquetes-turisticos", methods=["GET"])
def listar_paquetes_turisticos():
    paquetes_turisticos = sistema_paquetes.listar_paquetes_turisticos()
    return jsonify(paquetes_turisticos)


# ------------------------ Mostrar un paquete turistico específico -------------------------

@app.route("/paquetes-turisticos/<int:codigo>", methods=["GET"])
def mostrar_paquete_turistico(codigo):
    paquete = sistema_paquetes.consultar_paquete_turistico(codigo)
    if paquete:
        return jsonify(paquete)
    else:
        return "Paquete turístico no encontrado", 404

# ------------------------ Agregar un paquete turístico ----------------------------------

@app.route("/paquetes-turisticos", methods=["POST"])
def agregar_paquete_turistico():
    # Tomo los datos del formulario
    codigo = request.form['codigo']
    descripcion = request.form['descripcion']
    destino = request.form['destino']
    duracion = request.form['duracion']
    alojamiento = request.form['alojamiento']
    transporte = request.form['transporte']
    actividades = request.form['actividades']
    precio = request.form['precio']
    proveedor = request.form['proveedor']
    imagen = request.files['imagen']
    nombre_imagen = secure_filename(imagen.filename)

    #nombre_base, extension = os.path.splitext(nombre_imagen)
    #nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"    
    #imagen.save(os.path.join(ruta_destino, nombre_imagen))

    if sistema_paquetes.agregar_paquete_turistico(codigo, descripcion, destino, duracion, alojamiento, transporte, actividades, precio, nombre_imagen, proveedor):
        nombre_base, extension = os.path.splitext(nombre_imagen)
        nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
        imagen.save(os.path.join(ruta_destino, nombre_imagen))
        return jsonify({"mensaje": "Paquete turístico agregado"}), 201
    else:
        return jsonify({"mensaje": "Paquete turístico ya existe"}), 400


# ------------------------ Modificar un paquete turistico ----------------------------------

@app.route("/paquetes-turisticos/<int:codigo>", methods=["PUT"])
def modificar_paquete_turistico(codigo):
    # Recojo los datos del formulario o payload JSON
    nueva_descripcion = request.form.get("descripcion")
    nuevo_destino = request.form.get("destino")
    nueva_duracion = request.form.get("duracion")
    nuevo_alojamiento = request.form.get("alojamiento")
    nuevo_transporte = request.form.get("transporte")
    nuevas_actividades = request.form.get("actividades")
    nuevo_precio = request.form.get("precio")
    nuevo_proveedor = request.form.get("proveedor")
    
    # Procesamiento de la imagen
    imagen = request.files['imagen']
    nombre_imagen = secure_filename(imagen.filename)
    nombre_base, extension = os.path.splitext(nombre_imagen)
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
    imagen.save(os.path.join(ruta_destino, nombre_imagen))

    # Actualización del paquete turístico
    if sistema_paquetes.modificar_paquete_turistico(
        codigo, nueva_descripcion, nuevo_destino, nueva_duracion,
        nuevo_alojamiento, nuevo_transporte, nuevas_actividades,
        nuevo_precio, nombre_imagen, nuevo_proveedor
    ):
        return jsonify({"mensaje": "Paquete turístico modificado"}), 200
    else:
        return jsonify({"mensaje": "Paquete turístico no encontrado"}), 404

# ------------------------ Eliminar un paquete turístico ----------------------------------

@app.route("/paquetes-turisticos/<int:codigo>", methods=["DELETE"])
def eliminar_paquete_turistico(codigo):
        # Obtengo la información del paquete turístico para encontrar la imagen
    paquete_turistico = sistema_paquetes.consultar_paquete_turistico(codigo)
    
    if paquete_turistico:
        # Elimino la imagen asociada si existe
        ruta_imagen = os.path.join(ruta_destino, paquete_turistico['imagen_url'])
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)

        # Elimino el paquete turístico del listado
        if sistema_paquetes.eliminar_paquete_turistico(codigo):
            return jsonify({"mensaje": "Paquete turístico eliminado"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el paquete turístico"}), 500
    else:
        return jsonify({"mensaje": "Paquete turístico no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)