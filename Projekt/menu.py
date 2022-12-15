# Klasa menu
class Menu:
  def __init__(self, database):
    # Obiekt bazy danych, z którego korzystać będzie menu
    self.database = database

  # Funkcja wyświetlająca menu i obsługująca wybór opcji przez użytkownika
  def display_menu(self):
    # Pętla obsługująca menu
    while True:
      # Wyświetlenie dostępnych opcji
      print("1. Wstaw dane")
      print("2. Usuń dane")
      print("3. Wyszukaj dane")
      print("4. Listuj dane")
      print("5. Zakończ program")
      # Pobranie wyboru opcji przez użytkownika
      choice = input("Wybierz opcję: ")
      # Obsługa wyboru opcji
      if choice == "1":
        # Wstawienie danych do bazy
        author = input("Podaj autora: ")
        title = input("Podaj tytuł: ")
        publication_date = input("Podaj datę publikacji: ")
        category = input("Podaj kategorię: ")
        book = Book(author, title, publication_date, category)
        self.database.insert(book)
        print("Dane zostały wstawione do bazy.")
      elif choice == "2":
        # Usuwanie książki z bazy
        author = input("Podaj autora: ")
        title = input("Podaj tytuł: ")
        book = Book(author, title)
        self.database.delete(book)
        print("Dane zostały usunięte z bazy.")
      elif choice == "3":
        # Wyszukiwanie danych w bazie
        query = input("Podaj szukane wyrażenie: ")
        results = self.database.search(query)
        print("Znaleziono następujące wyniki:")
        for result in results:
          print(result)
      elif choice == "4":
        # Listowanie wszystkich danych w bazie
        items = self.database.list()
        print("Lista wszystkich elementów w bazie:")
        for item in items:
          print(item)
      elif choice == "5":
        # Zakończenie programu
        break
      else:
        print("Nieprawidłowy wybór.")

# Uruchomienie programu
if __name__ == "__main__":
    # Stworzenie obiektu bazy danych
    database = Database()
    # Stworzenie obiektu menu
    menu = Menu(database)
    # Wyświetlenie menu
    menu.display_menu()