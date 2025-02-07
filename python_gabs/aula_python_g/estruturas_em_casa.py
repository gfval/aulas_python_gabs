"""
estruturas condicionais
if, elif, else

"""
idade = int(input("Qual sua idade?"))
if idade:
    if idade > 30:
        print("Voce é velho(a)")
    elif idade <= 19:
        print("Você é jovem")
    elif idade <= 20 or idade >= 30:  # Entre 20 e 30 anos
        print("Você é adulto(a)")
else:
    print("Digite sua idade")
