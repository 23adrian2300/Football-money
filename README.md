# Temat
Celem zadania jest napisanie prostego serwisu webowego realizującego pewną złożoną funkcjonalność w oparciu o otwarte serwisy udostępniające REST API. Stworzyć serwis, który:

* udostępni klientowi statyczną stronę HTML z formularzem do zebrania parametrów żądania,
* odbierze zapytanie od klienta,
* odpyta serwis publiczny (różne endpointy), a lepiej kilka serwisów o dane potrzebne do skonstruowania odpowiedzi,
* dokona odróbki otrzymanych odpowiedzi (np.: wyciągnięcie średniej, znalezienie ekstremów, porównanie wartości z różnych serwisów itp.),
* wygeneruje i wyśle odpowiedź do klienta (statyczna strona HTML z wynikami).

## Rowiązanie
Wykorzystałem następujące API:

Bez API_KEY:
(Do znajdywania najdroższego piłkarza)
- https://transfermarkt-api.vercel.app/docs

(Do szukania średnich min, max przy zamianie kwoty na PLN)
- https://api.nbp.pl/
- https://www.frankfurter.app/docs/

Z API_KEY:
(Do konwersji Euro na PLN przy wartośći piłkarza)
- https://currencyapi.com/
- https://www.exchangerate-api.com/

W związku z tym w pliku .env znajdują się klucze API_KEY do tych serwisów.

W moim rozwiązaniu występują dwa formularze, jeden pozwala na wyszukanie najdroższego piłkarza w danej drużynie, a drugi pozwala na zamianę kwoty z Euro na PLN.
Zrobiłem tak, gdyż miałem problem z api pobierającym piłkarza, gdyż przez pewnien czas nie działało. Dlatego zrobiłem drugi formularz, który pozwala na zamianę kwoty z Euro na PLN, aby mieć awaryjnie jakieś rozwiązanie.

W pliku .env znajdują się klucze API_KEY do tych serwisów. Oczywiście, aby aplikacja działała poprawnie, należy dodać tam swoje klucze.
Tak samo należy podać api_key do samego api w main.py. Różne klucze znajdują się w pliku api_key.txt. Należy wykorzystać jeden z nich aby móc korzystać z aplikacji.

Jeśli trzeba można użyć:

`pip install -r requiements.txt`

Aby uruchomić:

`uvicorn main:app --reload --port 8002`

Numer portu można zmieniać na inny.
