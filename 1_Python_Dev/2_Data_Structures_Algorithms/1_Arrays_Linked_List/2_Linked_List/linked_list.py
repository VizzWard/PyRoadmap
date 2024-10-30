from node import node


class LinkedList:
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


    def insert(self, value, index: int = -1):
        new_node = node(value)

        # Si la lista está vacía
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
            return

        # Validar el índice
        if index < -1:
            raise IndexError("Index cannot be less than -1")
        if index > self.size:
            raise IndexError(f"Index out of range. List size is {self.size}")

        # Convertir índice -1 al índice final real
        if index == -1:
            index = self.size

        # Caso 1: Insertar al principio (índice 0)
        if index == 0:
            new_node.next = self.head
            self.head = new_node

        # Caso 2: Insertar al final
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node

        # Caso 3: Insertar en medio
        else:
            current = self.head
            # Nos movemos hasta la posición anterior donde queremos insertar
            for _ in range(index - 1):
                current = current.next
            # Insertamos el nuevo nodo
            new_node.next = current.next
            current.next = new_node

        self.size += 1


    def remove(self, value=None, index: int = None):
        if self.head is None:  # Lista vacía
            return False

        # Caso 1: Eliminar por índice
        if index is not None:
            if index >= self.size:  # Índice fuera de rango
                raise IndexError("Index out of range")

            if index == 0:  # Eliminar el primer elemento
                self.head = self.head.next
                if self.head is None:  # Si era el único elemento
                    self.tail = None
                self.size -= 1
                return True

            # Eliminar en una posición específica
            current = self.head
            pos = 0
            while pos < index - 1:
                current = current.next
                pos += 1

            # Actualizar tail si eliminamos el último elemento
            if current.next == self.tail:
                self.tail = current

            current.next = current.next.next
            self.size -= 1
            return True

        # Caso 2: Eliminar por valor
        if value is not None:
            if self.head.data == value:  # Si es el primer elemento
                self.head = self.head.next
                if self.head is None:  # Si era el único elemento
                    self.tail = None
                self.size -= 1
                return True

            current = self.head
            while current.next is not None:
                if current.next.data == value:
                    # Actualizar tail si eliminamos el último elemento
                    if current.next == self.tail:
                        self.tail = current

                    current.next = current.next.next
                    self.size -= 1
                    return True
                current = current.next

        return False  # No se encontró el elemento


    def traverse(self):
        if self.head is None:
            print("Lista vacía")
            return

        current = self.head
        position = 0
        while current is not None:
            print(f"Posición {position}: {current.data}")
            current = current.next
            position += 1


    def get_size(self):
        return self.size


    def is_empty(self):
        return self.size == 0