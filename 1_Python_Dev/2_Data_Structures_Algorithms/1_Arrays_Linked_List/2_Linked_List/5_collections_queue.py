from collections import deque


class BookmarkStack:
    def __init__(self):
        self.stack = deque()

    def add_bookmark(self, url, title):
        self.stack.append({
            'url': url,
            'title': title,
            'timestamp': '2024-03-30'  # En un caso real usarías datetime
        })

    def remove_last_bookmark(self):
        return self.stack.pop() if self.stack else None

    def peek_last_bookmark(self):
        return self.stack[-1] if self.stack else None

    def get_all_bookmarks(self):
        return list(self.stack)


# Uso
bookmarks = BookmarkStack()

# Agregar bookmarks
bookmarks.add_bookmark('https://python.org', 'Python Homepage')
bookmarks.add_bookmark('https://docs.python.org', 'Python Docs')
bookmarks.add_bookmark('https://pypi.org', 'Python Package Index')

# Ver todos los bookmarks
print("Todos los bookmarks:")
print(bookmarks.get_all_bookmarks())

# Ver último bookmark agregado
print("\nÚltimo bookmark:")
print(bookmarks.peek_last_bookmark())

# Eliminar último bookmark
removed = bookmarks.remove_last_bookmark()
print("\nBookmark eliminado:")
print(removed)

# Ver bookmarks restantes
print("\nBookmarks restantes:")
print(bookmarks.get_all_bookmarks())