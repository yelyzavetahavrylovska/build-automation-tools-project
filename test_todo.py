import unittest
import os

from TO_DO_APP import Zadanie, ListaZadan

class TestAplikacjiTodo(unittest.TestCase):

    def test_opis_zadania(self):
        """Sprawdza, czy opis zadania generuje się poprawnie."""
        zadanie = Zadanie("Test", "w toku")
        self.assertEqual(zadanie.opis(), 'Zadanie "Test" jest w toku')

    def test_dodawanie_zadania(self):
        """Sprawdza, czy zadanie jest poprawnie dodawane do bazy."""
        lista = ListaZadan()
        nowe_zadanie = Zadanie("Testowe zadanie", "nowe")
        wynik = lista.dodaj_zadanie(nowe_zadanie)
        
        # Sprawdzamy komunikat zwrotny
        self.assertIn("zostało dodane", wynik)
        
        # Sprawdzamy, czy fizycznie jest w bazie
        zadania = lista.pobierz_zadania()
        self.assertTrue(any(z.nazwa_zadania == "Testowe zadanie" for z in zadania))
        
        lista.zamknij_polaczenie()

    def test_usun_zadanie_nieistniejace(self):
        """Sprawdza reakcję na próbę usunięcia zadania o błędnym numerze."""
        lista = ListaZadan()
        wynik = lista.usun_zadanie(999) # Numer, którego na pewno nie ma
        self.assertEqual(wynik, "Nie ma zadania z takim numerem")
        lista.zamknij_polaczenie()

if __name__ == '__main__':
    unittest.main()
