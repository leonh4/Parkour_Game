# Pygame Platformer - Trophy Hunter

Projekt to dwuwymiarowa gra platformowa zrealizowana z wykorzystaniem biblioteki Pygame. Celem gracza jest dotarcie do trofeum umieszczonego na szczycie mapy, unikając przy tym generowanych losowo pocisków oraz przeszkód terenowych.

## Mechanika i działanie programu

Gra opiera się na maszynie stanów, która zarządza przejściami między menu głównym, rozgrywką, pauzą a ekranem wyników.

### Kluczowe systemy

- **Fizyka i ruch**: Implementacja grawitacji, kolizji z kafelkami mapy oraz skoków. Ruch postaci wspiera animacje (bieg, bezczynność) zależne od kierunku i stanu encji.
    
- **System walki i przeszkód**: Dynamiczna lista obiektów typu `Projectile`, które poruszają się w poprzek ekranu. Kolizja z pociskiem skutkuje śmiercią gracza i resetem pozycji.
    
- **Kamera**: System śledzenia gracza w osi Y (pionowej), zapewniający płynne podążanie widoku za wspinającą się postacią.
    
- **Zapis i odczyt stanu**: Możliwość zapisu bieżącej pozycji gracza, współrzędnych kamery oraz czasu gry do pliku tekstowego, co pozwala na późniejszą kontynuację rozgrywki.
    

### Zarządzanie wynikami

Program mierzy czas przejścia poziomu, a po zdobyciu trofeum przelicza go na wynik punktowy. Dane są archiwizowane, co pozwala na wyświetlanie listy pięciu najlepszych wyników (Best Scores) w menu oraz po zakończeniu gry.

### Sterowanie

- **Strzałki (Lewo/Prawo)**: Poruszanie postacią.
    
- **Spacja / Strzałka w górę**: Skok (dostępny tylko, gdy postać dotyka podłoża).
    
- **ESC**: Pauza i dostęp do menu zapisu.