# Laboratorium 1

## Zadanie 1

Wczytaj dwie nazwy miesięcy (nie sprawdzamy poprawności pisowni) i napisz, ile miesięcy mija od pierwszego z miesięcy do drugiego. Jeśli drugi jest wcześniejszy, to zakładamy, że jest on w następnym roku.  Przykład: marzec, maj, na wyjściu: 2; maj, styczeń, na wyjściu: 8; luty, luty, na wyjściu: 12. Dla wygody możesz ograniczyć sprawdzanie nazw miesięcy do pierwszych 3 liter.

## Zadanie 2

Napisz i zaprezentuj funkcję, która przyjmuje 2 napisy i stwierdza, czy przekazane teksty są w tym samym języku. Wskazówka: użyj przecięcia zbiorów; jeśli część wspólna zawiera przynajmniej 2 wspólne słowa (przy czym odrzucamy liczby etc. – użyj też metody isalpha()), to zakładamy zgodność języka.

## Zadanie 3

Dana jest lista zawierająca liczby całkowite. Nie używając pętli for ani while wygeneruj postać różnicową tej listy. 

```
Przykład: [100, 80, 20, 35, 90, 101, 99] --> [100, -20, -60, 15, 55, 11, -2]
```

## Zadanie 4

Dany jest adres IP i liczba bitów maski. Wypisz – w postaci binarnej i dziesiętnej – adres 
sieci, adres pierwszego i ostatniego hosta oraz adres rozgłoszeniowy (broadcast).

Przykład: 
wpisz IP oraz liczbę bitów maski oddzielone spacją 212.191.99.68 27

Zakładając że maska = 11111111.11111111.11111111.11100000

Adres sieci - uzyskujemy poprzez IP AND maska
> (‘212.191.99.64’, ‘11010100.10111111.01100011.01000000’)

Adres pierwszego hosta - uzyskujemy poprzez (IP AND maska) + 1
> (‘212.191.99.65’, ‘11010100.10111111.01100011.01000001’)

Adres rozgłoszeniowy - uzyskujemy poprzez IP OR (NOT maska)

> (‘212.191.99.95’, ‘11010100.10111111.01100011.01011111’)

Adres ostatniego hosta - uzyskujemy poprzez IP OR (NOT maska) -1
> (‘212.191.99.94’, ‘11010100.10111111.01100011.01011110’)
