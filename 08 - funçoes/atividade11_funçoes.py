# Autor: 
# Projeto: Desvio Condicional

# Criação das Variáveis
nome = input('Qual é o seu nome? ')
salario = float(input(f"{nome}, digite seu salário: "))
calculo = salario * 0.10
def status(salario):
    if calculo > 100:
        print(f"O {nome} tem dinheiro!")
    else:
        print(f"O {nome} não tem dinheiro!")

#chamada de funçao
status(salario)        
