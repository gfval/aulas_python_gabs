musicas = [
    {"titulo": "Smells Like Teen Spirit", "tocou": 3},
    {"titulo": "Thunderstruck", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too Young to Fall in Love", "tocou": 32}
]
print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])

mais_tocada = {{"titulo"} if "tocou" in musicas else "tocou": musica["tocou"]
               for musica in musicas}
print(mais_tocada)
