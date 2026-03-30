class Zadanie:
    def __init__(self, nazwa_zadania, status_zadania):
        self.nazwa_zadania = nazwa_zadania
        self.status_zadania = status_zadania

    def opis(self):
        return f"Zadanie \"{self.nazwa_zadania}\" jest {self.status_zadania}"

    def zmien_status_zadania(self, nowy_status_zadania):
        if self.status_zadania == nowy_status_zadania:
            return "Wprowadziłeś taki sam status zadania, wprowadź inny status zadania"
        else:
            self.status_zadania = nowy_status_zadania
            return f"Zmieniłeś status zadania na \"{nowy_status_zadania}\""

class ListaZadan:
    def __init__(self):
        self.lista_zadan = []

    def dodaj_zadanie(self, zadanie):
        if zadanie not in self.lista_zadan:
            self.lista_zadan.append(zadanie)
            return f"Zadanie \"{zadanie.nazwa_zadania}\" zostało dodane do listy zadań"
        else:
            return f"Zadanie \"{zadanie.nazwa_zadania}\" już znajduje się w liście"

    def usun_zadanie(self, indeks_zadania):
        if 0 <= indeks_zadania < len(self.lista_zadan):
            zadanie_do_usuniecia = self.lista_zadan[indeks_zadania]
            self.lista_zadan.remove(zadanie_do_usuniecia)
            return f"Zadanie \"{zadanie_do_usuniecia.nazwa_zadania}\" zostało usunięte z listy zadań"
        else:
            return "Nie ma zadania z takim numerem"


    def wyswietl_liste_zadan(self):
        if not self.lista_zadan:
            print("Lista zadań jest pusta")
            return
        print("Lista zadań: ")
        for i, j in enumerate(self.lista_zadan):
            print(f"{i + 1}. {j.nazwa_zadania} - {j.status_zadania}")

print("Witamy w programie do zarządzania zadaniami")
lista_zadan = ListaZadan()
while True:
    print("1.Dodaj zadanie \n2.Usuń zadanie \n3.Zmień status zadania \n4.Wyświetl listę zadań \n5.Zakończ program")
    wybor = int(input("Podaj swój wybór: "))
    if wybor == 1:
        nazwa_zadania = input("Podaj nazwę zadania: ")
        status_zadania = input("Podaj status zadania: ")
        zadanie = Zadanie(nazwa_zadania, status_zadania)
        print(lista_zadan.dodaj_zadanie(zadanie))
    elif wybor == 2:
        lista_zadan.wyswietl_liste_zadan()
        indeks_zadania = (int(input("Podaj numer zadania, które chcesz usunąć: "))) - 1
        print(lista_zadan.usun_zadanie(indeks_zadania))
    elif wybor == 3:
        lista_zadan.wyswietl_liste_zadan()
        indeks_zadania = (int(input("Podaj numer zadania, status którego chcesz zmienić: "))) - 1
        zadanie_w_ktorym_zmieniamy_status = lista_zadan.lista_zadan[indeks_zadania]
        nowy_status_zadania = input("Podaj status zadania: ")
        print(zadanie_w_ktorym_zmieniamy_status.zmien_status_zadania(nowy_status_zadania))
    elif wybor == 4:
        lista_zadan.wyswietl_liste_zadan()
    elif wybor == 5:
        print("Do zobaczenia")
        break