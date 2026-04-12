import sqlite3


class Zadanie:
    def __init__(self, nazwa_zadania, status_zadania, db_id=None):
        self.id = db_id
        self.nazwa_zadania = nazwa_zadania
        self.status_zadania = status_zadania

    def opis(self):
        return f"Zadanie \"{self.nazwa_zadania}\" jest {self.status_zadania}"


class ListaZadan:
    def __init__(self):
        self.conn = sqlite3.connect("zadania.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS zadania (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nazwa_zadania TEXT UNIQUE,
                status_zadania TEXT
            )
        ''')
        self.conn.commit()

    def pobierz_zadania(self):
        self.cursor.execute("SELECT id, nazwa_zadania, status_zadania FROM zadania")
        rows = self.cursor.fetchall()
        return [Zadanie(row[1], row[2], row[0]) for row in rows]

    def dodaj_zadanie(self, zadanie):
        try:
            self.cursor.execute("INSERT INTO zadania (nazwa_zadania, status_zadania) VALUES (?, ?)",
                                (zadanie.nazwa_zadania, zadanie.status_zadania))
            self.conn.commit()
            return f"Zadanie \"{zadanie.nazwa_zadania}\" zostało dodane do bazy zadań"
        except sqlite3.IntegrityError:
            return f"Zadanie \"{zadanie.nazwa_zadania}\" już znajduje się w bazie"

    def usun_zadanie(self, indeks_zadania):
        zadania = self.pobierz_zadania()
        if 0 <= indeks_zadania < len(zadania):
            zadanie_do_usuniecia = zadania[indeks_zadania]
            self.cursor.execute("DELETE FROM zadania WHERE id = ?", (zadanie_do_usuniecia.id,))
            self.conn.commit()
            return f"Zadanie \"{zadanie_do_usuniecia.nazwa_zadania}\" zostało usunięte z bazy zadań"
        else:
            return "Nie ma zadania z takim numerem"

    def zmien_status_zadania(self, indeks_zadania, nowy_status_zadania):
        zadania = self.pobierz_zadania()
        if 0 <= indeks_zadania < len(zadania):
            zadanie = zadania[indeks_zadania]
            if zadanie.status_zadania == nowy_status_zadania:
                return "Wprowadziłeś taki sam status zadania, wprowadź inny status zadania"
            else:
                self.cursor.execute("UPDATE zadania SET status_zadania = ? WHERE id = ?",
                                    (nowy_status_zadania, zadanie.id))
                self.conn.commit()
                return f"Zmieniłeś status zadania na \"{nowy_status_zadania}\""
        else:
            return "Nie ma zadania z takim numerem"

    def wyswietl_liste_zadan(self):
        zadania = self.pobierz_zadania()
        if not zadania:
            print("Lista zadań jest pusta")
            return
        print("Lista zadań: ")
        for i, j in enumerate(zadania):
            print(f"{i + 1}. {j.nazwa_zadania} - {j.status_zadania}")

    def zamknij_polaczenie(self):
        self.conn.close()


print("Witamy w programie do zarządzania zadaniami")
lista_zadan = ListaZadan()
while True:
    print("\n1. Dodaj zadanie\n2. Usuń zadanie\n3. Zmień status\n4. Wyświetl listę\n5. Wyjdź")
    try:
        wybor = int(input("Podaj swój wybór: "))
    except ValueError:
        print("Niepoprawny wybór, podaj liczbę od 1 do 5")
        continue

    if wybor == 1:
        nazwa_zadania = input("Podaj nazwę zadania: ")
        status_zadania = input("Podaj status zadania: ")
        zadanie = Zadanie(nazwa_zadania, status_zadania)
        print(lista_zadan.dodaj_zadanie(zadanie))

    elif wybor == 2:
        lista_zadan.wyswietl_liste_zadan()
        try:
            indeks_zadania = int(input("Podaj numer zadania, które chcesz usunąć: ")) - 1
        except ValueError:
            print("Niepoprawny numer")
            continue
        print(lista_zadan.usun_zadanie(indeks_zadania))

    elif wybor == 3:
        lista_zadan.wyswietl_liste_zadan()
        try:
            indeks_zadania = int(input("Podaj numer zadania, status którego chcesz zmienić: ")) - 1
        except ValueError:
            print("Niepoprawny numer")
            continue
        nowy_status_zadania = input("Podaj status zadania: ")
        print(lista_zadan.zmien_status_zadania(indeks_zadania, nowy_status_zadania))

    elif wybor == 4:
        lista_zadan.wyswietl_liste_zadan()

    elif wybor == 5:
        lista_zadan.zamknij_polaczenie()
        print("Do zobaczenia")
        break