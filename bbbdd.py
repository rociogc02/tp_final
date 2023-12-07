import mysql.connector 

class SistemaPaquetesTuristicos:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)
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


    def agregar_paquete_turistico(self, codigo, descripcion, destino, duracion, alojamiento, transporte, actividades, precio, imagen, proveedor):
        self.cursor.execute(f"SELECT * FROM paquetes_turisticos WHERE codigo = {codigo}")
        paquete_existe = self.cursor.fetchone()
        if paquete_existe:
            return False

        sql = f"INSERT INTO paquetes_turisticos (codigo, descripcion, destino, duracion, alojamiento, transporte, actividades, precio, imagen_url, proveedor) VALUES ({codigo}, '{descripcion}', '{destino}', '{duracion}', '{alojamiento}', '{transporte}', '{actividades}', {precio}, '{imagen}', {proveedor})"
        self.cursor.execute(sql)
        self.conn.commit()
        return True

    def consultar_paquete_turistico(self, codigo):
        # Consulto un paquete turístico por su código
        self.cursor.execute(f"SELECT * FROM paquetes_turisticos WHERE codigo = {codigo}")
        return self.cursor.fetchone()


    def modificar_paquete_turistico(self, codigo, nueva_descripcion, nuevo_destino, nueva_duracion, nuevo_alojamiento, nuevo_transporte, nuevas_actividades, nuevo_precio, nueva_imagen, nuevo_proveedor):
        sql = f"""
            UPDATE paquetes_turisticos
            SET descripcion = '{nueva_descripcion}',
                destino = '{nuevo_destino}',
                duracion = '{nueva_duracion}',
                alojamiento = '{nuevo_alojamiento}',
                transporte = '{nuevo_transporte}',
                actividades = '{nuevas_actividades}',
                precio = {nuevo_precio},
                imagen_url = '{nueva_imagen}',
                proveedor = {nuevo_proveedor}
            WHERE codigo = {codigo}
        """
        self.cursor.execute(sql)
        self.conn.commit()
        return self.cursor.rowcount > 0

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

    def listar_paquetes_turisticos(self):
        # Mostramos en pantalla un listado de todos los paquetes turísticos en la tabla
        self.cursor.execute("SELECT * FROM paquetes_turisticos")
        paquetes_turisticos = self.cursor.fetchall()
        print("-" * 40)
        for paquete in paquetes_turisticos:
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

    def eliminar_paquete_turistico(self, codigo):
    # Eliminamos un paquete turístico de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM paquetes_turisticos WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0



###################################### Programa principal ###############################

sistema_paquetes = SistemaPaquetesTuristicos(host='localhost', user='root', password='', database='viajes')

# Agrego 3 productos
sistema_paquetes.agregar_paquete_turistico(
    codigo=1,
    descripcion="Playa Paradisíaca",
    destino="Pinamar",
    duracion="7 días, 6 noches",
    alojamiento="Resort de lujo",
    transporte="Vuelo incluido",
    actividades="Snorkeling, Paseo en barco",
    precio=25000,
    imagen="img/pinamar.jpg",
    proveedor=123
)
sistema_paquetes.agregar_paquete_turistico(
    codigo=2,
    descripcion="Aventura en la montaña",
    destino="Mendoza",
    duracion="5 días, 4 noches",
    alojamiento="Cabaña acogedora",
    transporte="Autobús incluido",
    actividades="Senderismo, Escalada",
    precio=60000,
    imagen="img/mendoza.jpg",
    proveedor=456
)

sistema_paquetes.agregar_paquete_turistico(
    codigo=3,
    descripcion="Exploración en la selva",
    destino="Selva Exuberante",
    duracion="8 días, 7 noches",
    alojamiento="Eco-lodge sostenible",
    transporte="Vuelo privado",
    actividades="Avistaje de aves, Paseo en bote",
    precio=40000,
    imagen="img/selva.jpg",
    proveedor=789
)

# Consulto un producto y lo muestro

codigo_a_consultar = int(input("Ingrese el código del producto que desea consultar: "))
paquete_consultado = sistema_paquetes.consultar_paquete_turistico(codigo_a_consultar)

if paquete_consultado:
    print("Información del paquete turístico:")
    print(f"Código.......: {paquete_consultado['codigo']}")
    print(f"Descripción..: {paquete_consultado['descripcion']}")
    print(f"Destino......: {paquete_consultado['destino']}")
    print(f"Duración.....: {paquete_consultado['duracion']}")
    print(f"Alojamiento..: {paquete_consultado['alojamiento']}")
    print(f"Transporte...: {paquete_consultado['transporte']}")
    print(f"Actividades..: {paquete_consultado['actividades']}")
    print(f"Precio.......: {paquete_consultado['precio']}")
    print(f"Imagen.......: {paquete_consultado['imagen_url']}")
    print(f"Proveedor....: {paquete_consultado['proveedor']}")
else:
    print(f"No se encontró un paquete turístico con código {codigo_a_consultar}.")


# Modificamos un paquete turístico y lo mostramos
sistema_paquetes.mostrar_paquete_turistico(1)
sistema_paquetes.modificar_paquete_turistico(1, 'Paquete de aventura', 'Montañas místicas', '7 días, 6 noches', 'Refugio en la montaña', 'Transporte incluido', 'Senderismo, Escalada', 1400.0, 'aventura.jpg', 900)
sistema_paquetes.mostrar_paquete_turistico(1)

# Listamos todos los paquetes turísticos
sistema_paquetes.listar_paquetes_turisticos()


# Eliminamos un paquete turístico
codigo_a_eliminar = int(input("Ingrese el código del producto que desea eliminar: "))
sistema_paquetes.eliminar_paquete_turistico(codigo_a_eliminar)
# Listamos los paquetes turísticos restantes
sistema_paquetes.listar_paquetes_turisticos()




"""
    def consultar_paquete_turistico(self, codigo):
        for paquete in self.paquetes_turisticos:
            if paquete['codigo'] == codigo:
                return paquete
        return False

    def agregar_paquete_turistico(self, codigo, descripcion, destino, duracion, alojamiento, transporte, actividades, precio, imagen, proveedor):
        if self.consultar_paquete_turistico(codigo):
            return False

        nuevo_paquete = {
            'codigo': codigo,
            'descripcion': descripcion,
            'destino': destino,
            'duracion': duracion,
            'alojamiento': alojamiento,
            'transporte': transporte,
            'actividades': actividades,
            'precio': precio,
            'imagen': imagen,
            'proveedor': proveedor
        }

        self.paquetes_turisticos.append(nuevo_paquete)
        return True
    
    def modificar_paquete_turistico(self, codigo, nueva_descripcion, nuevo_destino, nueva_duracion, nuevo_alojamiento, nuevo_transporte, nuevas_actividades, nuevo_precio, nueva_imagen, nuevo_proveedor):
        for paquete in self.paquetes_turisticos:
            if paquete['codigo'] == codigo:
                paquete['descripcion'] = nueva_descripcion
                paquete['destino'] = nuevo_destino
                paquete['duracion'] = nueva_duracion
                paquete['alojamiento'] = nuevo_alojamiento
                paquete['transporte'] = nuevo_transporte
                paquete['actividades'] = nuevas_actividades
                paquete['precio'] = nuevo_precio
                paquete['imagen'] = nueva_imagen
                paquete['proveedor'] = nuevo_proveedor
                return True
        return False
    
    def listar_paquetes_turisticos(self):
        print("-" * 50)
        for paquete in self.paquetes_turisticos:
            print(f"Código.......: {paquete['codigo']}")
            print(f"Descripción..: {paquete['descripcion']}")
            print(f"Destino......: {paquete['destino']}")
            print(f"Duración.....: {paquete['duracion']}")
            print(f"Alojamiento..: {paquete['alojamiento']}")
            print(f"Transporte...: {paquete['transporte']}")
            print(f"Actividades..: {', '.join(paquete['actividades'])}")
            print(f"Precio.......: {paquete['precio']}")
            print(f"Imagen.......: {paquete['imagen']}")
            print(f"Proveedor....: {paquete['proveedor']}")
            print("-" * 50)

    def eliminar_paquete_turistico(self, codigo):
        for paquete in self.paquetes_turisticos:
            if paquete['codigo'] == codigo:
                self.paquetes_turisticos.remove(paquete)
                return True
        return False
    
    def mostrar_paquete_turistico(self, codigo):
        paquete = self.consultar_paquete_turistico(codigo)
        if paquete:
            print("-" * 50)
            print(f"Código.......: {paquete['codigo']}")
            print(f"Descripción..: {paquete['descripcion']}")
            print(f"Destino......: {paquete['destino']}")
            print(f"Duración.....: {paquete['duracion']}")
            print(f"Alojamiento..: {paquete['alojamiento']}")
            print(f"Transporte...: {paquete['transporte']}")
            print(f"Actividades..: {', '.join(paquete['actividades'])}")
            print(f"Precio.......: {paquete['precio']}")
            print(f"Imagen.......: {paquete['imagen']}")
            print(f"Proveedor....: {paquete['proveedor']}")
            print("-" * 50)
        else:
            print("Paquete turístico no encontrado.")

"""

###################### Para probar la función agregar_paqute_turistico ######################################

"""
def probar_sistema_paquetes():
    sistema_paquetes = SistemaPaquetesTuristicos()
    codigo = "PT001"
    descripcion = "Paquete turístico a la playa"
    destino = "Playa Paradisíaca"
    duracion = "5 días, 4 noches"
    alojamiento = "Resort de lujo"
    transporte = "Vuelo incluido"
    actividades = ["Tour en barco", "Esquí acuático"]
    precio = 1500.0
    imagen = "url_imagen.jpg"
    proveedor = "Compañía Turística XYZ"

    if sistema_paquetes.agregar_paquete_turistico(codigo, descripcion, destino, duracion, alojamiento, transporte, actividades, precio, imagen, proveedor):
        print("Paquete turístico agregado con éxito.")
    else:
        print("El paquete turístico ya existe.")

    # Intenta agregar el mismo paquete nuevamente (debería mostrar que ya existe)
    if sistema_paquetes.agregar_paquete_turistico(codigo, descripcion, destino, duracion, alojamiento, transporte, actividades, precio, imagen, proveedor):
        print("Paquete turístico agregado con éxito.")
    else:
        print("El paquete turístico ya existe.")

    # Muestra la lista de paquetes turísticos en el sistema
    print("Lista de paquetes turísticos:")
    for paquete in sistema_paquetes.paquetes_turisticos:
        print(paquete)

# Ejecuta la función de prueba
probar_sistema_paquetes()

"""

########################## Para probar la función modificar_paquete_turistico ################################

"""
# Crea una instancia de la clase SistemaPaquetesTuristicos
sistema_paquetes = SistemaPaquetesTuristicos()

# Agrega un paquete turístico para tener algo que modificar
codigo = "PT001"
descripcion = "Paquete turístico a la playa"
destino = "Playa Paradisíaca"
duracion = "5 días, 4 noches"
alojamiento = "Resort de lujo"
transporte = "Vuelo incluido"
actividades = ["Tour en barco", "Esquí acuático"]
precio = 1500.0
imagen = "url_imagen.jpg"
proveedor = "Compañía Turística XYZ"

sistema_paquetes.agregar_paquete_turistico(codigo, descripcion, destino, duracion, alojamiento, transporte, actividades, precio, imagen, proveedor)

# Muestra la información antes de la modificación
print("Antes de la modificación:")
print(sistema_paquetes.paquetes_turisticos)

# Modifica el paquete turístico
nueva_descripcion = "Paquete turístico a la isla"
nuevo_destino = "Isla Exótica"
nueva_duracion = "7 días, 6 noches"
nuevo_alojamiento = "Hotel Boutique"
nuevo_transporte = "Vuelo privado"
nuevas_actividades = ["Snorkeling", "Excursión en jeep"]
nuevo_precio = 2000.0
nueva_imagen = "nueva_url_imagen.jpg"
nuevo_proveedor = "Compañía Turística ABC"

if sistema_paquetes.modificar_paquete_turistico(codigo, nueva_descripcion, nuevo_destino, nueva_duracion, nuevo_alojamiento, nuevo_transporte, nuevas_actividades, nuevo_precio, nueva_imagen, nuevo_proveedor):
    print("Modificación exitosa.")
else:
    print("El paquete turístico no fue encontrado.")

# Muestra la información después de la modificación
print("Después de la modificación:")
print(sistema_paquetes.paquetes_turisticos)

"""

###################### Para probar la función listar_paqute_turistico ######################################

"""
# Creo un sistema de paquetes turísticos
sistema_paquetes = SistemaPaquetesTuristicos()

# Agrego algunos paquetes turísticos de prueba
sistema_paquetes.agregar_paquete_turistico("PT001", "Paquete a la playa", "Playa Soleada", "7 días", "Resort de lujo", "Vuelo incluido", ["Snorkeling", "Paseo en barco"], 1500.0, "imagen1.jpg", "Compañía Turística A")
sistema_paquetes.agregar_paquete_turistico("PT002", "Paquete a la montaña", "Montañas Verdes", "5 días", "Cabaña acogedora", "Autobús incluido", ["Senderismo", "Escalada"], 1200.0, "imagen2.jpg", "Compañía Turística B")

# Listo los paquetes turísticos
sistema_paquetes.listar_paquetes_turisticos()

"""

###################### Para probar la función eliminar_paqute_turistico ######################################

"""
# Creo un sistema de paquetes turísticos
sistema_paquetes = SistemaPaquetesTuristicos()

# Agrego algunos paquetes turísticos de prueba
sistema_paquetes.agregar_paquete_turistico("PT001", "Paquete a la playa", "Playa Soleada", "7 días", "Resort de lujo", "Vuelo incluido", ["Snorkeling", "Paseo en barco"], 1500.0, "imagen1.jpg", "Compañía Turística A")
sistema_paquetes.agregar_paquete_turistico("PT002", "Paquete a la montaña", "Montañas Verdes", "5 días", "Cabaña acogedora", "Autobús incluido", ["Senderismo", "Escalada"], 1200.0, "imagen2.jpg", "Compañía Turística B")

# Listo los paquetes turísticos
sistema_paquetes.listar_paquetes_turisticos()

# Elijo el código a eliminar#
codigo_a_eliminar = "PT002"

if sistema_paquetes.eliminar_paquete_turistico(codigo_a_eliminar):
    print(f"Paquete turístico con código {codigo_a_eliminar} eliminado con éxito.")
else:
    print(f"No se encontró un paquete turístico con código {codigo_a_eliminar}.")

# Listo los paquetes turísticos nuevamente para ver si se borró
sistema_paquetes.listar_paquetes_turisticos()

"""

###################### Para probar la función mostrar_paqute_turistico ######################################

"""
# Creo un sistema de paquetes turísticos
sistema_paquetes = SistemaPaquetesTuristicos()

# Agrego algunos paquetes turísticos de prueba
sistema_paquetes.agregar_paquete_turistico("PT001", "Paquete a la playa", "Playa Soleada", "7 días", "Resort de lujo", "Vuelo incluido", ["Snorkeling", "Paseo en barco"], 1500.0, "imagen1.jpg", "Compañía Turística A")
sistema_paquetes.agregar_paquete_turistico("PT002", "Paquete a la montaña", "Montañas Verdes", "5 días", "Cabaña acogedora", "Autobús incluido", ["Senderismo", "Escalada"], 1200.0, "imagen2.jpg", "Compañía Turística B")

# Elijo el código a mostrar#
codigo_a_mostrar = "PT001"

sistema_paquetes.mostrar_paquete_turistico(codigo_a_mostrar)

"""