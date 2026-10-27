class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class ElementoPostre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cabeza = None


class GestorPostres:
    def __init__(self):
        self.postres = []

    def buscar_postre(self, nombre):
        for i, postre in enumerate(self.postres):
            if postre.nombre.lower() == nombre.strip().lower():
                return i
        return -1

    def imprimir_ingredientes(self, nombre_postre):
        if not self.postres:
            print("El arreglo POSTRES está vacío.")
            return

        idx = self.buscar_postre(nombre_postre)
        if idx == -1:
            print(f"El postre '{nombre_postre}' no existe.")
            return

        actual = self.postres[idx].cabeza
        if actual is None:
            print(f"'{self.postres[idx].nombre}' no tiene ingredientes (NIL).")
            return

        print(f"Ingredientes de '{self.postres[idx].nombre}':", end=" ")
        while actual is not None:
            print(f"[{actual.nombre}] ->", end=" ")
            actual = actual.siguiente
        print("NIL")

    def insertar_ingrediente(self, nombre_postre, ingrediente):
        idx = self.buscar_postre(nombre_postre)
        if idx == -1:
            print(f"El postre '{nombre_postre}' no existe.")
            return

        ingrediente = ingrediente.strip()
        if not ingrediente:
            return

        postre = self.postres[idx]
        nuevo_nodo = NodoIngrediente(ingrediente)

        if postre.cabeza is None:
            postre.cabeza = nuevo_nodo
            print(f"Ingrediente '{ingrediente}' agregado.")
            return

        actual = postre.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo
        print(f"Ingrediente '{ingrediente}' agregado.")

    def eliminar_ingrediente(self, nombre_postre, ingrediente):
        idx = self.buscar_postre(nombre_postre)
        if idx == -1:
            print(f"El postre '{nombre_postre}' no existe.")
            return

        postre = self.postres[idx]
        actual = postre.cabeza
        anterior = None

        if actual is None:
            print("El postre no tiene ingredientes para eliminar.")
            return

        if actual.nombre.lower() == ingrediente.strip().lower():
            postre.cabeza = actual.siguiente
            print(f"Ingrediente '{ingrediente}' eliminado.")
            return

        while actual is not None and actual.nombre.lower() != ingrediente.strip().lower():
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            print(f"El ingrediente '{ingrediente}' no se encontró.")
            return

        anterior.siguiente = actual.siguiente
        print(f"Ingrediente '{ingrediente}' eliminado.")

    def alta_postre(self, nombre_postre, lista_ingredientes):
        nombre_postre = nombre_postre.strip()
        if not nombre_postre:
            return

        nuevo_postre = ElementoPostre(nombre_postre)

        pos = 0
        while pos < len(self.postres) and self.postres[pos].nombre.lower() < nombre_postre.lower():
            pos += 1

        self.postres.insert(pos, nuevo_postre)
        print(f"Postre '{nombre_postre}' registrado.")

        for ing in lista_ingredientes:
            if ing.strip():
                nuevo_nodo = NodoIngrediente(ing.strip())
                if nuevo_postre.cabeza is None:
                    nuevo_postre.cabeza = nuevo_nodo
                else:
                    actual = nuevo_postre.cabeza
                    while actual.siguiente is not None:
                        actual = actual.siguiente
                    actual.siguiente = nuevo_nodo

    def baja_postre(self, nombre_postre):
        idx = self.buscar_postre(nombre_postre)
        if idx == -1:
            print(f"El postre '{nombre_postre}' no existe.")
            return

        self.postres[idx].cabeza = None
        eliminado = self.postres.pop(idx)
        print(f"Postre '{eliminado.nombre}' y sus ingredientes eliminados.")

    def eliminar_repetidos(self):
        if not self.postres:
            print("El arreglo POSTRES está vacío.")
            return

        i = 0
        while i < len(self.postres) - 1:
            if self.postres[i].nombre.lower() == self.postres[i + 1].nombre.lower():
                self.postres[i + 1].cabeza = None
                eliminado = self.postres.pop(i + 1)
                print(f"Postre repetido '{eliminado.nombre}' eliminado.")
            else:
                i += 1

        for postre in self.postres:
            actual = postre.cabeza
            while actual is not None:
                pivote = actual
                while pivote.siguiente is not None:
                    if pivote.siguiente.nombre.lower() == actual.nombre.lower():
                        repetido = pivote.siguiente.nombre
                        pivote.siguiente = pivote.siguiente.siguiente
                        print(f"Ingrediente repetido '{repetido}' eliminado de '{postre.nombre}'.")
                    else:
                        pivote = pivote.siguiente
                actual = actual.siguiente

        print("Limpieza de elementos repetidos completada.")

    def mostrar_estructura(self):
        print("\n--- ESTRUCTURA POSTRES ---")
        if not self.postres:
            print("[ Vacío ]")
        for i, postre in enumerate(self.postres):
            print(f"[{i}] {postre.nombre:<15} -> ", end="")
            actual = postre.cabeza
            while actual is not None:
                print(f"[{actual.nombre}] -> ", end="")
                actual = actual.siguiente
            print("NIL")
        print("--------------------------")


def menu():
    gestor = GestorPostres()

    gestor.alta_postre("Pastel", ["Harina", "Huevos", "Leche", "Azúcar", "Mantequilla"])
    gestor.alta_postre("Cheesecake", ["Queso crema", "Galletas", "Mantequilla", "Azúcar"])
    gestor.alta_postre("Brownie", ["Chocolate", "Mantequilla", "Huevos", "Azúcar", "Harina"])
    gestor.alta_postre("Arroz con leche", ["Arroz", "Leche", "Canela", "Azúcar"])

    while True:
        gestor.mostrar_estructura()
        print("a. Imprimir ingredientes")
        print("b. Insertar ingrediente")
        print("c. Eliminar ingrediente")
        print("d. Dar de alta un postre")
        print("e. Dar de baja un postre")
        print("f. Eliminar elementos repetidos")
        print("s. Salir")

        op = input("\nOpción: ").strip().lower()

        if op == 'a':
            gestor.imprimir_ingredientes(input("Nombre del postre: "))
        elif op == 'b':
            postre = input("Nombre del postre: ")
            ing = input("Nuevo ingrediente: ")
            gestor.insertar_ingrediente(postre, ing)
        elif op == 'c':
            postre = input("Nombre del postre: ")
            ing = input("Ingrediente a eliminar: ")
            gestor.eliminar_ingrediente(postre, ing)
        elif op == 'd':
            postre = input("Nuevo postre: ")
            ings = input("Ingredientes separados por coma (o Enter si no tiene): ")
            lista = [x.strip() for x in ings.split(",") if x.strip()]
            gestor.alta_postre(postre, lista)
        elif op == 'e':
            gestor.baja_postre(input("Postre a eliminar: "))
        elif op == 'f':
            gestor.eliminar_repetidos()
        elif op == 's':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()