try:
    idade = int(input("Qual sua idade? "))

    if idade > 30:
        print("Você é velho(a)")
    elif idade <= 19:
        print("Você é jovem")
    else:
        print("Você é adulto(a)")
except ValueError:
    print("Por favor, digite uma idade válida (número).")
