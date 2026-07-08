# Generator Kodu i Komunikacja TCP

Projekt na laboratorium - generator kodu serializacji/deserializacji danych do formatu binarnego (bez AI) przy użyciu szablonów Jinja2 oraz prosty test komunikacji przez gniazda TCP/IP.

## Jak to działa
1. W pliku `interface.json` definiujemy klasę i jej pola.
2. Skrypt `generate.py` bierze szablon z folderu `templates/` i generuje plik `generated_codec.py`.
3. Pliki `server.py` i `client.py` importują wygenerowaną klasę i przesyłają dane między sobą przez lokalną sieć.

## Struktura projektu
* `interface.json` - konfiguracja pól klasy
* `generate.py` - skrypt do generowania kodu
* `server.py` - serwer odbierający pakiety TCP
* `client.py` - klient wysyłający dane przez TCP
* `requirements.txt` - spis bibliotek (Jinja2)
* `templates/template.py.jinja2` - szablon dla generatora

## Uruchomienie

Najpierw trzeba przygotować środowisko i zainstalować potrzebną bibliotekę:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Żeby wygenerować kod z pliku JSON, wpisujemy:

```bash
python generate.py
```

Żeby przetestować działanie sieci, otwieramy dwa okna terminala. W pierwszym odpalamy serwer, a w drugim klienta:

```bash
# Terminal 1
python server.py

# Terminal 2
python client.py
```