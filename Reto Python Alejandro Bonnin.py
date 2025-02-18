
# EJECICIO 1

def contar_caracteres(cadena):
    return len(cadena)

# EJERCICIO 2

def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# EJERCICIO 3

def encontrar_duplicado(lista):
    seen = set()
    for elemento in lista:
        if elemento in seen:
            return elemento
        seen.add(elemento)
    return None

# EJERCICIO 4

def enmascarar_datos(variable):

    cadena = str(variable)
    if len(cadena) > 4:
        return '#' * (len(cadena) - 4) + cadena[-4:]
    else:
        return cadena

# EJERCICIO 5

def es_anagrama(palabra1, palabra2):

    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()

    return sorted(palabra1) == sorted(palabra2)


# EJERCICIO 6

def buscar_nombre():

    nombres = ["Jaime", "Silvia", "Ana"]

    nombre_buscado = input("Introduce el nombre que deseas buscar: ")

    if nombre_buscado in nombres:
        print(f"El nombre '{nombre_buscado}' fue encontrado en la lista.")
    else:
        raise ValueError(f"El nombre '{nombre_buscado}' no se encuentra en la lista.")


# EJERCICIO 7

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# EJERCICIO 8

def encontrar_puesto_empleado(nombre_completo, lista):
    try:
        nombre, apellido = nombre_completo.split()
    except:
        return f"{nombre_completo} no trabaja aquí"
    for elemento in lista:
        if nombre == elemento["nombre"] and apellido == elemento["apellido"]:
            return elemento["puesto"]
    return f"{nombre_completo} no trabaja aquí"

empleados = [
    {'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
    {'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
    {'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}
]

# EJERCICIO 9

def cubo_numero(numero):
    return (lambda x: x ** 3)(numero)

# EJERCICIO 10


resto_division = lambda a, b: a % b

# EJERCICIO 11

lista_numeros = [24, 56, 2.3, 19, -1, 0]
numeros_pares = list(filter(lambda x : x % 2 == 0, lista_numeros))
print(numeros_pares)

# EJERCICIO 12


lista_numeros = [24, 56, 2.3, 19, -1, 0]
numeros_suma = list(map(lambda x: x + 3, lista_numeros))

print(numeros_suma)

# EJERCICIO 13

lista_numeros_1 = [1, 4, 5, 6 , 7 , 7]
lista_numeros_2 = [3, 11, 34, 56]
sumar_listas = lambda lista1, lista2: [x + y for x,y in zip(lista1, lista2)]

print(sumar_listas(lista_numeros_1, lista_numeros_2)) 

# EJERCICIO 14

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición inválida para quitar la rama.")

    def info_arbol(self):
        return f"Tronco: {self.tronco}, Número de ramas: {len(self.ramas)}, Longitudes de las ramas: {self.ramas}"


arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()

arbol.quitar_rama(2)


info = arbol.info_arbol()
print(info)

# EJERCICIO 15

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad}.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad  

    def __str__(self):
        return f"{self.nombre} - Saldo: {self.saldo}, Cuenta Corriente: {self.cuenta_corriente}"

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

alicia.agregar_dinero(20)
bob.transferir_dinero(alicia, 80)

try:
    alicia.retirar_dinero(50)
except ValueError as e:
    print(e)

print(alicia)
print(bob)

# EJERCICIO 16

def contar_palabras(texto):
    conteo = {}
    palabras = texto.lower().split()
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

def reemplazar_palabra(texto, palabra_original, palabra_nueva):

    resultado = []
    palabras = texto.lower().split()
    for palabra in palabras:
        if palabra == palabra_original:
            resultado.append(palabra_nueva)
        else:
            resultado.append(palabra)

    return ' '.join(resultado)

def eliminar_palabra(texto, palabra_eliminar):

    palabras = texto.lower().split()
    resultado = []
    for palabra in palabras:
        if palabra != palabra_eliminar:
            resultado.append(palabra)
    return ' '.join(resultado)

def procesar_texto(texto, opcion, *args):

    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "remplazar":
        if len(args) != 2:
            raise ValueError(f"Se esperan dos argumentos para reemplazar. Argumentos pasados: {len(args)}")
        return reemplazar_palabra(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError(f"Se espera un argumento para eliminar. Argumentos pasados: {len(args)}")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError(f"Opción no válida")

texto = "Este es un ejemplo de texto . Este texto contiene palabras repetidas."

conteo_palabras = procesar_texto(texto, "contar")
print("Conteo de palabras en el texto:")
print(conteo_palabras)

texto_reemplazado = procesar_texto(texto, "remplazar", "texto", "relato")
print("\nTexto con la palabra 'texto' reemplazada por 'relato':")
print(texto_reemplazado)

texto_sin_palabra = procesar_texto(texto, "eliminar", "ejemplo")
print("\nTexto con la palabra 'ejemplo' eliminada:")
print(texto_sin_palabra)
