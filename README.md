# Trophy Hunter

Dwuwymiarowa gra platformowa napisana w Pythonie z użyciem biblioteki **Pygame**. Gracz wspina się po platformach w górę mapy, omija pociski przelatujące przez ekran i próbuje jak najszybciej dotrzeć do trofeum na szczycie. Liczy się czas: im szybciej, tym lepszy wynik.

## Funkcje

- **Wspinaczka w pionie**: kamera płynnie podąża za graczem w osi Y.
- **Fizyka**: grawitacja, skoki i kolizje z kafelkami mapy.
- **Przeszkody**: pociski poruszają się w poziomie co 100 pikseli wysokości, każdy z losową prędkością. Trafienie przez pocisk lub spadnięcie z mapy cofa gracza na start.
- **Animacje**: animacja biegu oraz sprite'y zwrócone w lewo lub w prawo zależnie od kierunku ruchu.
- **Tablica wyników**: czas każdego przejścia jest zapisywany, a gra pokazuje 5 najlepszych wyników.
- **Zapis gry**: z menu pauzy można zapisać pozycję gracza i czas gry, a potem wczytać je z menu głównego.
- **Grafika pixel-art**: obraz jest renderowany w rozdzielczości 320×240 i skalowany do okna 960×960.

## Uruchomienie

Wymagania: Python 3 i Pygame.

```sh
pip install pygame
python src/game.py
```

> Grę trzeba uruchamiać z **głównego katalogu repozytorium**, bo ścieżki do zasobów (`assets/...`) są względne.

## Sterowanie

| Klawisz | Akcja |
|---|---|
| ← / → | Ruch w lewo / w prawo |
| Spacja / ↑ | Skok (tylko gdy postać stoi na podłożu) |
| ESC | Pauza / powrót do gry |
| Lewy przycisk myszy | Obsługa przycisków w menu |

## Ekrany gry

- **Menu główne**: *Play* (nowa gra), *Score* (najlepsze wyniki), *Load* (wczytanie zapisu), *Exit* (wyjście).
- **Rozgrywka**: wspinaczka do trofeum, z licznikiem czasu działającym w tle.
- **Pauza**: *Save* zapisuje stan gry i wraca do menu, *Back* wraca do gry.
- **Ekran końcowy**: wyświetla czas przejścia i 5 najlepszych wyników.

## Struktura projektu

```
src/
  game.py        # klasa Game: pętla główna, stany gry, zapis/odczyt
  entity.py      # gracz: ruch, grawitacja, kolizje
  map.py, tile.py  # wczytywanie i rysowanie mapy z kafelków
  projectile.py  # pociski
  trophy.py      # trofeum (cel gry)
  menu.py, button.py  # menu i przyciski
  clouds.py, cloud.py # chmury w tle
  score.py       # pojedynczy wynik
  utils.py       # wczytywanie grafik i wyników
assets/
  levels/        # pliki z układem mapy
  tiles/, entities/, clouds/  # grafiki
  save.txt       # zapisany stan gry
  scores.txt     # historia wyników
docs/            # dokumentacja Sphinx
```

### Jak działa gra

Klasa `Game` działa jak prosta maszyna stanów. Flagi `in_menu`, `game_running`, `pause`, `post_game` i `viewing_score` decydują o tym, która pętla (menu, rozgrywka, pauza, ekran wyników) jest aktualnie aktywna. Wszystkie obiekty rysują się z przesunięciem o pozycję kamery (`camera_y`).

### Format plików

**Poziomy** (`assets/levels/*.txt`): każda linia opisuje jeden kafelek o rozmiarze 16×16 px:

```
x;y;nazwa_kafelka;numer_grafiki
48;224;grass;0
```

`x` i `y` to współrzędne w pikselach, a `grass;0` oznacza grafikę `assets/tiles/grass/0.png`. Gra wczytuje wszystkie pliki z tego katalogu, więc żeby dodać nowy fragment mapy, wystarczy dodać nowy plik.

**Wyniki** (`assets/scores.txt`):

```
MM:SS | data i godzina | liczba sekund
01:40 | 2025-06-11 12:34:05.124639 | 100
```

**Zapis gry** (`assets/save.txt`): 4 linie z pozycją x i y gracza, pozycją kamery i liczbą sekund gry. Zapis jest jednorazowy, bo plik zostaje wyczyszczony po wczytaniu.

## Dokumentacja

Dokumentację API generuje Sphinx (autodoc) na podstawie docstringów w kodzie:

```sh
cd docs
make html        # Windows: make.bat html
```

Wygenerowane strony trafiają do `docs/_build/html/`.

## Autor

Leonard Hołubowicz, 2025
