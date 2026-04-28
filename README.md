# Ohjelmistotekniikka, Minesweeper harjoitustyo

sovelluksella käyttäjän on tarkoitus pystyä pelaamaan miinaharavaa ja kirjoittamaan tulokset tiedostoon automaattisesti.


# documentaaatio
- [käyttöohje](https://github.com/AnteroVehkaoja/ot-harjoitustyo/blob/main/documentation/kayttoohje.md)
- [työpäiväkirja](https://github.com/AnteroVehkaoja/ot-harjoitustyo/blob/main/documentation/tyopaivakirja.md)
- [vaatimusmäärittely](https://github.com/AnteroVehkaoja/ot-harjoitustyo/blob/main/documentation/vaatimusmaarittely.md)
- [changelog](https://github.com/AnteroVehkaoja/ot-harjoitustyo/blob/main/documentation/changelog.md)
- [arkkitehtuuri](https://github.com/AnteroVehkaoja/ot-harjoitustyo/blob/main/documentation/arkkitehtuuri.md)
- [release1](https://github.com/AnteroVehkaoja/ot-harjoitustyo/releases/tag/week5)
- [release2](https://github.com/AnteroVehkaoja/ot-harjoitustyo/releases/tag/week6)

## asennus

- asenna riippuvuudet: 'poetry install'
- mene poetry virtualliympäristöön komennolls 'eval $(poetry env activate)'
- käynnistä: 'poetry run invoke start'


### invoke
Muita invoke komentoja on

1. poetry run invoke test  mikä ajaa testit
2. poetry run invoke coverage-report   mikä ajaa testit ja kirjoittaa raportin
3. poetry run invoke lint   ajaa pylint sovelluksen
   
