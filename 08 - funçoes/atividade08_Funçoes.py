# Criação das Variáveis
nome = input('Digite seu nome: ')
nota = float(input('Digite a nota final: '))

#funçao status do aluno
def status(nota):
    if nota>=6:
        print(f'Aluno: (nome) está aprovado')
    else:
        print(f"Aluno  (nome) está reprovado")

#chamada da funçao
status(nota)    