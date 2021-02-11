from os import remove


def abrir(nombre):
    archivo = open(nombre + ".txt", "a")
    archivo.close()
    archivo = open(nombre + ".txt", "r")
    print("----------------------------------------")
    print("Archivo: " + nombre)
    print("----------------------------------------")
    print("Contenido:")
    print("----------------------------------------")
    print(archivo.read())
    print("----------------------------------------")
    archivo.close()


def editar(nombre):
    aux = open(nombre + ".txt", "r")
    lineas = aux.read()
    aux.close()
    archivo = open(nombre + ".txt", "a")
    texto = input("Ingrese el texto: ")
    archivo.write(texto + "\n")
    while True:
        print("¿Desea agregar otra línea?")
        print("1. Sí")
        print("2. No\n")
        op = int(input("Escoja una opción: "))
        while op > 2 or op < 1:
            print("1. Sí")
            print("2. No\n")
            op = int(input("Escoja una opción: "))
        if op == 1:
            texto = input("Ingrese el texto: ")
            archivo.write(texto + "\n")
        elif op == 2:
            archivo.close()
            break
    guardar(nombre, lineas)


def guardar(nombre, aux):
    archivo = open(nombre + ".txt", "a")
    print("¿Desea guardar los cambios?")
    print("1. Sí")
    print("2. No\n")
    op = int(input("Escoja una opción: "))
    while op > 2 or op < 1:
        print("1. Sí")
        print("2. No\n")
        op = int(input("Escoja una opción: "))
    if op == 1:
        archivo.close()
        print("Cambios guardados exitosamente")
    elif op == 2:
        archivo.close()
        archivo = open(nombre + ".txt", "w")
        archivo.write(aux)
        archivo.close()
        print("Cambios descartados")


def eliminar(nombre):
    archivo = open(nombre+".txt", "a")
    archivo.close()
    remove(nombre+".txt")
    print("Archivo eliminado correctamente")


nombre = input("Ingrese nombre del archivo: ")
abrir(nombre)
while True:
    print("1. Editar archivo")
    print("2. Eliminar archivo")
    print("3. Salir\n")
    op = int(input("Escoja una opción: "))
    while op > 3 or op < 1:
        print("1. Editar archivo")
        print("2. Eliminar archivo")
        print("3. Salir\n")
        op = int(input("Escoja una opción: "))
    if op == 1:
        editar(nombre)
    elif op == 2:
        eliminar(nombre)
        break
    elif op == 3:
        break
