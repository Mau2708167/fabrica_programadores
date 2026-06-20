# Autor: 
# Projeto: Desvio Condicional

# Criação das Variáveis
nome = input('Qual é o seu nome? ')
idade = int(input(' Quantos anos você tem? '))
cidade = input('qual é sua cidade? ')
def status(idade):
    if idade>=12:
        print('você já é adolescente ')
    else:
        print('você ainda é o bebezinho da mamãe')

#chamada de funçao
status(idade)     