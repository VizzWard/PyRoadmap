from linked_list import LinkedList


class Task:
    def __init__(self, description, priority="Media"):
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"{self.description} (Prioridad: {self.priority})"

    def __repr__(self):
        return self.__str__()


def mostrar_menu():
    print("\n=== Lista de Tareas Pendientes ===")
    print("1. Agregar tarea al final")
    print("2. Agregar tarea prioritaria (al inicio)")
    print("3. Agregar tarea en posición específica")
    print("4. Eliminar tarea")
    print("5. Mostrar todas las tareas")
    print("6. Salir")


def main():
    todo_list = LinkedList()

    # Agregamos algunas tareas de ejemplo
    todo_list.insert(Task("Hacer la compra", "Baja"))
    todo_list.insert(Task("Preparar presentación", "Alta"))
    todo_list.insert(Task("Llamar al médico", "Media"))

    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-6): ")

        if opcion == "1":
            desc = input("Descripción de la tarea: ")
            prio = input("Prioridad (Alta/Media/Baja): ")
            todo_list.insert(Task(desc, prio))
            print("Tarea agregada al final de la lista!")

        elif opcion == "2":
            desc = input("Descripción de la tarea prioritaria: ")
            todo_list.insert(Task(desc, "Alta"), 0)
            print("Tarea prioritaria agregada al inicio!")

        elif opcion == "3":
            desc = input("Descripción de la tarea: ")
            prio = input("Prioridad (Alta/Media/Baja): ")
            pos = int(input(f"Posición (0-{todo_list.get_size()}): "))
            try:
                todo_list.insert(Task(desc, prio), pos)
                print(f"Tarea agregada en la posición {pos}!")
            except IndexError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            if todo_list.is_empty():
                print("La lista está vacía!")
                continue

            print("\nTareas actuales:")
            todo_list.traverse()
            pos = int(input("\nIngrese la posición de la tarea a eliminar: "))
            try:
                todo_list.remove(index=pos)
                print("Tarea eliminada exitosamente!")
            except IndexError as e:
                print(f"Error: {e}")

        elif opcion == "5":
            if todo_list.is_empty():
                print("No hay tareas pendientes!")
            else:
                print("\nLista de tareas:")
                todo_list.traverse()
                print(f"\nTotal de tareas: {todo_list.get_size()}")

        elif opcion == "6":
            print("\n¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    main()