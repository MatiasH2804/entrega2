import json # Importamos un archivo.json donde se van a almacenar los datos

# Vamos a definir la clase cliente, colocando los parametros para comprar
class Cliente: 
    def __init__(self, nombre, usuario, telefono, email):
        self.nombre = nombre
        self.usuario = usuario
        self.telefono = telefono
        self.email = email

    def actualizar_telefono(self, nuevo_telefono):
        """Actualiza el número de teléfono del cliente."""
        self.telefono = nuevo_telefono

    def actualizar_email(self, nuevo_email):
        """Actualiza el correo electrónico del cliente."""
        self.email = nuevo_email

    def __str__(self):
        """Devuelve una representación en cadena del objeto."""
        return f" los datos almacenados, indican que el cliente es Cliente: {self.nombre}, con Usuario: {self.usuario}, Teléfono: {self.telefono}, y su Email: {self.email}"

# Solicitar los datos del usuario
nombre = input("Introduce tu nombre: ")
usuario = input("Introduce tu usuario: ")
telefono = input("Introduce tu número de teléfono: ")
email = input("Introduce tu email: ")

# Crear una instancia de Cliente con los datos proporcionados
cliente = Cliente(nombre, usuario, telefono, email)

# Imprimir los datos almacenados 
print(cliente)

# Crear el diccionario para almacenar la información de usuario
datos_usuario = {
    "nombre": cliente.nombre,
    "usuario": cliente.usuario,
    "telefono": cliente.telefono,
    "email": cliente.email
}

# Exportar los datos del usuario a un archivo JSON
archivo_usuario = 'datos_usuario.json'
with open(archivo_usuario, 'w') as file:
    json.dump(datos_usuario, file)
# Como última accion del primer paso, nos devuelve un texto que nos indica donde fueron guardados los datos
print(f"Los datos del usuario han sido guardados en el archivo {archivo_usuario}")

# Una vez tengo datos del usuario, vamos a Solicitar información sobre la compra
cantidad_objetos = input("¿Cuántos objetos desea comprar?: ")
objeto = input("¿Qué objeto desea comprar?: ")
lugar_compra = input("¿Dónde desea comprarlo?: ")

# Creamos el diccionario para almacenar la información de la compra
datos_compra = {
    "usuario": usuario,
    "cantidad_objetos": cantidad_objetos,
    "objeto": objeto,
    "lugar_compra": lugar_compra
}

# Exportar los datos de la compra a un archivo JSON
archivo_compra = 'datos_compra.json'
with open(archivo_compra, 'w') as file:
    json.dump(datos_compra, file)

print(f"Los datos de la compra han sido guardados en el archivo {archivo_compra}")

# Imprimir el mensaje final, una vez realizada la compra
print(f"El usuario {usuario} ha comprado {cantidad_objetos} {objeto}(s) en {lugar_compra}.")

