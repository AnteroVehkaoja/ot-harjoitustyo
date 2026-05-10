## Sovellus

```mermaid
 classDiagram
    gameloop "1" --> "1" grid
    gameloop "1" --> "1" text
    gameloop "1" --> "1" renderer
    gameloop "1" --> "1" EventQueue
    gameloop "1" --> "1" Write
    gameloop "1" --> "1" Clock
    grid "1" --> "*" gridcell
    grid "1" --> "1" text
    MineZone "1" --> "1" gridcell
    renderer "1" --> "1" grid
    renderer "1" --> "1" text
```

sovelluksen pääosana on gameloop luokka mikä saa argumentteina Grid, Text, Renderer, EventQueue,Write ja Clock luokat

Intreaktio käyttäjän kanssa tapahtuu renderer ja evenqueue luokkien avulla, renderer näyttää käyttäjälle ruudukon ja eventqueue kerää informaation käyttäjän hiirestä ja näppäimistöstä.

Gameloop filtteröi eventqueuen antamia eventtejä ja kutsuu grid luokan metodia updateclick oikeilla parametreilla ja resetoi ruudukon kun painetaan r. updateclick palauttaa joko true tai false riippuen onko peli ohi klikkauksen aiheuttamana vai ei, jos kyllä se kirjoittaa tuloksen tiedostoon write luokan avulla.


Grid luokan olion luodessa, se tekee tyhjän ruudukon. Kun updateclick kutsutaan sallitussa paikassa ensimmäisen kerran luo grid luokka oikea ruudukon ja avaa tämän ruudun. Ennen ruudun näyttämistä käyttäjälle jos konfiguroitava GEN_GRID on "yes", grid injektoidaan solve funktiolle, mikä yrittää ratkaista ruudukon, jos se ei onnistu yritetään uudestaan 1000 kertaa.
