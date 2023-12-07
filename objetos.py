class SistemaPaquetesTuristicos:
    def __init__(self):
        self.paquetes_turisticos = []

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