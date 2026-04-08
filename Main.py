from LinkedList import LinkedList

lista = LinkedList()

while True:
    print("Menú")
    print("1 - Insertar al inicio")
    print("2 - Insertar al final")
    print("3 - Mostrar lista")
    print("4 - Buscar elemento")
    print("5 - Eliminar primer elemento")
    print("6 - Eliminar por valor")
    print("7 - Tamaño de la lista")
    print("8 - Invertir lista")
    print("9 - Ordenar lista")
    print("10 - Salir")

    opcion = input("Elige una opcion: ")

    match opcion:
        case 1:
            data = input("Ingrese el dato: ")
            lista.insert_at_beginning(data)
        case 2:
            data = input("Ingrese el dato: ")
            lista.insert_at_end(data)
        case 3:
            lista.display()
        case 4:
            data = input("Dato que desea buscar: ")
            print ("Resultado:", lista.search(data))
        case 5:
            lista.delete_first()
