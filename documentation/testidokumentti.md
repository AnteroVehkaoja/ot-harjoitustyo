# Testausdokumentti

Ohjelmaa on testattu yksikkötason unittesteillä ja manuaalisella testauksella.



### Testauskattavuus
<img width="867" height="310" alt="image" src="https://github.com/user-attachments/assets/36618e43-2868-4b5d-9bde-28fdc706ca6f" />

Suurin osa automaattisista testeistä on kohdistettu grid ja solve_algorithm tiedostoihin, mitkä käsittelevät suurimman osan sovelluksen logiikasta.

Muu sovelluksen toiminnasta on testattu manuaalisesti, mutta file ja timer ja gameloop tiedostoille pystyisi kirjoittamaan automaattisia testejä.

## Sovellukseen jääneet laatuongelmat

- sovellus ei kerro jos tuhannen kierroksen jälkeen sovellus ei pystynyt luomaan arvaamatonta ruudukkoa
