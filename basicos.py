#lista
alimentos = []

def mostrar_alimentos():
    if len(alimentos) == 0:
        print("No hay alimentos\n")
    else:
        for alimento in alimentos:
            print(alimento["nombre"])
            print(alimento["precio"])
            print(alimento["cantidad"])
            print(f"{'-'*20}")

def agregar_alimento(nombre, precio, cantidad):
    alimento = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    alimentos.append(alimento)

mostrar_alimentos()

#argumentos posicionales
agregar_alimento("Leche", 70, 10)
agregar_alimento(nombre="huevo", precio=70, cantidad=10) 
agregar_alimento("Jamon", 70, 10)
agregar_alimento("Pan", 70, 10)
agregar_alimento("Queso", 70, 10)
agregar_alimento("Lechuga", 70, 10)
agregar_alimento("Tomate", 70, 10)
agregar_alimento("Pepino", 70, 10)
agregar_alimento("Papa", 70, 10)
agregar_alimento("Cebolla", 70, 10)

#mostrar_alimentos()
n=len(alimentos)
print(f"Actualmente hay {n} alimentos\n")
print(alimentos)


def buscar(producto):
    for i in range(n):
        if alimentos[i]["nombre"] == producto:
            return True, i
    print("No se encontro el alimento")
    return False, 0

alimento = input("Ingrese el alimento a buscar: ")
disponible, pos = buscar(alimento)
if disponible:
    print(f"{alimentos[pos]}")