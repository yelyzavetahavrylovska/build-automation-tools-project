# TO-DO App

## Opis projektu

TO-DO App to aplikacja napisana w Pythonie do zarządzania zadaniami w trybie terminalowym.
Pozwala na tworzenie, usuwanie, edytowanie oraz przeglądanie listy zadań zapisanych w bazie danych SQLite.

Aplikacja została rozbudowana o mechanizmy testowania oraz automatyzacji procesu budowy i uruchamiania przy użyciu Dockera oraz GitHub Actions.

## Funkcjonalności

* Dodawanie zadań
* Usuwanie zadań
* Zmiana statusu zadania
* Wyświetlanie listy zadań
* Wyszukiwanie zadań
* Ustawianie priorytetu (niski / normalny / wysoki)
* Automatyczne zapisywanie daty utworzenia i zakończenia zadania

## Technologie

Projekt wykorzystuje:

* Python 3.14
* SQLite jako bazę danych
* Docker i Docker Compose do uruchamiania aplikacji w kontenerze
* unittest do testów jednostkowych
* GitHub Actions do automatycznego uruchamiania testów przy każdym pushu i pull requeście

## Uruchomienie aplikacji

Aplikację można uruchomić lokalnie:

```bash
python TO_DO_APP.py
```

Lub przy użyciu Dockera:

```bash
docker build -t todo-app .
docker run -it todo-app
```

Możliwe jest również użycie Docker Compose:

```bash
docker-compose up --build
```

## Testy i automatyzacja

Testy jednostkowe można uruchomić lokalnie poleceniem:

```bash
python -m unittest discover
```

Dodatkowo projekt zawiera konfigurację GitHub Actions, która automatycznie uruchamia testy przy każdej zmianie w repozytorium.

## Struktura projektu

```
.
├── TO_DO_APP.py
├── test_todo.py
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .github/workflows/python-tests.yml
```

