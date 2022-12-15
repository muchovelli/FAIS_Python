# Biblioteki potrzebne do obsługi plików i danych w formacie JSON
import json
import os


# Klasa książki
class Book:
    def __init__(self, author, title, publication_date, category):
        self.author = author
        self.title = title
        self.publication_date = publication_date
        self.category = category


# Klasa bazy danych
class Database:
    def __init__(self):
        # Nazwa pliku, w którym zapisywane będą dane bazy danych
        self.filename = "books.json"
        # Sprawdzenie, czy plik z danymi istnieje. Jeśli nie, utworzenie pustego pliku
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("[]")

    # Funkcja wstawiająca dane do bazy
    def insert(self, book):
        # Odczytanie danych z pliku
        with open(self.filename, "r") as f:
            books = json.load(f)
        # Dodanie nowej książki do już istniejących
        books.append(book.__dict__)
        # Zapisanie danych do pliku
        with open(self.filename, "w") as f:
            json.dump(books, f)

    # Funkcja usuwająca dane z bazy
    def delete(self, book):
        # Odczytanie danych z pliku
        with open(self.filename, "r") as f:
            books = json.load(f)
        # Usuwanie książki z bazy
        books.remove(book.__dict__)
        # Zapisanie danych do pliku
        with open(self.filename, "w") as f:
            json.dump(books, f)

    # Funkcja wyszukująca dane w bazie
    def search(self, query):
        # Odczytanie danych z pliku
        with open(self.filename, "r") as f:
            books = json.load(f)
        # Lista wyników wyszukiwania
        results = []
        # Wyszukiwanie książek
        for book in books:
            if query in book["author"] or query in book["title"] or query in book["category"]:
                results.append(book)
        # Zwrócenie wyników wyszukiwania
        return results

        # Funkcja listująca wszystkie dane w bazie
    def list(self):
        # Odczytanie danych z pliku
        with open(self.filename, "r") as f:
            books = json.load(f)
        # Zwrócenie listy książek
        return books
