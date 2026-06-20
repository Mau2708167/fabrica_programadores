# Autor: 
# Projeto: Desvio Condicional

# Criação das Variáveis
nome = input('Qual é o seu nome? ')
idade = int(input('Quantos anos você tem? '))
def status (idade):
    if idade>=18:
        print(f'{nome}, você tem carteira de motorista? pode dirigir!')
    else:
        print(f"{nome}, você não tem idade suficiente para dirigir")
#chamada de funçao
status(idade)