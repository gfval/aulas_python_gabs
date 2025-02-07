lista = {
    "cidade": {
        "sao paulo": [
            "Joao M",
            "Maria S",
            "Juan C",
            "Patrick G"
        ],
        "rio de janeiro": [
            "Joao P",
            "Maria M",
            "Juan JR"
        ]
    }
}

quantidade = sum(len(local) for local in lista["cidade"].values())
print(f"Quantidade total: {quantidade}")  # Saída: Quantidade total: 7
print(lista["cidade"]["rio de janeiro"])  # Saída: ['Joao P', 'Maria M',
# 'Juan JR']
