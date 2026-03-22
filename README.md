'TO-DO App'

Opis programu: 
TO-DO App to prosty program w Pythonie do zarządzania zadaniami. 
Umożliwia dodawanie, usuwanie, zmianę statusu oraz przeglądanie listy zadań.

Wymagania systemowe:
- Docker Desktop (Windows lub Linux)
- Na Windows wymagana jest integracja WSL2 do uruchamiania kontenerów

Instrukcja uruchomienia:

Budowanie obrazu Docker:
docker build -t todo-app .

Uruchamianie programu w kontenerze:
docker run -it todo-app

Wskazówki:
- Po zbudowaniu obrazu możesz uruchamiać program wielokrotnie poleceniem `docker run -it todo-app`.
- Program działa w terminalu w trybie interaktywnym.