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
    renderer "1" --> "1" grid
    renderer "1" --> "1" text
```
