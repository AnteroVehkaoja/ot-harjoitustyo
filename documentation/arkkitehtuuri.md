```mermaid
 classDiagram
    gameloop "1" --> "1" grid
    gameloop "1" --> "1" text
    gameloop "1" --> "1" renderer
    gameloop "1" --> "1" EventQueue
    grid "1" --> "*" gridcell
    grid "1" --> "1" text
    renderer "1" --> "1" grid
    renderer "1" --> "1" text
```
