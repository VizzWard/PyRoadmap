from collections import deque


class PrintQueue:
    def __init__(self):
        self.queue = deque()

    def add_document(self, doc_name, pages, priority=False):
        document = {
            'name': doc_name,
            'pages': pages,
            'status': 'pending'
        }
        # Si es prioritario, añadir al inicio
        if priority:
            self.queue.appendleft(document)
        else:
            self.queue.append(document)

    def print_next(self):
        return self.queue.popleft() if self.queue else None

    def view_queue(self):
        return list(self.queue)


# Uso
printer = PrintQueue()

# Agregar documentos
printer.add_document("Reporte.pdf", 5)
printer.add_document("Factura.pdf", 1, priority=True)
printer.add_document("Manual.pdf", 15)

print("Cola de impresión:")
print(printer.view_queue())

# Imprimir siguiente documento
next_doc = printer.print_next()
print("\nImprimiendo:", next_doc['name'])

print("\nCola restante:")
print(printer.view_queue())