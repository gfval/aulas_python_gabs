prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

# zip() -> junta duas ou mais listas, tuplas, dicionários, etc.
# zip() -> retorna um iterador, que é um objeto que gera um elemento por vez
final0 = {dados[0]: max(dados[1], dados[2]) for dados in zip
          (alunos, prova1, prova2)}

final = zip(alunos, prova1, prova2)

print(final0)
print(list(final))

# ulizano map e lamda
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(list(final))
