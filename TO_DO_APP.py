import sqlite3
from datetime import datetime


class Zadanie:
    def __init__(self, nazwa_zadania, status_zadania, priorytet="Normalny", created_at=None, db_id=None):
        self.id = db_id
        self.nazwa_zadania = nazwa_zadania
        self.status_zadania = status_zadania
        self.priorytet = priorytet
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def opis(self):
        return f'Zadanie "{self.nazwa_zadania}" jest {self.status_zadania}'


class ListaZadan:
    def __init__(self, db_path="zadania.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS zadania (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nazwa_zadania TEXT UNIQUE,
                status_zadania TEXT,
                priorytet TEXT,
                created_at TEXT
            )
        ''')
        try:
            self.cursor.execute("ALTER TABLE zadania ADD COLUMN priorytet TEXT DEFAULT 'Normalny'")
        except sqlite3.OperationalError:
            pass
        self.conn.commit()

    def pobierz_zadania(self):
        self.cursor.execute("SELECT id, nazwa_zadania, status_zadania, priorytet, created_at FROM zadania")
        rows = self.cursor.fetchall()
        return [Zadanie(row[1], row[2], row[3], row[4], row[0]) for row in rows]

    def dodaj_zadanie(self, zadanie):
        try:
            self.cursor.execute(
                "INSERT INTO zadania (nazwa_zadania, status_zadania, priorytet, created_at) VALUES (?, ?, ?, ?)",
                (zadanie.nazwa_zadania, zadanie.status_zadania, zadanie.priorytet, zadanie.created_at)
            )
            self.conn.commit()
            return f'Zadanie "{zadanie.nazwa_zadania}" zostało dodane do bazy zadań'
        except sqlite3.IntegrityError:
            return f'Zadanie "{zadanie.nazwa_zadania}" już znajduje się w bazie'

    def usun_zadanie(self, indeks_zadania):
        zadania = self.pobierz_zadania()
        if 0 <= indeks_zadania < len(zadania):
            zadanie = zadania[indeks_zadania]
            self.cursor.execute("DELETE FROM zadania WHERE id = ?", (zadanie.id,))
            self.conn.commit()
            return f'Zadanie "{zadanie.nazwa_zadania}" zostało usunięte z bazy zadań'
        return "Nie ma zadania z takim numerem"

    def zmien_status_zadania(self, indeks_zadania, nowy_status_zadania):
        zadania = self.pobierz_zadania()
        if 0 <= indeks_zadania < len(zadania):
            zadanie = zadania[indeks_zadania]

            if zadanie.status_zadania == nowy_status_zadania:
                return "Wprowadziłeś taki sam status zadania, wprowadź inny status zadania"

            self.cursor.execute(
                "UPDATE zadania SET status_zadania = ? WHERE id = ?",
                (nowy_status_zadania, zadanie.id)
            )
            self.conn.commit()
            return f'Zmieniłeś status zadania na "{nowy_status_zadania}"'

        return "Nie ma zadania z takim numerem"

    def wyswietl_liste_zadan(self):
        zadania = self.pobierz_zadania()
        if not zadania:
            print("Lista zadań jest pusta")
            return

        print("Lista zadań:")
        for i, z in enumerate(zadania):
            print(f"{i + 1}. {z.nazwa_zadania} [{z.priorytet}] - {z.status_zadania} [Utworzono: {z.created_at}]")

    def szukaj_zadania(self, fraza):
        self.cursor.execute("SELECT id, nazwa_zadania, status_zadania, priorytet, created_at FROM zadania WHERE nazwa_zadania LIKE ?", (f'%{fraza}%',))
        rows = self.cursor.fetchall()
        zadania = [Zadanie(row[1], row[2], row[3], row[4], row[0]) for row in rows]

        if not zadania:
            print(f"Nie znaleziono zadań pasujących do: {fraza}")
            return

        print(f"Wyniki wyszukiwania dla: {fraza}")
        for i, z in enumerate(zadania):
            print(f"{i + 1}. {z.nazwa_zadania} [{z.priorytet}] - {z.status_zadania} [Utworzono: {z.created_at}]")

    def zamknij_polaczenie(self):
        self.conn.close()


if __name__ == "__main__":
    print("Witamy w programie do zarządzania zadaniami")
    lista_zadan = ListaZadan()

    while True:
        print("\n1. Dodaj zadanie\n2. Usuń zadanie\n3. Zmień status\n4. Wyświetl listę\n5. Szukaj zadania\n6. Wyjdź")

        try:
            wybor = int(input("Podaj swój wybór: "))
        except ValueError:
            print("Niepoprawny wybór, podaj liczbę od 1 do 6")
            continue

        if wybor == 1:
            nazwa_zadania = input("Podaj nazwę zadania: ")
            if not nazwa_zadania.strip():
                print("Nazwa zadania nie może być pusta")
                continue
            status_zadania = input("Podaj status zadania(Nowe, Wykonane, W trakcie): ").lower()
            if status_zadania not in ("nowe", "wykonane", "w trakcie"):
                print("Nieprawidłowy status zadania. Wybierz: Nowe, Wykonane, W trakcie")
                continue
            priorytet = input("Podaj priorytet (Niski, Normalny, Wysoki): ").lower()
            if priorytet not in ("niski", "normalny", "wysoki"):
                print("Nieprawidłowy priorytet. Wybierz: Niski, Normalny lub Wysoki")
                continue
            zadanie = Zadanie(nazwa_zadania, status_zadania, priorytet)
            print(lista_zadan.dodaj_zadanie(zadanie))

        elif wybor == 2:
            lista_zadan.wyswietl_liste_zadan()
            try:
                indeks_zadania = int(input("Podaj numer zadania do usunięcia: ")) - 1
            except ValueError:
                print("Niepoprawny numer")
                continue
            print(lista_zadan.usun_zadanie(indeks_zadania))

        elif wybor == 3:
            lista_zadan.wyswietl_liste_zadan()
            try:
                indeks_zadania = int(input("Podaj numer zadania: ")) - 1
            except ValueError:
                print("Niepoprawny numer")
                continue

            nowy_status = input("Podaj nowy status: ").lower()
            if nowy_status not in ("nowe", "wykonane", "w trakcie"):
                print("Nieprawidłowy status zadania. Wybierz: Nowe, Wykonane, W trakcie")
                continue
            print(lista_zadan.zmien_status_zadania(indeks_zadania, nowy_status))

        elif wybor == 4:
            lista_zadan.wyswietl_liste_zadan()

        elif wybor == 5:
            fraza = input("Podaj frazę do wyszukania: ")
            lista_zadan.szukaj_zadania(fraza)

        elif wybor == 6:
            lista_zadan.zamknij_polaczenie()
            print("Do zobaczenia")
            break